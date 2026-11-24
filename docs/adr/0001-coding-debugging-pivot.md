# ADR 0001: Mengganti artefak matematika dengan tugas debugging pemrograman

- Status: diterima 2026-11-23
- Konteks: Kelompok 9 bertugas menganalisis SocioMathLLM. Aturan brief memperbolehkan analisis "tidak harus sama, tapi serupa". Anggota kelompok mengusulkan soal pemrograman dengan aspek sosialisasi berupa debugging bersama.

## Keputusan
Artefak yang dihasilkan framework adalah tugas debugging program, bukan mathematical word problem. Kesamaan dengan Topik 1 dipertahankan pada level kerangka: tiga modul prompt, empat kompetensi sosial, tanpa fine-tuning, serta evaluasi rubrik dan LLM-as-judge.

## Alternatif yang dipertimbangkan
1. Replikasi SocioMathLLM dengan data publik lain.
2. Perluasan domain ke soal grafik/tabel MathVista, tetap menghasilkan word problem.
3. MWP dengan solusi cacat dari MathDial atau StepVerify, lalu cue debug bersama.
4. Pivot penuh ke kode (dipilih).

## Alasan
Pilihan 1 dan 2 paling aman secara akademik tetapi tidak menjawab usulan anggota. Pilihan 3 tetap menghasilkan word problem dan paling aman terhadap aturan topik, tetapi tidak menghasilkan kode. User secara eksplisit menerima risiko pilihan 4 dengan penjelasan bahwa komponen kecil boleh diganti selama komponen besarnya mirip.

## Konsekuensi
- Risiko nyata: pembaca dapat menilai ini sebagai topik berbeda. Mitigasi: bagian pendahuluan dan related work menyatakan secara eksplisit kesamaan level kerangka dan perbedaan level artefak.
- Seluruh rantai evaluasi harus didesain ulang. BLEU dan BERT tidak lagi menjadi metrik utama.
- Tidak ada dataset publik yang menggabungkan kode buggy, dialog debugging antar orang, dan label sosial. Aspek sosial diwujudkan sebagai petunjuk pada prompt dan dinyatakan sebagai limitasi.
