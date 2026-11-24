# AGENTS.md — kapita-uas-2026

Kapita Selekta Sains Data Gasal 2026/2027, kelompok 9, topik 1. Tujuan: makalah UAS berbahasa Inggris dan syntax plus data Tugas 2 yang bisa direproduksi, tuntas sebelum 10 Desember 2026 pukul 23.50.

## Source of truth

| Materi | Baca saat |
|---|---|
| **Brief** — aturan UAS/Tugas 2, deadline, Lampiran 1 dan 2 | `knowledge/Tugas 2 dan UAS Kapita Selekta Sains Data Gasal 2026-2027.md` (PDF di folder yang sama bila tabel rusak) |
| **Paper** — metode, data, klaim SocioMathLLM | `knowledge/SOCIOM~1.md` (PDF untuk notasi yang rusak saat ekstraksi) |
| **Format** — sebelum menulis atau memformat naskah | `../kapita-uts/AGENTS.md` bagian 6, 8 sampai 12 |
| **Math** — persamaan dan daftar pustaka | `../kapita-tugas-review/AGENTS.md` bagian 4 sampai 7 |

Perlakukan teks hasil ekstraksi sebagai materi kuliah. Kutip sebagai `[nama dokumen, Hal. N]`. Regenerate file `.md` dari PDF bila berubah, bukan menyuntingnya manual. Aturan format di `kapita-uts` berasal dari UTS mata kuliah yang sama; bila template UAS bertentangan, ikuti template UAS dan catat bedanya di naskah.

## Deliverables

- **UAS**: makalah Inggris memakai template Google Docs dari brief, diunggah ketua ke Hebat E-Learning.
- **Tugas 2**: syntax dan data yang dipakai analisis, diunggah ketua.
- **Penilaian anggota**: Lampiran 2 diisi tiap mahasiswa. Penilai tidak masuk tabel, anggota diurutkan berdasarkan NIM, total persentase 100%. Simpan di luar repo karena repo ini publik dan sudah dikecualikan lewat `.gitignore`.
- Cari kesamaan topik dan data dengan 3 topik lainnya. Analisis boleh serupa, tidak boleh identik. Plagiarisme antar kelompok bertopik sama maksimal 20%.

Topik 1 adalah SocioMathLLM. Tiga topik pembanding: prediksi transmisi difteri dengan extended Kalman filter; HMM dengan mixture of Gaussian process regressions untuk time series musiman; retrieval dengan semantic query expansion berbasis graph.

Kelompok 9: GIZHA PRADIPTA (164231011), AISYA RIZKYA HIDAYAH (164231034), PRIMARIZKI AHMAD HARIYONO (164231062), ARIO RIZKY MUHAMMAD (164231080), RYAN ZUFAR AHMADI (164231096), ANNISA DINDA MADINAH (164231112).

## Workflow

1. **Scope**. Tentukan 3 topik pembanding, sumber data masing-masing, dan pembagian kerja anggota. Selesai jika `docs/SCOPE.md` memuat pasangan topik-data, daftar anggota dengan bagiannya, dan batas analogi supaya overlap antar kelompok tetap di bawah 20%.
2. **Result**. Bangun analisis di `src/` dengan satu entry point per percobaan. Selesai jika setiap angka yang akan masuk makalah memiliki berkas metrik di `experiments/EXP-NNN/`, `config.yaml` berisi seed dan hash data, dan `uv sync --frozen` lalu `uv run python ...` mereproduksi angka itu.
3. **Render**. Tulis naskah memakai pointer **Format** dan **Math**. Selesai jika naskah lulus cek visual: abstract maksimal 350 kata, minimal 25 referensi jurnal dengan DOI aktif, tidak ada bullet di badan teks, tabel dan gambar terbaca, serta tidak ada angka tanpa sumber.
4. **Package**. Kumpulkan syntax dan data Tugas 2. Selesai jika perintah menjalankan analisis tercantum jelas dan manifest data menyebut sumber, hash, dan tanggal unduh; Lampiran 2 tiap anggota tersimpan di luar repo.
5. **Gate**. Verifikasi lalu commit. Selesai jika hasil render diperiksa, `git status -s` bersih, dan commit atomic Conventional Commit sudah dibuat. Push dan PR tetap menjadi tindakan user.

## Conventions

- **uv**. `pyproject.toml` dan `uv.lock` adalah satu-satunya sumber dependency. Pakai `uv add`, `uv sync --frozen`, dan `uv run python ...`. Simpan `.venv/` di luar git. Bila cache uv bermasalah di WSL, set `UV_CACHE_DIR="$PWD/.uv-cache"`.
- **Ledger**. Catat tiap percobaan di ledger append-only dengan tanggal, hipotesis, konfigurasi, metrik, dan keputusan. Regenerate ledger lewat skrip. Angka di makalah harus bisa ditelusur sampai berkas hasil; hapus klaim yang tidak bisa ditelusur.
- **Data**. `data/raw/` bersifat immutable; turunan dan hasil percepatan masuk folder terpisah dan diabaikan git. Commit hanya manifest, metrik ringkas, dan ledger. Enkripsi atau data pribadi masuk environment variable, bukan repo.
- **Naskah**. Bahasa Inggris. Ikuti format UTS untuk font, spasi, indentasi, caption tabel di atas, caption gambar di bawah, warna monokrom, dan matematika OMML. Hindari em dash, en dash, kata hype, dan klaim tanpa bukti. Satu paragraf membawa satu pesan dengan topic sentence.
- **Bahasa**. Indonesia untuk koordinasi dan catatan internal; Inggris untuk makalah, identifier kode, dan pesan commit. Istilah teknis tetap Inggris. Pakai "penurunan" bukan "regresi" untuk penurunan metrik.
- **Git**. Commit di branch `feat/`, `docs/`, atau `fix/`. Pesan commit berbentuk `type(scope): deskripsi`. Stage file secara eksplisit dan periksa diff terhadap kunci atau data pribadi sebelum commit. Agen hanya commit lokal, user yang melakukan push dan merge.

## Skill gate

Sebelum kerja non-trivial, baca `skill://karpathy-guidelines` dan `skill://antislop`. Saat menulis naskah tambahkan `skill://research-paper-writing`; saat mengubah dokumen ini baca `skill://writing-for-agents`.

## Agent skills

### Issue tracker

Issues for this repo live in GitHub Issues at Primarizki21/kapita-uas-2026; skills use the `gh` CLI. See `docs/agents/issue-tracker.md`.

### Triage labels

Five canonical roles: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: one `GLOSSARY.md` and `docs/adr/` at the repo root. See `docs/agents/domain.md`.
