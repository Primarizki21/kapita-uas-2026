#!/usr/bin/env python3
"""Plot EXP-001 trace artifacts. Missing data is reported, never invented."""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import yaml

from experiment_report import load_events, summarize
ROOT = Path(__file__).resolve().parents[1]
EXP_DIR = ROOT / "experiments" / "EXP-001"
OUT_DIR = ROOT / "experiments" / "outputs" / "EXP-001" / "figures"


def plot_stage_timeline(summary: dict) -> None:
    rows = [
        (f'{s["stage"]} [a{s["attempt"]}]', s["t_s"], s["duration_s"])
        for s in summary["stages"] if s["duration_s"] is not None
    ]
    if not rows:
        print("[skip] stage timeline: no completed stages")
        return
    fig, ax = plt.subplots(figsize=(8, 3.5))
    ax.barh([r[0] for r in rows], [r[2] for r in rows], left=[r[1] for r in rows])
    ax.set_xlabel("seconds since run start")
    ax.set_title("EXP-001 stage timeline")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "stage_timeline.png", dpi=150)
    plt.close(fig)


def plot_pass_rates(metrics: dict) -> None:
    rows = metrics.get("execution_per_item") or []
    if not rows:
        print("[skip] pass rate per item: no execution records")
        return
    buggy = [r["buggy"]["passed"] / r["buggy"]["total"] if r["buggy"]["total"] else 0.0 for r in rows]
    correct = [r["correct"]["passed"] / r["correct"]["total"] if r["correct"]["total"] else 0.0 for r in rows]
    fig, ax = plt.subplots(figsize=(10, 3.5))
    ax.plot(range(len(rows)), buggy, "o-", markersize=3, label="buggy")
    ax.plot(range(len(rows)), correct, "s-", markersize=3, label="correct")
    ax.set_ylim(-0.05, 1.05)
    ax.set_xlabel("item order")
    ax.set_ylabel("pass rate")
    ax.set_title("EXP-001 pass rate per item")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT_DIR / "pass_rate_per_item.png", dpi=150)
    plt.close(fig)


def plot_judge(metrics: dict) -> None:
    means = ((metrics.get("generation") or {}).get("mean_by_dimension")) or {}
    if not means or all(value is None for value in means.values()):
        print("[skip] judge scores: full run not recorded")
        return
    config = yaml.safe_load((EXP_DIR / "config.yaml").read_text(encoding="utf-8"))
    scale = config["judge"]["scale_max"]
    fig, ax = plt.subplots(figsize=(7, 3.5))
    ax.bar(list(means), [means[d] for d in means])
    ax.set_ylim(0, scale)
    ax.set_ylabel(f"mean score (1-{scale})")
    ax.set_title("EXP-001 judge scores")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "judge_scores.png", dpi=150)
    plt.close(fig)


def plot_failures(summary: dict, metrics: dict) -> None:
    compile_failures = sum(
        1 for row in metrics.get("execution_per_item", [])
        if not row["buggy"]["compiled"] or not row["correct"]["compiled"]
    )
    runtime_failures = len(summary["errors"])
    if not compile_failures and not runtime_failures:
        print("[skip] failure breakdown: no failures recorded")
        return
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.bar(["compile failed", "run failed"], [compile_failures, runtime_failures])
    ax.set_ylabel("count")
    ax.set_title("EXP-001 failure breakdown")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "failure_breakdown.png", dpi=150)
    plt.close(fig)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    summary = summarize(load_events(EXP_DIR / "events.jsonl"))
    metrics = json.loads((EXP_DIR / "metrics.json").read_text(encoding="utf-8"))
    plot_stage_timeline(summary)
    plot_pass_rates(metrics)
    plot_judge(metrics)
    plot_failures(summary, metrics)
    print(f"figures: {OUT_DIR}")


if __name__ == "__main__":
    main()
