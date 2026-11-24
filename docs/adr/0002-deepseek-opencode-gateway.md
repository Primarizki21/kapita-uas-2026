# ADR 0002: DeepSeek V4.1 Flash melalui gateway OpenCode

- Status: diterima 2026-11-23
- Konteks: SocioMathLLM memakai GPT-4o API. Tidak ada kredensial OpenAI di environment. GPU RTX 5050 8 GB tersedia tetapi `torch` belum terpasang dan model multimodal lokal berisiko kehabisan memori.

## Keputusan
Framework dijalankan dengan model `deepseek-v4.1-flash` melalui endpoint OpenAI-compatible OpenCode. Base URL dan model ID disimpan di `config.yaml` agar jalur Go dan Console dapat dipakai tanpa mengubah kode. Kunci dibaca dari environment `OPENCODE_API_KEY`.

## Alternatif yang dipertimbangkan
1. GPT-4o API: paling mirip paper asli, tetapi tidak tersedia.
2. Qwen2.5-VL lokal: tanpa kredensial, tetapi butuh GPU dan berisiko pada 8 GB.
3. Endpoint DeepSeek resmi: dokumen jelas dan mendukung vision, tetapi user memilih gateway opencode.

## Alasan
User menyediakan kunci khusus dari OpenCode. Penggantian model sekaligus menjawab limitasi yang diakui penulis SocioMathLLM, yaitu belum ada validasi lintas-model.

## Konsekuensi
- Syntax bergantung pada kredensial eksternal; syntax tanpa kunci hanya bisa menjalankan tahap persiapan dan pemeriksaan data.
- Versi checkpoint yang disajikan melalui gateway perlu dicatat saat eksekusi. Jika tidak tersedia, paper menyebut nama model sesuai konfigurasi, bukan tanggal checkpoint.
- Traffic gateway dipantau untuk pola coding-agent; kode harus mengirim user agent dan session ID yang stabil sesuai dokumentasi OpenCode.
- Rujukan: `https://opencode.ai/docs/console/models/`, `https://opencode.ai/docs/go/`.

## Catatan eksekusi 2026-11-24

Endpoint Console menolak panggilan dengan HTTP 402 karena saldo pay-as-you-go tidak cukup. Endpoint Go `https://opencode.ai/inference/go/v1` menerima kunci yang sama untuk model `deepseek-v4.1-flash`; konfigurasi dipindahkan ke jalur Go. Model tidak diganti, dan tidak ada model lain yang dipanggil.

## Catatan mode berpikir 2026-11-24

Panggilan pertama menghasilkan `content` kosong karena seluruh batas token terpakai untuk `reasoning_content`. Konfigurasi menetapkan `thinking: disabled`; dokumentasi DeepSeek menyebut mode berpikir aktif secara default dan menyediakan toggle tersebut. Ini bukan penggantian model.
