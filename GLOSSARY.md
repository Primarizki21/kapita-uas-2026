# GLOSSARY

Istilah di bawah dipakai untuk naskah dan syntax. Definisi ini sengaja bebas dari detail implementasi.

## Authentic debugging context
Bahan kontekstual yang berasal dari artifact pemrograman nyata: pernyataan tugas, kode yang mengandung cacat, dan perilaku saat dijalankan. Padanan fungsional dari *authentic context* pada SocioMathLLM.

## Collaborative debugging task
Tugas pemrograman yang meminta dua atau lebih pelajar menemukan dan memperbaiki defect bersama, disertai petunjuk interaksi. Ini adalah artefak yang dihasilkan framework kami.

## Debugging competency
Salah satu dari empat perilaku sosial yang menjadi target prompt: lokalisasi cacat bersama, pembagian peran saat memperbaiki, negosiasi mengenai penyebab dan perbaikan, serta pertukaran dan justifikasi ide. Keempatnya adalah padanan fungsional dari empat kompetensi sosialisasi SocioMathLLM.

## Pair profile
Ringkasan latar belakang dua pelajar yang dipakai untuk menyesuaikan tugas. Isinya mencakup pengalaman pemrograman dan preferensi peran, bukan kemampuan matematika.

## Prompt pipeline
Tiga tahap berurutan: pembangkitan kandidate dari konteks, seleksi satu kandidate dengan penalaran berdasarkan kriteria dan profil, lalu pengubahan kandidate menjadi tugas kolaboratif.

## LLM-as-judge
Penggunaan model bahasa untuk menilai keluaran berdasarkan rubrik yang sama dengan yang dipakai penilai manusia. Bukan pengganti penilaian manusia, melainkan pembanding.

## Cross-model validation
Pengujian kembali suatu framework dengan model yang berbeda dari model pada studi aslinya. Studi ini menggantikan GPT-4o dengan DeepSeek V4.1 Flash.

## Public benchmark
Kumpulan data dengan sumber, lisensi, dan versi yang dapat dicek pihak lain. Tidak mencakup data yang dibuat khusus oleh kelompok untuk penelitian ini.

## Fail-to-pass
Sifat dari kasus debugging yang sah: kode buggy gagal pada test tertentu sedangkan kode rujukan lulus. Dipakai sebagai pemeriksaan validitas butir, bukan sebagai metrik kualitas generasi.
