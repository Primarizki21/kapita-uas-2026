# kapita-uas-2026

Repositori UAS Kapita Selekta Sains Data Gasal 2026/2027, kelompok 9, topik 1. EXP-001 mereplikasi pendekatan SocioMathLLM untuk menghasilkan collaborative debugging tasks dari dataset ITSP: tiga modul prompt, judge empat kompetensi sosial, dan jejak audit tiap run. Angka makalah harus bisa ditelusur sampai artifact di `experiments/EXP-001/`.

## Requirements

- Python 3.13 atau lebih baru
- [uv](https://docs.astral.sh/uv/) sebagai pengelola dependency
- `gcc` untuk mengompilasi kode C
- Koneksi internet untuk mengunduh ITSP dan memanggil gateway OpenCode
- `OPENCODE_API_KEY` hanya untuk full run

Pasang uv bila belum ada:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Setup dan run

```bash
# 1. Unduh arsip ITSP yang dipakai config.
mkdir -p data/raw
curl -L "https://codeload.github.com/jyi/ITSP/tar.gz/0553f683f99403efb5ef440af826c1d229a52376" \
  -o data/raw/ITSP-0553f683f99403efb5ef440af826c1d229a52376.tar.gz
sha256sum data/raw/ITSP-0553f683f99403efb5ef440af826c1d229a52376.tar.gz
# Hash harus: 7d2329ca5cd1009ee0c7518095a13b18fb82a6931750ece27014a83f5d13dec0

# 2. Pasang dependency.
uv sync --frozen

# 3. Siapkan kunci untuk full run. Berkas .env tidak masuk git.
cp .env.example .env
# Edit .env dan isi OPENCODE_API_KEY=<kunci-anda>

# 4. Jalankan prepare-only dulu, lalu full run.
uv run python src/exp001.py --prepare-only
uv run python src/exp001.py

# 5. Bangun plot.
uv run python src/exp001_report.py
```

`--prepare-only` menimpa `metrics.json` dengan `generation: null`, jadi jalankan sebelum full run. Karena temperature judge 0,7, angka judge dapat berubah pada run berikutnya. Selalu sebutkan `run_id` saat memakai angka di makalah.

## Artifact

- Commit: `experiments/EXP-001/{config.yaml,metrics.json,events.jsonl,provenance.json,data-manifest.json}`, `experiments/LEDGER.md`, dan plot notebook.
- Lokal, diabaikan git: `data/raw/`, `data/processed/`, dan `experiments/outputs/EXP-001/` berisi `run.log`, `errors.log`, prompt/response mentah, serta `figures/`.

## Test dan notebook

```bash
uv run python -m unittest discover -s tests

uv sync --extra notebook
uv run python scripts/build_walkthrough_notebook.py
# Buka notebooks/EXP-001-walkthrough.ipynb, lalu Restart and Run All
```

`src/experiment_trace.py` adalah core trace reusable. `scripts/build_walkthrough_notebook.py` membangun notebook dari snippet kode dan artifact yang sudah ada.
