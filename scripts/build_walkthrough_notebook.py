#!/usr/bin/env python3
"""Build notebooks/EXP-001-walkthrough.ipynb from real snippets and artifacts.

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
OUT = ROOT / "notebooks" / "EXP-001-walkthrough.ipynb"
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

INTRO = """Notebook ini menjelaskan apa yang dikerjakan kode EXP-001 dan jejaknya. Angka di bawah dibaca dari artifact hasil run yang sebenarnya, bukan dihitung ulang dari data mentah."""

PAIRS = [
    (
        "1. Data dan pertanyaan",
        "Config menetapkan seed, arsip ITSP, dan 20 butir yang dipakai.",
        "config",
        """import json
import sys
import yaml
from pathlib import Path

ROOT = Path.cwd()
if not (ROOT / "pyproject.toml").is_file():
    ROOT = ROOT.parent
D = ROOT / "experiments" / "EXP-001"

cfg = yaml.safe_load((D / "config.yaml").read_text(encoding="utf-8"))
manifest = json.loads((D / "data-manifest.json").read_text(encoding="utf-8"))
print(json.dumps({
    "seed": cfg["seed"],
    "dataset": cfg["data"]["name"],
    "commit": cfg["data"]["commit"],
    "sha256": cfg["data"]["sha256"],
    "n_items": cfg["data"]["n_items"],
    "n_items_available": manifest["n_items_available"],
}, indent=2))""",
    ),
    (
        "2. Dari arsip ke 20 butir",
        "Fungsi ini memilih butir secara deterministik dari dataset hasil ekstraksi.",
        "items",
        """metrics = json.loads((D / "metrics.json").read_text(encoding="utf-8"))
print(json.dumps(metrics["data"], indent=2))""",
    ),
    (
        "3. Kompilasi dan fail-to-pass",
        "Kode buggy dan benar dikompilasi, lalu dibandingkan jumlah test yang lulus.",
        "compile",
        """print(json.dumps(metrics["execution"], indent=2))""",
    ),
    (
        "4. Prompt dan judge",
        "Empat panggilan LLM per butir menghasilkan kandidat, seleksi, rewrite, dan skor.",
        "prompt",
        """print(json.dumps(metrics["generation"], indent=2))""",
    ),
    (
        "5. Trace core",
        "RunLog menulis event append-only, menghitung attempt, dan menolak config yang berubah.",
        "trace",
        """from collections import Counter

events = [
    json.loads(line)
    for line in (D / "events.jsonl").read_text(encoding="utf-8").splitlines()
    if line.strip()
]
print(json.dumps({
    "events": len(events),
    "by_name": dict(Counter(event["event"] for event in events)),
    "attempts": sorted({
        event.get("attempt") for event in events if event.get("attempt") is not None
    }),
}, indent=2))""",
    ),
    (
        "6. Provenance dan artifact lokal",
        "Provenance mencatat versi dan hash, sementara teks mentah tetap di folder yang diabaikan git.",
        "provenance",
        """provenance = json.loads((D / "provenance.json").read_text(encoding="utf-8"))
local = ROOT / "experiments" / "outputs" / "EXP-001"
print(json.dumps(provenance, indent=2))
print("local files:", len(list(local.glob("*"))))
print("figures:", [path.name for path in sorted((local / "figures").glob("*.png"))])""",
    ),
    (
        "7. Visualisasi",
        "Empat plot dibaca dari artifact dan ditampilkan di sini tanpa menghitung ulang angka.",
        "report",
        """import matplotlib.pyplot as plt

fig_dir = local / "figures"
paths = sorted(fig_dir.glob("*.png"))
print([path.name for path in paths])
fig, axes = plt.subplots(2, 2, figsize=(11, 7))
for ax, path in zip(axes.ravel(), paths):
    ax.imshow(plt.imread(path))
    ax.axis("off")
    ax.set_title(path.stem)
plt.tight_layout()
plt.show()""",
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
