# PAPER-PLAN: outline makalah UAS

Status: usulan, 2026-11-27. Naskah akhir berbahasa Inggris memakai template Google Docs dari brief (`knowledge/Tugas 2 dan UAS Kapita Selekta Sains Data Gasal 2026-2027.md` baris 26-29). Berkas ini catatan internal bahasa Indonesia. Turunan dari `docs/SCOPE.md`; batas klaim lengkap ada di bagian 8 dokumen itu dan tidak diulang di sini.

## Cerita makalah

SocioMathLLM memakai urutan prompt contextualization, personalization, dan socialization untuk menghasilkan soal cerita geometri yang mengajak siswa berinteraksi. Pertanyaan kami: apakah urutan yang sama tetap berguna bila artefaknya bukan soal cerita, melainkan program C yang salah? Jawabannya: strukturnya dapat dipakai ulang, tetapi cara mengukurnya harus diganti. Dengan 20 butir dari ITSP kami menjalankan tiga modul prompt ditambah satu judge, lalu mengukur keberhasilan kompilasi, perilaku test, dan empat skor kompetensi sosial. Hasilnya bersifat pilot dan tidak membuktikan perubahan perilaku mahasiswa.

## Batas klaim untuk Abstract dan Introduction

| Klaim | Status | Dasar |
|---|---|---|
| Kami mengadaptasi struktur prompt tiga modul SocioMathLLM ke tugas debugging C. | Didukung | `docs/SCOPE.md` bagian 1-2; `src/exp001.py` baris 275-337 |
| Keluaran memuat delapan cue dari empat kompetensi sosial, bukan perilaku sosial yang teramati. | Didukung | `src/exp001.py` baris 296-305; `experiments/EXP-001/metrics.json` |
| Tugas meningkatkan kolaborasi mahasiswa. | Dilarang | tidak ada uji dengan mahasiswa, `docs/SCOPE.md` bagian 8.1 |
| Pipeline lebih baik daripada zero-shot. | Dilarang | tidak ada kondisi zero-shot, `docs/SCOPE.md` bagian 8.1 |
| Skor judge sama dengan perilaku sosial aktual. | Dilarang | judge menilai teks tugas, `docs/SCOPE.md` bagian 8.1 |
| Evaluasi lengkap tiga sumber seperti paper. | Dilarang | tidak ada panel manusia, `docs/SCOPE.md` bagian 8.1 |

Kalimat aman untuk hasil: "The judged task texts received mean scores of 4.15, 4.00, 3.55, and 4.20 on the four social-competence cues." Kalimat yang tidak aman: "The tasks improved student collaboration."

## Peta bagian

### Judul sementara

Adapting the SocioMathLLM Prompt Framework to Generate Collaborative Debugging Tasks from Student C Programs

### Abstract, target 250-300 kata

- Pesan utama: struktur kerangka dapat dipindah ke artefak baru, tetapi metrik harus mengikuti artefak itu.
- Claim: adaptasi tiga modul berhasil dijalankan pada 20 butir ITSP. Evidence: `experiments/EXP-001/metrics.json`, `run_id` `EXP-001-20261124T035513458240Z-f8283ecc`.
- Claim: 14 dari 20 butir lolos fail-to-pass, skor judge terbaca untuk 20 dari 20 butir. Evidence: berkas metrik yang sama.
- Batas: sebut pilot, sebut tidak ada uji mahasiswa. Jangan sebut peningkatan atau perbandingan langsung dengan paper.

### 1. Introduction

- Claim: paper asli menghasilkan soal matematika, sedangkan praktik pemrograman pemula memakai tugas debugging; keduanya sama-sama memerlukan interaksi teman sebaya.
- Evidence: `knowledge/SOCIOM~1.md` hal. 274-276 untuk tiga modul; `docs/SCOPE.md` bagian 1 untuk alasan pivot.
- Urutan paragraf: premis paper, celah artefak, apa yang kami lakukan, apa yang tidak kami klaim.

### 2. Related Work

- Claim: tidak ada dataset publik yang menggabungkan kode buggy, dialog debugging sungguhan, dan label sosial pada skala yang dipakai.
- Evidence: `docs/SCOPE.md` bagian 3; `docs/research/collab-debugging-datasets.md`.
- Bedakan dari paper: GPT-4o dan geometri versus DeepSeek dan kode C; paper membandingkan dengan zero-shot, kami tidak.
- Hubungkan ke tiga topik lain sesuai brief baris 16-25 dan `docs/SCOPE.md` bagian 5, pada level kerangka saja.

### 3. Method

- Claim: pipeline memakai prompt engineering tanpa fine-tuning, satu model, dan tiga modul berurutan ditambah judge.
- Evidence: `src/exp001.py` baris 275-337; `experiments/EXP-001/config.yaml` (`temperature: 0.7`, model `deepseek-v4.1-flash`).
- Claim: 20 butir dipilih secara deterministik dari 661 butir dengan seed `20261123`, arsip ITSP commit `0553f683...` dan hash terverifikasi.
- Evidence: `experiments/EXP-001/config.yaml`; `experiments/EXP-001/data-manifest.json` (tanggal unduh 2026-11-23).
- Claim: validitas butir diperiksa dengan kompilasi `gcc` dan test tertanam sebelum generasi.
- Evidence: `src/exp001.py` baris 138-170.
- Jelaskan pemetaan tiga modul: soal asli plus kode buggy menjadi lima kandidat, profil pasangan memilih satu, empat cue menulis ulang menjadi tugas akhir.

### 4. Results

- Claim: angka eksekusi dan rubrik dari satu `run_id` tertentu.
- Evidence: `experiments/EXP-001/metrics.json`: 17 dari 20 kode buggy terkompilasi, 16 dari 20 kode benar terkompilasi, 14 dari 20 fail-to-pass (0,70), judge terbaca 20 dari 20, rata-rata collaboration 4,15, cooperation 4,00, negotiation 3,55, ideas sharing 4,20.
- Sertakan `attempt: 3` dan config hash `f8283ecc...` agar angka tidak tercampur dengan run lain.
- Nyatakan bahwa angka judge dapat berubah karena temperature 0,7.

### 5. Discussion

- Claim: yang berpindah adalah arsitektur prompt dan tujuan pedagogis; yang tidak berpindah adalah ukuran kualitas.
- Evidence: `docs/SCOPE.md` bagian 2 dan 8.1.
- Jelaskan mengapa BLEU, METEOR, ROUGE-L, BLEURT, dan BERT tidak dipakai: tidak ada teks referensi buatan manusia.
- Jangan membandingkan angka kami dengan angka paper secara numerik; keduanya mengukur hal berbeda.

### 6. Limitations

- Satu paragraf per pembatas, masing-masing dengan penunjuk: 20 dari 661 butir; kesulitan hanya proxy id praktikum; profil pasangan hipotetis; tanpa panel manusia dan ICC; satu model lewat satu gateway; tanpa audit kebocoran solusi; batas tumpang tindih 20% belum diukur.
- Evidence: `docs/SCOPE.md` bagian 8.1 sampai 8.4.

### 7. Conclusion

- Claim: kerangka tiga modul dapat dipakai untuk artefak debugging, tetapi klaimnya berhenti pada kualitas teks tugas dan kelayakan eksekusi, bukan hasil belajar.
- Evidence: gabungan bagian Results dan Limitations.

## Tabel dan gambar

| Item | Isi | Sumber dan tindakan |
|---|---|---|
| Tabel 1 | Perbandingan SocioMathLLM dan studi ini | `docs/SCOPE.md` bagian 2. Caption di atas, tiga garis horizontal, tanpa garis vertikal. |
| Tabel 2 | Hasil EXP-001 | `experiments/EXP-001/metrics.json`. Sertakan `run_id` di caption atau narasi. |
| Gambar 1 | Diagram alur tiga modul ditambah judge | Buat baru, monokrom, dari `src/exp001.py` baris 275-337. Caption di bawah. |
| Gambar 2 | Rata-rata skor judge per dimensi | `src/exp001_report.py` menghasilkan `judge_scores.png` di folder yang diabaikan git. Regenerate lalu salin ke path yang ter-commit. |
| Gambar 3 | Tingkat lulus test per butir | Sumber sama, berkas `pass_rate_per_item.png`. Perlakuan sama seperti Gambar 2. |

Cek warna: plot bawaan matplotlib mungkin berwarna. Sesuaikan ke skala abu-abu sebelum dimasukkan ke naskah, sesuai aturan monokrom di `../kapita-tugas-review/AGENTS.md` bagian 5.

## Referensi

- Minimal 25 artikel jurnal dengan DOI aktif, format APA 6.0, sesuai pointer Format bagian 8.
- Sumber utama: SocioMathLLM DOI `10.1109/TLT.2026.3677266`; ITSP; DebugBench DOI `10.18653/v1/2024.findings-acl.247`.
- Seleksi 25 jurnal ber-DOI aktif sudah tercatat di `docs/REFERENCES.md`, diambil dari `docs/research/reference-pool.md` dengan status DOI dicek 2026-11-23.
- Validasi DOI aktif kembali sebelum submission. Jangan memasukkan entri tanpa DOI hanya untuk mencapai 25.

## Urutan kerja

1. Setujui outline ini, lalu tulis draf Abstract, Introduction, Method, dan Results dalam bahasa Inggris memakai peta klaim di atas.
2. Buat Tabel 1 dan 2, ditambah Gambar 1 sampai 3, lalu cek keterbacaan dan warna.
3. Lengkapi daftar pustaka sampai 25 jurnal ber-DOI aktif.
4. Periksa format akhir: abstract maksimal 350 kata, tanpa bullet di badan teks, caption tabel di atas dan gambar di bawah, setiap angka bisa ditelusur ke artifact.
5. Notebook menyusul setelah naskah berjalan. Rapikan narasi lewat `scripts/build_walkthrough_notebook.py` bagian `INTRO` dan `PAIRS`, bukan dengan menyunting `notebooks/walkthrough.ipynb` langsung.
6. Package syntax dan data Tugas 2, lalu gate commit. Push dan PR tetap menjadi tindakan user.
