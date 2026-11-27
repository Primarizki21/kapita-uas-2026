# SCOPE — UAS dan Tugas 2 Kelompok 9

Status: disetujui 2026-11-23. Deadline: 10 Desember 2026 pukul 23.50.

## 1. Keputusan final

Makalah berbahasa Inggris dengan topik **LLM framework untuk menghasilkan tugas debugging pemrograman yang mendorong kolaborasi**. Ini adalah perluasan dari Topik 1 (SocioMathLLM), bukan salinan.

Kesamaan dinilai pada level kerangka besar, sesuai interpretasi user: komponen kecil boleh diganti selama komponen besar tetap mirip. Komponen besar yang dipertahankan:

1. pipeline prompt tiga modul;
2. tujuan pedagogis mendorong interaksi sosial saat menyelesaikan masalah;
3. pendekatan prompt engineering tanpa fine-tuning;
4. evaluasi triangulasi: metrik otomatis, penilaian berbasis rubrik, dan LLM-as-judge;
5. komponen sosial empat kompetensi yang diimplementasikan ulang sebagai perilaku debugging bersama.

Risiko yang sudah disampaikan dan diterima: mengganti artefak dari *math word problem* menjadi kode dapat dibaca sebagai topik berbeda. Mitigasinya adalah menuliskan secara eksplisit di makalah bahwa struktur kerangka, bukan artefak, yang menjadi dasar kesamaan.

## 2. Sumber dan batas analogi

| Aspek | SocioMathLLM (Hwang & Utami, 2026) | Studi kita | Alasan pembeda |
|---|---|---|---|
| Artefak | mathematical word problem 2-D geometry | tugas debugging program C dari ITSP | menghindari replikasi langsung |
| Konteks | foto benda nyata + diagram | pernyataan soal asli + kode buggy + jawaban benar | kontekstualisasi tetap berbasis artifact autentik |
| Personalisasi | profil siswa matematika | profil pasangan pemrograman | konsep "profil grup" dipertahankan, isinya diganti |
| Sosialisasi | collaboration, cooperation, negotiation, ideas-sharing | versi debugging: lokalisasi bersama, peran driver/navigator, negosiasi root cause, justifikasi perbaikan | empat kompetensi dipertahankan sebagai kerangka |
| Model | GPT-4o via API | DeepSeek V4.1 Flash via gateway OpenCode | validasi lintas-model yang belum ada di paper asli |
| Metrik utama | BLEU, METEOR, ROUGE-L, BLEURT, BERT | kompilasi, perilaku test, dan rubrik LLM | metrik teks tidak mengukur kebenaran kode |

Sumber: `knowledge/SOCIOM~1.md`; brief `knowledge/Tugas 2 dan UAS Kapita Selekta Sains Data Gasal 2026-2027.md` baris 16-32; hasil riset di `docs/research/`.

## 3. Pasangan topik dan data

- TopikUtama: SocioMathLLM, DOI `10.1109/TLT.2026.3677266`.
- DataUtama: ITSP, repo `https://github.com/jyi/ITSP`, commit `0553f683f99403efb5ef440af826c1d229a52376`, lisensi MIT. Berisi 661 program mahasiswa: pernyataan soal lengkap, pasangan kode buggy dan benar, serta file test.
- DataPembanding: DebugBench, DOI `10.18653/v1/2024.findings-acl.247`, lisensi Apache-2.0, 4.253 kasus. Dipakai hanya sebagai pembanding deskriptif, bukan campuran data.
- Fallback (disimpan, tidak dipakai default): MathVista `testmini`, sumber `ChartQA` (50) + `TabMWP` (62) = 112 item, untuk opsi kontekstualisasi bergambar.

Tidak ada dataset publik yang menggabungkan kode buggy, dialog debugging antar orang, dan label sosial pada skala terpakai. Aspek sosial karena itu diwujudkan sebagai cue generatif pada prompt, bukan sebagai data dialog yang diamati. Fakta ini dicatat sebagai limitasi.

## 4. Struktur analisis

1. **Contextualization**: ekstrak pernyataan soal dari `Main.c`, kode buggy, kode benar, dan id praktikum sebagai proxy kesulitan. Hasilnya dipakai untuk membangkitkan lima kandidate tugas debugging.
2. **Personalization**: profil pasangan berisi pengalaman pemrograman, kebiasaan peran driver/navigator, dan riwayat debugging hipotetis. CoT memilih satu kandidate.
3. **Socialization**: empat prompt kompetensi + few-shot cue dialog debugging, menghasilkan tugas akhir yang meminta pasangan mendiskusikan dan memperbaiki bug.

Eksekusi: `gcc` tersedia; kode buggy dan benar dikompilasi sebagai pemeriksaan validitas. Angka metrik ditulis ke `experiments/EXP-001/` beserta salinan config dan hash data.

## 5. Pembagian kerja

| NIM | Nama | Bagian |
|---|---|---|
| 164231011 | GIZHA PRADIPTA | Literature review dan referensi ber-DOI |
| 164231034 | AISYA RIZKYA HIDAYAH | Manifest data, hash, dan preprocessing ITSP |
| 164231062 | PRIMARIZKI AHMAD HARIYONO | Pipeline prompt dan entry point percobaan |
| 164231080 | ARIO RIZKY MUHAMMAD | Metrik evaluasi dan rubrik LLM-as-judge |
| 164231096 | RYAN ZUFAR AHMADI | Naskah metode dan hasil |
| 164231112 | ANNISA DINDA MADINAH | Naskah pendahuluan dan related work, cek format |

## 6. Aturan operasional

- Bahasa Indonesia untuk koordinasi, Inggris untuk makalah, identifier kode, dan pesan commit.
- `data/raw/` tidak diubah. Turunan dan hasil Generasi masuk folder yang diabaikan git.
- Kunci API dibaca dari environment variabel `OPENCODE_API_KEY`; tidak pernah ditulis di repo atau chat.
- Commit hanya manifest, metrik ringkas, ledger, naskah, dan syntax. Push dan PR menjadi tindakan user.
- Penilaian anggota Lampiran 2 disimpan di luar repo.

## 7. Reproduksi untuk Tugas 2

```bash
uv sync --frozen
uv run python src/exp001.py --prepare-only
cp .env.example .env   # isi OPENCODE_API_KEY di .env
uv run python src/exp001.py
```

Skrip memuat `.env` dari root repo otomatis tanpa menimpa variabel yang sudah ada di environment. Alternatif tanpa berkas: `OPENCODE_API_KEY=<kunci-anda> uv run python src/exp001.py`.

Mode `--prepare-only` memverifikasi hash arsip, membangun 20 butir dari 661 butir ITSP dengan seed `20261123`, mengompilasi kode, dan menulis metrik eksekusi tanpa jaringan. Mode penuh menambah tiga modul prompt dan LLM judge melalui gateway OpenCode; kunci tidak boleh ditulis di repo.

Status verifikasi 2026-11-24: full run berhasil dengan run_id `EXP-001-20261124T035513458240Z-f8283ecc`, attempt 3, model `deepseek-v4.1-flash` melalui endpoint Go OpenCode, thinking dinonaktifkan, 20 dari 20 penilaian judge terbaca. Metrik: 17 dari 20 kode buggy dan 16 dari 20 kode benar terkompilasi, 14 butir fail-to-pass (0,70). Rerata skor judge: collaboration 4,15; cooperation 4,00; negotiation 3,55; ideas sharing 4,20. Angka ada di `experiments/EXP-001/metrics.json`, provenance di `experiments/EXP-001/provenance.json`, dan jejak generasi lokal di `experiments/outputs/EXP-001/`. Karena temperature 0,7, angka judge dapat berubah pada run berikutnya; versi makalah harus memakai angka dari run_id ini.

## 8. Batasan yang disetujui

Bagian ini menjaga klaim makalah tetap berada dalam ruang yang bisa dibuktikan. Setiap butir menunjuk ke artifact atau dokumen yang menjadi dasarnya.

### 8.1 Referensi dan metrik

- Tidak ada reference task berupa tugas debugging kolaboratif buatan manusia. Yang tersedia adalah pasangan kode buggy dan benar beserta test di `data/processed/EXP-001/items.jsonl`, bukan teks tujuan generasi. Metrik BLEU, METEOR, ROUGE-L, BLEURT, dan BERT tidak dipakai karena tidak ada pasangan teks referensi untuk dibandingkan. Metrik otomatis paper mengukur kesamaan soal hasil dengan soal referensi, sedangkan metrik kita hanya mengukur keberhasilan eksekusi dan skor rubrik.
- Tidak ada kondisi zero-shot. Percobaan hanya menjalankan satu pipeline terstruktur, sehingga tidak boleh ada klaim peningkatan terhadap baseline. Paper membandingkan metodenya dengan zero-shot (`knowledge/SOCIOM~1.md`, Hal. 276-278).
- Tidak ada panel penilai manusia, tidak ada validasi rubrik oleh instruktur, dan tidak ada ICC. Rubrik empat kompetensi diadaptasi dari paper tanpa kalibrasi serupa. Skor judge berasal dari satu model pada temperature 0,7, sehingga angka terikat pada `run_id` dan dapat berubah pada run berikutnya (`experiments/EXP-001/metrics.json`, `experiments/EXP-001/provenance.json`).
- Judge menilai teks tugas, bukan perilaku pasangan saat debugging dan bukan hasil belajar. Tidak ada uji dengan mahasiswa atau quasi-experiment.

### 8.2 Data dan konstruk

- Hanya 20 dari 661 butir ITSP yang dipakai dengan seed `20261123`. Ini skala pilot, bukan dasar generalisasi statistik (`experiments/EXP-001/config.yaml`).
- Artefaknya adalah program C, bukan mathematical word problem. Kontekstualisasi memakai pernyataan teks, bukan gambar dan diagram seperti modul multimodal paper.
- Profil pasangan bersifat hipotetis. Tidak ada dialog debugging sungguhan maupun label sosial pada data; empat kompetensi diwujudkan sebagai cue pada prompt dan dinyatakan sebagai limitasi sejak ADR 0001.
- Kesulitan hanya proxy berupa id praktikum. Kode rujukan hanya diverifikasi dengan test contoh yang tertanam di butir, tanpa hidden test, sehingga lulus test belum membuktikan kebenaran semantik.
- Dari 20 butir, 17 kode buggy dan 16 kode benar terkompilasi, serta 14 butir memenuhi fail-to-pass. Enam butir tidak lolos kriteria validitas ketat tersebut (`experiments/EXP-001/metrics.json`).

### 8.3 Pipeline dan reproduksi

- Satu model, `deepseek-v4.1-flash`, lewat satu gateway. Tidak ada validasi lintas model dan tidak ada fine-tuning. Paper juga hanya memakai GPT-4o, jadi studi ini tidak menambah bukti generalisasi model.
- Tidak ada audit kebocoran solusi. Prompt meminta agar perbaikan tidak diungkap, tetapi keluaran belum diperiksa secara sistematis terhadap kode benar (`src/exp001.py`).
- Reproduksi penuh membutuhkan `OPENCODE_API_KEY`, jaringan, dan `gcc` 15.2.0. Prompt dan response mentah serta figure berada di folder yang diabaikan git; yang ter-commit hanya ringkasan metrik, events, provenance, dan manifest (`README.md`, `docs/adr/0002-deepseek-opencode-gateway.md`).
- Notebook walkthrough membaca artifact lokal yang diabaikan git. Pipeline dan `src/exp001_report.py` harus dijalankan lebih dulu sebelum notebook di-regenerate.
- Ledger memuat baris ganda dari beberapa `prepare` run dan belum dikurasi. Angka makalah memakai baris run penuh terakhir, bukan seluruh isi ledger.

### 8.4 Risiko penilaian dan kelengkapan

- Penggantian artefak dari mathematical word problem ke kode berisiko dibaca sebagai topik berbeda. Mitigasi ditulis di pendahuluan dan related work, tetapi batas tumpang tindih 20 persen dengan kelompok bertopik sama belum diukur dengan alat (`docs/adr/0001-coding-debugging-pivot.md`, `knowledge/Tugas 2 dan UAS Kapita Selekta Sains Data Gasal 2026-2027.md` baris 30-32).
- Target minimal 25 referensi jurnal ber-DOI belum terpenuhi dari tema sempit saja. Dari 30 karya terverifikasi di `docs/research/coding-framework-fit.md`, 13 di antaranya adalah jurnal atau review. Referensi tambahan harus diambil dari strand riset lain.
