#!/usr/bin/env python3
"""Reusable append-only run trace for experiments.

Callers supply the experiment id, paths, config, and the names and payloads of
domain events. This module has no knowledge of any specific experiment.
"""
from __future__ import annotations

import hashlib
import json
import platform
import subprocess
import sys
import traceback
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from time import monotonic, time
from typing import Any, Iterator, Mapping

try:
    import resource
except ImportError:  # pragma: no cover - non POSIX platforms
    resource = None


class ConfigChangedError(RuntimeError):
    """Raised when an existing trace was written with a different config."""


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def canonical_config_sha256(config: Mapping[str, Any]) -> str:
    return sha256_text(json.dumps(config, sort_keys=True, separators=(",", ":"), default=str))


def git_sha(repo: Path) -> str:
    try:
        cp = subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "HEAD"],
            capture_output=True, text=True, timeout=5, check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return "unknown"
    return cp.stdout.strip() if cp.returncode == 0 else "unknown"


class RunLog:
    """Append-only event stream plus local raw artifacts for one run."""

    def __init__(
        self,
        experiment_id: str,
        *,
        run_dir: Path,
        local_dir: Path,
        config: Mapping[str, Any],
        repo: Path = Path.cwd(),
        config_sha256: str | None = None,
    ) -> None:
        self.experiment_id = experiment_id
        self.run_dir = Path(run_dir)
        self.local_dir = Path(local_dir)
        self.config = config
        self.repo = Path(repo)
        self.config_sha256 = config_sha256 or canonical_config_sha256(config)
        self.events_path = self.run_dir / "events.jsonl"
        self.run_log_path = self.local_dir / "run.log"
        self.errors_path = self.local_dir / "errors.log"
        self.provenance_path = self.run_dir / "provenance.json"
        self.started_utc = datetime.now(timezone.utc).isoformat()
        self.run_id = f"{experiment_id}-{utc_stamp()}-{self.config_sha256[:8]}"
        self.attempt = self._next_attempt()
        self._stage = ""
        self._item_id = ""
        self._mono_start = monotonic()
        self._wall_start = time()
        self._fh = None

    def _next_attempt(self) -> int:
        if not self.events_path.is_file():
            return 1
        attempts = []
        for line in self.events_path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            event = json.loads(line)
            previous = event.get("config_sha256")
            if previous is not None and previous != self.config_sha256:
                raise ConfigChangedError(
                    f"{self.events_path} holds config_sha256={previous}; "
                    f"current config_sha256={self.config_sha256}"
                )
            if isinstance(event.get("attempt"), int):
                attempts.append(event["attempt"])
        return max(attempts, default=0) + 1

    def __enter__(self) -> "RunLog":
        self.run_dir.mkdir(parents=True, exist_ok=True)
        self.local_dir.mkdir(parents=True, exist_ok=True)
        self._fh = self.events_path.open("a", encoding="utf-8")
        return self

    def __exit__(self, exc_type, exc, tb) -> bool:
        if exc_type is not None and exc is not None:
            self.fail(exc)
        if self._fh is not None:
            self._fh.close()
            self._fh = None
        return False

    def context(self) -> tuple[str, str]:
        return self._stage, self._item_id

    def _wall_time(self) -> float:
        return round(time() - self._wall_start, 3)

    def _write(self, name: str, **payload: Any) -> None:
        event = {
            "event": name,
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "t_s": round(monotonic() - self._mono_start, 3),
            "run_id": self.run_id,
            "attempt": self.attempt,
        }
        if self._stage:
            event["stage"] = self._stage
        if self._item_id:
            event["item_id"] = self._item_id
        event.update(payload)
        self._fh.write(json.dumps(event, ensure_ascii=False, default=str) + "\n")
        self._fh.flush()

    def start(self, *, mode: str, config_sha256: str | None = None, **payload: Any) -> None:
        self._write(
            "started",
            mode=mode,
            config_sha256=config_sha256 or self.config_sha256,
            git_sha=git_sha(self.repo),
            **payload,
        )

    def event(self, name: str, **payload: Any) -> None:
        self._write(name, **payload)

    @contextmanager
    def stage(self, name: str) -> Iterator[None]:
        previous = self._stage
        self._stage = name
        self._write("stage_started")
        begin = monotonic()
        try:
            yield
        except Exception as exc:
            self._write(
                "stage_failed",
                error_class=type(exc).__name__,
                duration_s=round(monotonic() - begin, 3),
            )
            self._stage = previous
            raise
        else:
            self._write("stage_completed", duration_s=round(monotonic() - begin, 3))
            self._stage = previous

    @contextmanager
    def item(self, item_id: str) -> Iterator[None]:
        previous = self._item_id
        self._item_id = item_id
        try:
            yield
        finally:
            self._item_id = previous

    def artifact(self, name: str, text: str) -> dict:
        """Store raw text locally; return only a reference safe for committed events."""
        (self.local_dir / name).write_text(text, encoding="utf-8")
        return {"artifact": name, "sha256": sha256_text(text), "bytes": len(text.encode("utf-8"))}

    def fail(self, exc: BaseException) -> None:
        self.errors_path.write_text(traceback.format_exc(), encoding="utf-8")
        self._write("failed", error_class=type(exc).__name__, wall_time_s=self._wall_time())

    def finish(self, **totals: Any) -> None:
        self._write("completed", wall_time_s=self._wall_time(), **totals)

    def write_provenance(self, **extra: Any) -> None:
        payload: dict[str, Any] = {
            "experiment": self.experiment_id,
            "run_id": self.run_id,
            "attempt": self.attempt,
            "config_sha256": self.config_sha256,
            "git_sha": git_sha(self.repo),
            "started_utc": self.started_utc,
            "python": platform.python_version(),
            "platform": platform.platform(),
            "wall_time_s": self._wall_time(),
        }
        if resource is not None:
            payload["peak_rss_mb"] = round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024, 2)
        payload.update(extra)
        self.provenance_path.write_text(
            json.dumps(payload, indent=2, default=str) + "\n", encoding="utf-8"
        )


class _Tee:
    def __init__(self, stream, log_path: Path, run_id: str, context, tag: str) -> None:
        self.stream = stream
        self.log_path = log_path
        self.run_id = run_id
        self.context = context
        self.tag = tag
        self._buffer = ""

    def write(self, data: str) -> int:
        self._buffer += data
        while "\n" in self._buffer:
            line, self._buffer = self._buffer.split("\n", 1)
            self._emit(line)
        return len(data)

    def _emit(self, line: str) -> None:
        stage, item_id = self.context()
        prefix = f"[{self.run_id}][{stage or '-'}][{item_id or '-'}]"
        text = f"{prefix} {self.tag} {line}\n"
        self.stream.write(text)
        self.stream.flush()
        with self.log_path.open("a", encoding="utf-8") as fh:
            fh.write(text)

    def flush(self) -> None:
        if self._buffer:
            line, self._buffer = self._buffer, ""
            self._emit(line)
        self.stream.flush()


@contextmanager
def capture_terminal(trace: RunLog) -> Iterator[None]:
    original_out, original_err = sys.stdout, sys.stderr
    out = _Tee(original_out, trace.run_log_path, trace.run_id, trace.context, "OUT")
    err = _Tee(original_err, trace.run_log_path, trace.run_id, trace.context, "ERR")
    sys.stdout, sys.stderr = out, err
    try:
        yield
    finally:
        out.flush()
        err.flush()
        sys.stdout, sys.stderr = original_out, original_err
