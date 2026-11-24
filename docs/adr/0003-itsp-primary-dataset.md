# ADR 0003: ITSP sebagai dataset utama

- Status: diterima 2026-11-23
- Konteks: studi membutuhkan data publik yang menyediakan pernyataan tugas pemrograman, kode buggy, kode rujukan, dan sarana pengecekan.

## Keputusan
ITSP dipakai sebagai sumber utama. Versi dipatok pada commit `0553f683f99403efb5ef440af826c1d229a52376`. DebugBench dipakai hanya sebagai pembanding deskriptif. Fallback MathVista tetap tercatat tetapi tidak aktif.

## Alternatif yang dipertimbangkan
1. DebugBench: 4.253 kasus dan label kesulitan, tetapi bug disuntikkan sintetis dan hidden test tidak terbundle.
2. IntroClass: defect autentik dan test tersedia, tetapi pernyataan hanya enam deskripsi one-line dan tidak ada label kesulitan.
3. CodeContests: skema paling lengkap, tetapi wrong submission tidak kurasi dan dapat gagal kompilasi.

## Alasan
ITSP adalah satu-satunya paket ringkas berlisensi MIT yang menyatukan pernyataan soal lengkap, pasangan kode buggy dan benar dari mahasiswa yang sama, serta file test. Ini paling mendukung klaim autentisitas sekaligus pemeriksaan fail-to-pass tanpa GPU atau unduhan besar.

## Konsekuensi
- Kesulitan hanya tersedia sebagai proxy berupa id praktikum; ini harus dinyatakan sebagai keterbatasan.
- Kode berbahasa C, sehingga kompilasi memakai `gcc`.
- Hash publik tidak tersedia; hash dihitung lokal dari arsip pada commit yang dipatok dan ditulis ke manifest.
