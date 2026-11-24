#!/usr/bin/env python3
"""Generic reader for append-only experiment traces."""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable, Mapping


def load_events(path: str | Path) -> list[dict]:
    source = Path(path)
    if not source.is_file():
        return []
    events = []
    for lineno, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid JSON at {source}:{lineno}") from exc
    return events


def summarize(events: Iterable[Mapping[str, Any]]) -> dict:
    runs: dict[str, dict] = {}
    stages: list[dict] = []
    items: dict[str, dict] = defaultdict(dict)
    errors: list[dict] = []
    item_keys = (
        "variant", "buggy_compiled", "correct_compiled", "buggy_passed",
        "correct_passed", "passed", "total", "compiled", "parse_ok",
        "dimension", "score", "error_class", "status", "module",
    )
    for event in events:
        name = event.get("event")
        run_id = event.get("run_id", "")
        if name == "started":
            runs[run_id] = {
                "run_id": run_id,
                "attempt": event.get("attempt"),
                "mode": event.get("mode"),
                "config_sha256": event.get("config_sha256"),
                "started_utc": event.get("timestamp_utc"),
                "status": "running",
                "wall_time_s": None,
            }
        elif name == "stage_started":
            stages.append({
                "run_id": run_id,
                "attempt": event.get("attempt"),
                "stage": event.get("stage"),
                "t_s": event.get("t_s", 0.0),
                "duration_s": None,
            })
        elif name == "stage_completed":
            for stage in reversed(stages):
                if (stage["run_id"] == run_id and stage["stage"] == event.get("stage")
                        and stage["duration_s"] is None):
                    stage["duration_s"] = event.get("duration_s")
                    break
        elif name in ("completed", "failed"):
            if run_id in runs:
                runs[run_id]["status"] = "completed" if name == "completed" else "failed"
                runs[run_id]["wall_time_s"] = event.get("wall_time_s")
            if name == "failed":
                errors.append({
                    "run_id": run_id,
                    "attempt": event.get("attempt"),
                    "error_class": event.get("error_class"),
                    "timestamp_utc": event.get("timestamp_utc"),
                })
        if event.get("item_id"):
            bucket = items[event["item_id"]]
            for key in item_keys:
                if key in event:
                    bucket.setdefault(key, []).append(event[key])
    return {"runs": list(runs.values()), "stages": stages, "items": dict(items), "errors": errors}
