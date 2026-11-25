#!/usr/bin/env python3
"""Build notebooks/walkthrough.ipynb from real snippets and artifacts.

Snippets are extracted verbatim from src/ at build time. Code cells are executed
here once so stdout and plots are embedded; no Jupyter dependency is needed.
"""
from __future__ import annotations

import base64
import contextlib
import io
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "notebooks" / "walkthrough.ipynb"
EXP = ROOT / "experiments" / "EXP-001"


def source_block(path: Path, name: str, *, method: str | None = None) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    needle = f"{'    ' if method else ''}def {name}("
    start = next(i for i, line in enumerate(lines) if line.startswith(needle))
    while start > 0 and lines[start - 1].lstrip().startswith("@"):
        start -= 1
    indent = len(lines[start]) - len(lines[start].lstrip())
    end = len(lines)
    for i in range(start + 1, len(lines)):
        line = lines[i]
        if not line.strip():
            continue
        current = len(line) - len(line.lstrip())
        if current <= indent and not line.lstrip().startswith("#"):
            end = i
            break
    return "\n".join(lines[start:end]).rstrip()


EXP001 = ROOT / "src" / "exp001.py"
TRACE = ROOT / "src" / "experiment_trace.py"
REPORT = ROOT / "src" / "exp001_report.py"

SNIPPETS = {
    "config": source_block(EXP001, "load_config"),
    "items": source_block(EXP001, "load_items"),
    "compile": source_block(EXP001, "execution_metrics"),
    "prompt": source_block(EXP001, "call_llm_traced"),
    "trace": "\n\n".join(
        source_block(TRACE, name, method=True)
        for name in ("_next_attempt", "_write", "start")
    ),
    "provenance": source_block(TRACE, "write_provenance", method=True),
    "report": source_block(REPORT, "main"),
}

INTRO = """Notebook ini menjelaskan alur pipeline dan jejaknya. Angka di bawah dibaca dari artifact hasil run yang sebenarnya, bukan dihitung ulang dari data mentah."""

PAIRS = [
    (
        "1. Data dan pertanyaan",
        "Config menetapkan seed, arsip ITSP, model, dan butir yang dipakai. Pertanyaan praktisnya: apakah pipeline menghasilkan tugas yang lolos pemeriksaan eksekusi dan memenuhi rubrik sosial?",
        "config",
        """import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import yaml

ROOT = Path.cwd()
if not (ROOT / "pyproject.toml").is_file():
    ROOT = ROOT.parent
D = ROOT / "experiments" / "EXP-001"
FIG = ROOT / "experiments" / "outputs" / "EXP-001" / "figures"
PROCESSED = ROOT / "data" / "processed" / "EXP-001"

cfg = yaml.safe_load((D / "config.yaml").read_text(encoding="utf-8"))
manifest = json.loads((D / "data-manifest.json").read_text(encoding="utf-8"))
metrics = json.loads((D / "metrics.json").read_text(encoding="utf-8"))


def show_figure(name: str) -> None:
    plt.figure(figsize=(10, 4))
    plt.imshow(plt.imread(FIG / name))
    plt.axis("off")
    plt.show()


summary = pd.DataFrame(
    [
        ("seed", cfg["seed"]),
        ("dataset", cfg["data"]["name"]),
        ("n_available", manifest["n_items_available"]),
        ("n_selected", cfg["data"]["n_items"]),
        ("model", cfg["model"]["name"]),
        ("temperature", cfg["model"]["temperature"]),
        ("run_id", metrics["run_id"]),
    ],
    columns=["field", "value"],
)
print(summary.to_string(index=False))""",
    ),
    (
        "2. Dari arsip ke contoh butir",
        "Fungsi load_items memilih butir secara deterministik. Dua baris di bawah menunjukkan bentuk data yang masuk ke pipeline.",
        "items",
        """items = pd.DataFrame(
    [json.loads(line) for line in (PROCESSED / "items.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
)
sample = items[["item_id", "lab", "difficulty_proxy"]].head(2).copy()
sample["statement_preview"] = items["statement"].head(2).str.replace("\\n", " ", regex=False).str[:60] + "..."
sample["n_tests"] = items["tests"].head(2).apply(len)
print(sample.to_string(index=False))

generations = pd.DataFrame(
    [json.loads(line) for line in (PROCESSED / "generations.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
)
print("\\nContoh final_task:")
print(generations["final_task"].iloc[0][:420])""",
    ),
    (
        "3. Kompilasi dan fail-to-pass",
        "Kode buggy dan benar dikompilasi, lalu dibandingkan jumlah test yang lulus. Plot dibaca dari artifact yang sama dengan metrik.",
        "compile",
        """execution = pd.DataFrame(list(metrics["execution"].items()), columns=["metric", "value"])
print(execution.to_string(index=False))
show_figure("pass_rate_per_item.png")""",
    ),
    (
        "4. Prompt dan judge",
        "Empat panggilan LLM per butir menghasilkan kandidat, seleksi, rewrite, dan skor. Rubrik memakai empat kompetensi sosial.",
        "prompt",
        """judge = pd.DataFrame(
    list(metrics["generation"]["mean_by_dimension"].items()),
    columns=["dimension", "mean_score"],
)
print(judge.to_string(index=False))
print(f"judge_parseable: {metrics['generation']['judge_parseable']}/{metrics['generation']['n_items']}")
show_figure("judge_scores.png")""",
    ),
    (
        "5. Trace core",
        "RunLog menulis event append-only, menghitung attempt, dan menolak config yang berubah.",
        "trace",
        """events = [
    json.loads(line)
    for line in (D / "events.jsonl").read_text(encoding="utf-8").splitlines()
    if line.strip()
]
event_counts = pd.Series([event["event"] for event in events]).value_counts()
print(event_counts.rename_axis("event").rename("count").to_string())
show_figure("stage_timeline.png")""",
    ),
    (
        "6. Provenance dan artifact lokal",
        "Provenance mencatat versi dan hash. Plot kegagalan merangkum error yang tercatat selama run.",
        "provenance",
        """provenance = json.loads((D / "provenance.json").read_text(encoding="utf-8"))
rows = [(key, value) for key, value in provenance.items() if not isinstance(value, (dict, list))]
print(pd.DataFrame(rows, columns=["field", "value"]).to_string(index=False))
show_figure("failure_breakdown.png")""",
    ),
    (
        "7. Dari kode ke plot",
        "Plot dibangun oleh skrip terpisah dari artifact yang sama. Notebook hanya menampilkannya di bagian yang relevan.",
        "report",
        """figures = sorted(path.name for path in FIG.glob("*.png"))
print("artifact plot:")
print("\\n".join(f"- {name}" for name in figures))""",
    ),
]


def main() -> None:
    cells: list[dict] = []

    def add_markdown(text: str) -> None:
        cells.append({
            "cell_type": "markdown",
            "id": f"cell-{len(cells):02d}",
            "metadata": {},
            "source": text.splitlines(True),
        })

    def add_code(source: str, outputs: list[dict]) -> None:
        cells.append({
            "cell_type": "code",
            "execution_count": sum(c["cell_type"] == "code" for c in cells) + 1,
            "id": f"cell-{len(cells):02d}",
            "metadata": {},
            "outputs": outputs,
            "source": source.splitlines(True),
        })

    add_markdown(INTRO)
    namespace: dict = {}
    images: list[str] = []
    original_show = plt.show

    def capture_show(*args, **kwargs) -> None:
        buffer = io.BytesIO()
        plt.gcf().savefig(buffer, format="png", dpi=120)
        images.append(base64.b64encode(buffer.getvalue()).decode("ascii"))
        plt.close("all")

    plt.show = capture_show
    try:
        for heading, sentence, snippet_key, source in PAIRS:
            snippet = SNIPPETS[snippet_key]
            add_markdown(f"## {heading}\n\n{sentence}\n\n```python\n{snippet}\n```")
            images.clear()
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout):
                exec(compile(source, heading, "exec"), namespace)
            outputs: list[dict] = []
            if stdout.getvalue():
                outputs.append({
                    "output_type": "stream",
                    "name": "stdout",
                    "text": stdout.getvalue().splitlines(True),
                })
            for image in images:
                outputs.append({
                    "output_type": "display_data",
                    "data": {"image/png": image},
                    "metadata": {},
                })
            add_code(source, outputs)
    finally:
        plt.show = original_show

    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3 (kapita-uas)",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3.13"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(notebook, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(cells)} cells)")


if __name__ == "__main__":
    main()
