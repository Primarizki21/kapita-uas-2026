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
