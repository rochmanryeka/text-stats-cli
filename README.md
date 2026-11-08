# Text Stats CLI

Alat command-line sederhana untuk menghitung kata, karakter, dan baris teks.
Dibangun dengan Python standard library, tanpa dependensi tambahan.

## Persyaratan

Python 3.10 atau lebih baru. Tidak perlu `pip install`.

## Penggunaan

```bash
python text_stats.py "Halo dunia"
```

Hasil:

```json
{"words": 2, "characters": 10, "lines": 1}
```

- Kata dipisahkan oleh whitespace.
- Karakter dihitung sebagai Unicode code point, termasuk whitespace.
- Baris dihitung menggunakan `str.splitlines()`; teks kosong memiliki nol baris.

## Pengujian

```bash
python -m unittest discover -s tests -v
```

Tes juga berjalan melalui GitHub Actions untuk setiap pull request dan push ke `main`.
