#!/usr/bin/env python3
"""EXP-001: LLM framework for collaborative debugging task generation.

Two modes:
  --prepare-only  verify data and compute execution metrics, no network, no API key
  (default)       run the three prompt modules plus the LLM judge
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import re
import subprocess
import tarfile
import tempfile
import urllib.request
import uuid
from datetime import datetime, timezone
from pathlib import Path

import yaml
from importlib.metadata import PackageNotFoundError, version
from time import monotonic

from experiment_trace import ConfigChangedError, RunLog, capture_terminal, sha256_text

ROOT = Path(__file__).resolve().parents[1]


def load_dotenv() -> None:
    """Load ROOT/.env into os.environ without overriding existing values."""
    path = ROOT / ".env"
    if not path.is_file():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def gcc_version(cfg: dict) -> str | None:
    try:
        cp = subprocess.run(
            [cfg["evaluation"]["gcc"], "--version"],
            capture_output=True, text=True, timeout=5, check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    return cp.stdout.splitlines()[0] if cp.stdout.strip() else None


def package_version(name: str) -> str | None:
    try:
        return version(name)
    except PackageNotFoundError:
        return None


def load_config(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def dataset_root(cfg: dict) -> Path:
    archive = ROOT / cfg["data"]["archive"]
    assert archive.is_file(), f"missing archive: {archive}"
    assert sha256(archive) == cfg["data"]["sha256"], "archive SHA-256 mismatch"
    target = ROOT / "data" / "raw" / f"ITSP-{cfg['data']['commit']}"
    if not target.is_dir():
        with tarfile.open(archive) as tf:
            tf.extractall(target, filter="data")
    roots = list(target.glob("*/dataset"))
    assert len(roots) == 1, f"expected one dataset dir, got {roots}"
    return roots[0]


def statement_from_main(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    head = text.split("#include", 1)[0]
    lines = []
    for line in head.splitlines():
        line = line.strip().lstrip("*").strip()
        if line in ("/**", "/*", "*/", ""):
            continue
        lines.append(line)
    return "\n".join(lines).strip()


def load_items(cfg: dict) -> list[dict]:
    data = dataset_root(cfg)
    items: list[dict] = []
    for main in sorted(data.glob("Lab-*/*/Main.c")):
        lab, prob_id = main.parent.parent.name, main.parent.name
        tests = []
        for inp in sorted(
            (data / "test").glob(f"in.{prob_id}.*.txt"),
            key=lambda p: int(p.name.split(".")[-2]),
        ):
            idx = inp.name.split(".")[-2]
            out = data / "test" / f"out.{prob_id}.{idx}.txt"
            if out.is_file():
                tests.append((inp.read_text(encoding="utf-8", errors="replace"),
                              out.read_text(encoding="utf-8", errors="replace")))
        for buggy in sorted(main.parent.glob("*_buggy.c")):
            student = buggy.name.removesuffix("_buggy.c")
            correct = main.parent / f"{student}_correct.c"
            if not correct.is_file() or not tests:
                continue
            items.append({
                "item_id": f"{lab}-{prob_id}-{student}",
                "lab": lab,
                "difficulty_proxy": int(lab.split("-")[-1]),
                "statement": statement_from_main(main),
                "buggy_code": buggy.read_text(encoding="utf-8", errors="replace"),
                "correct_code": correct.read_text(encoding="utf-8", errors="replace"),
                "tests": tests,
            })
    return items


def normalized(out: str) -> list[str]:
    return [line.rstrip() for line in out.replace("\r\n", "\n").strip().splitlines() if line.strip()]


def compile_and_run(
    code: str, tests: list, work: Path, cfg: dict,
    trace: RunLog, variant: str, item_id: str,
) -> dict:
    src = work / "prog.c"
    binary = work / "prog"
    src.write_text(code, encoding="utf-8")
    cp = subprocess.run(
        [cfg["evaluation"]["gcc"], "-std=gnu99", "-O0", "-w", str(src), "-o", str(binary)],
        capture_output=True, timeout=cfg["evaluation"]["compile_timeout_s"],
    )
    if cp.returncode != 0:
        reference = trace.artifact(
            f"{item_id}-{variant}-gcc.stderr", cp.stderr.decode(errors="replace")
        )
        trace.event(
            "compile_failed", variant=variant, error_class="CompileError",
            returncode=cp.returncode, output_ref=reference,
        )
        return {"compiled": False, "passed": 0, "total": len(tests)}
    passed = 0
    for stdin, expected in tests:
        try:
            run = subprocess.run(
                [str(binary)], input=stdin.encode(), capture_output=True,
                timeout=cfg["evaluation"]["run_timeout_s"],
            )
            if run.returncode == 0 and normalized(run.stdout.decode(errors="replace")) == normalized(expected):
                passed += 1
        except subprocess.TimeoutExpired:
            trace.event("run_timeout", variant=variant, error_class="TimeoutExpired")
            continue
    return {"compiled": True, "passed": passed, "total": len(tests)}


def execution_metrics(items: list[dict], cfg: dict, trace: RunLog) -> tuple[list[dict], dict]:
    results = []
    with tempfile.TemporaryDirectory() as td:
        work = Path(td)
        for item in items:
            item_id = item["item_id"]
            with trace.item(item_id):
                buggy = compile_and_run(
                    item["buggy_code"], item["tests"], work, cfg, trace, "buggy", item_id
                )
                correct = compile_and_run(
                    item["correct_code"], item["tests"], work, cfg, trace, "correct", item_id
                )
                for variant, result in (("buggy", buggy), ("correct", correct)):
                    trace.event(
                        "item_executed", variant=variant, compiled=result["compiled"],
                        passed=result["passed"], total=result["total"],
                    )
                trace.event(
                    "item_compiled",
                    buggy_compiled=buggy["compiled"], correct_compiled=correct["compiled"],
                    buggy_passed=buggy["passed"], correct_passed=correct["passed"],
                    total=buggy["total"],
                )
            results.append({"item_id": item_id, "buggy": buggy, "correct": correct})
    n = len(results)
    fail_to_pass = sum(
        1 for r in results
        if r["buggy"]["compiled"] and r["correct"]["compiled"]
        and r["buggy"]["passed"] < r["correct"]["passed"]
    )
    return results, {
        "n_items": n,
        "buggy_compiled": sum(r["buggy"]["compiled"] for r in results),
        "correct_compiled": sum(r["correct"]["compiled"] for r in results),
        "fail_to_pass_items": fail_to_pass,
        "fail_to_pass_rate": round(fail_to_pass / n, 4) if n else 0.0,
    }


def call_llm(cfg: dict, messages: list[dict], session: str) -> str:
    key = os.environ.get(cfg["model"]["api_key_env"])
    if not key:
        raise SystemExit(
            f"Missing {cfg['model']['api_key_env']}. Set it in your shell before running "
            "the generation mode, or use --prepare-only."
        )
    url = cfg["model"]["base_url"].rstrip("/") + cfg["model"]["chat_path"]
    payload = {
        "model": cfg["model"]["name"],
        "messages": messages,
        "temperature": cfg["model"]["temperature"],
        "max_tokens": cfg["model"]["max_tokens"],
    }
    if cfg["model"].get("thinking"):
        payload["thinking"] = {"type": cfg["model"]["thinking"]}
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode(), method="POST",
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "User-Agent": cfg["model"]["user_agent"],
            cfg["model"]["session_header"]: session,
        },
    )
    with urllib.request.urlopen(req, timeout=cfg["model"]["timeout_s"]) as resp:
        body = json.loads(resp.read().decode())
    return body["choices"][0]["message"]["content"]


def call_llm_traced(
    cfg: dict, messages: list[dict], session: str,
    trace: RunLog, module: str,
) -> str:
    prompt = messages[0]["content"]
    prompt_ref = trace.artifact(f"prompt-{module}-{sha256_text(prompt)[:12]}.txt", prompt)
    began = monotonic()
    try:
        response = call_llm(cfg, messages, session)
    except Exception as exc:
        trace.event(
            "item_prompted", module=module, status="failed",
            prompt_sha256=prompt_ref["sha256"], prompt_bytes=prompt_ref["bytes"],
            error_class=type(exc).__name__, latency_s=round(monotonic() - began, 3),
        )
        raise
    response_ref = trace.artifact(
        f"response-{module}-{sha256_text(response)[:12]}.txt", response
    )
    trace.event(
        "item_prompted", module=module, status="ok",
        prompt_sha256=prompt_ref["sha256"], prompt_bytes=prompt_ref["bytes"],
        response_sha256=response_ref["sha256"], response_bytes=response_ref["bytes"],
        latency_s=round(monotonic() - began, 3),
    )
    return response


def role(content: str) -> dict:
    return {"role": "user", "content": content}


def generation_for_item(item: dict, cfg: dict, session: str, trace: RunLog) -> dict:
    statement = item["statement"]
    buggy = item["buggy_code"]
    dims = cfg["judge"]["dimensions"]

    context_prompt = (
        "You are designing a debugging exercise for introductory C programmers.\n"
        f"Authentic problem statement:\n{statement}\n\nBuggy student code:\n{buggy}\n\n"
        "Produce five distinct candidate debugging tasks. Use exactly five blocks starting "
        "with 'CANDIDATE 1:' through 'CANDIDATE 5:'. Each block states what the partner must find and fix.\n"
    )
    candidates = call_llm_traced(cfg, [role(context_prompt)], session, trace, "candidates")

    persona = (
        "Pair profile: two students, one with more C practice and one with less; both can read "
        "compiler output but differ in patience with trace inspection.\n"
        "Review these five candidates:\n" + candidates + "\n"
        "Select the one best matched to this pair. Reply with 'SELECTED: <number>' and a short reason.\n"
    )
    selection = call_llm_traced(cfg, [role(persona)], session, trace, "selection")

    cues = (
        "Collaboration: locate the fault together.\n"
        "Cooperation: split driver and navigator roles.\n"
        "Negotiation: disagree about the root cause and decide on a patch.\n"
        "Ideas sharing: explain and justify the hypothesis.\n"
        "Rewrite the selected task into one collaborative debugging task with four labelled sections: "
        "COLLABORATION:, COOPERATION:, NEGOTIATION:, IDEAS_SHARING:. Do not reveal the fix.\n"
        + selection
    )
    final_task = call_llm_traced(cfg, [role(cues)], session, trace, "rewrite")

    judge_prompt = (
        "Score the following debugging task from 1 to 5 on each dimension. "
        "Reply with one line per dimension in the form 'name: score'.\n"
        + final_task
    )
    raw_judge = call_llm_traced(cfg, [role(judge_prompt)], session, trace, "judge")
    scores = {}
    for d in dims:
        match = re.search(rf"{d}\s*:\s*([1-5])", raw_judge, re.IGNORECASE)
        if match:
            scores[d] = int(match.group(1))
            trace.event("judge_scored", dimension=d, score=scores[d], parse_ok=True)
    missing = [d for d in dims if d not in scores]
    if missing:
        trace.event(
            "judge_parse_failed", error_class="JudgeParseError",
            missing=missing, expected=len(dims), parsed=len(scores),
        )
    trace.event(
        "item_parsed", module="judge", parse_ok=not missing,
        parsed=len(scores), expected=len(dims),
    )
    return {
        "item_id": item["item_id"],
        "candidates": candidates,
        "selection": selection,
        "final_task": final_task,
        "judge_raw": raw_judge,
        "judge_scores": scores,
        "judge_parse_ok": len(scores) == len(dims),
    }


def run(cfg: dict, args: argparse.Namespace, trace: RunLog, config_sha: str) -> None:
    mode = "prepare" if args.prepare_only else "full"
    exp_dir = ROOT / "experiments" / cfg["experiment"]
    trace.start(mode=mode, config_sha256=config_sha, data_sha256=cfg["data"]["sha256"])

    with trace.stage("verify_data"):
        all_items = load_items(cfg)
    with trace.stage("sampling"):
        rng = random.Random(cfg["seed"])
        items = rng.sample(all_items, min(cfg["data"]["n_items"], len(all_items)))
        items.sort(key=lambda x: x["item_id"])
    with trace.stage("compile"):
        exec_results, execution = execution_metrics(items, cfg, trace)

    derived = ROOT / "data" / "processed" / cfg["experiment"]
    derived.mkdir(parents=True, exist_ok=True)
    (derived / "items.jsonl").write_text(
        "\n".join(json.dumps(i, ensure_ascii=False) for i in items) + "\n", encoding="utf-8"
    )

    generation = None
    if not args.prepare_only:
        with trace.stage("generation"):
            session = str(uuid.uuid5(uuid.NAMESPACE_URL, cfg["experiment"] + cfg["data"]["commit"]))
            records = []
            for item in items:
                with trace.item(item["item_id"]):
                    records.append(generation_for_item(item, cfg, session, trace))
            (derived / "generations.jsonl").write_text(
                "\n".join(json.dumps(r, ensure_ascii=False) for r in records) + "\n", encoding="utf-8"
            )
        with trace.stage("judge"):
            parsed = [r for r in records if r["judge_parse_ok"]]
            generation = {
                "n_items": len(records),
                "judge_parseable": len(parsed),
                "mean_by_dimension": {
                    d: round(sum(r["judge_scores"][d] for r in parsed) / len(parsed), 4) if parsed else None
                    for d in cfg["judge"]["dimensions"]
                },
            }

    metrics = {
        "experiment": cfg["experiment"],
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "config_sha256": config_sha,
        "seed": cfg["seed"],
        "run_id": trace.run_id,
        "attempt": trace.attempt,
        "events_path": str((exp_dir / "events.jsonl").relative_to(ROOT)),
        "data": {
            "name": cfg["data"]["name"],
            "commit": cfg["data"]["commit"],
            "archive_sha256": cfg["data"]["sha256"],
            "n_items_available": len(all_items),
            "n_items_selected": len(items),
        },
        "model": None if args.prepare_only else {
            "name": cfg["model"]["name"],
            "base_url": cfg["model"]["base_url"],
        },
        "execution": execution,
        "generation": generation,
        "execution_per_item": exec_results,
    }
    (exp_dir / "metrics.json").write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    (exp_dir / "data-manifest.json").write_text(json.dumps({
        "source": cfg["data"]["url"],
        "commit": cfg["data"]["commit"],
        "sha256": cfg["data"]["sha256"],
        "license": cfg["data"]["license"],
        "download_date": "2026-11-23",
        "local_archive": cfg["data"]["archive"],
        "n_items_available": len(all_items),
    }, indent=2) + "\n", encoding="utf-8")
    trace.write_provenance(
        data_sha256=cfg["data"]["sha256"],
        gcc=gcc_version(cfg),
        pyyaml=package_version("PyYAML"),
        model=None if args.prepare_only else cfg["model"]["name"],
        gateway=None if args.prepare_only else cfg["model"]["base_url"],
        n_items=len(items),
    )
    with (ROOT / "experiments/LEDGER.md").open("a", encoding="utf-8") as fh:
        fh.write(
            f"| {datetime.now(timezone.utc).date()} | {cfg['experiment']} | "
            f"structured prompts elicit collaborative debugging | seed={cfg['seed']}, "
            f"n={len(items)}, mode={mode}, run_id={trace.run_id} | "
            f"fail_to_pass={execution['fail_to_pass_rate']} | "
            f"{'data verified only' if args.prepare_only else 'generation recorded'} |\n"
        )
    trace.finish(mode=mode, n_items=len(items), fail_to_pass_rate=execution["fail_to_pass_rate"])
    print(json.dumps({
        "mode": mode,
        "run_id": trace.run_id,
        "attempt": trace.attempt,
        "n_items": len(items),
        "execution": execution,
        "generation": generation,
    }, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default=str(ROOT / "experiments/EXP-001/config.yaml"))
    parser.add_argument("--prepare-only", action="store_true")
    args = parser.parse_args()
    load_dotenv()

    cfg = load_config(Path(args.config))
    config_sha = sha256(Path(args.config))
    try:
        trace = RunLog(
            cfg["experiment"],
            run_dir=ROOT / "experiments" / cfg["experiment"],
            local_dir=ROOT / "experiments" / "outputs" / cfg["experiment"],
            config=cfg,
            repo=ROOT,
            config_sha256=config_sha,
        )
    except ConfigChangedError as exc:
        print(f"refusing to run: {exc}")
        raise SystemExit(2) from None

    with trace, capture_terminal(trace):
        run(cfg, args, trace, config_sha)


if __name__ == "__main__":
    main()
