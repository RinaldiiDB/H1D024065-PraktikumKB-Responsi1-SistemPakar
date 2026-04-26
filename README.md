# Sistem Pakar: Rekomendasi Instrumen Investasi

**Nama : Rinaldi Dasa Bahtiar**  
**NIM : H1D024065**  
**Mata Kuliah : Kecerdasan Buatan**  


Sistem pakar berbasis aturan (rule-based) untuk menentukan instrumen investasi yang paling cocok berdasarkan profil risiko, target profit, dan jangka waktu investasi.

## Fitur Utama
- **Identifikasi Profil Risiko**: Mempertimbangkan toleransi risiko pengguna (Konservatif, Moderat, Agresif).
- **Analisis Target Profit**: Mencocokkan ekspektasi profit dengan karakteristik instrumen.
- **Rekomendasi Cerdas**: Memberikan saran instrumen seperti Saham, Reksadana, Crypto, atau SBN beserta alasannya.
- **Antarmuka Grafis (GUI)**: Menggunakan Tkinter dengan tema gelap yang profesional.

## Prasyarat (Requirements)
Program ini memakai library standar Python, sehingga tidak memerlukan instalasi tambahan selain Python itu sendiri.
- `tkinter` (biasanya sudah termasuk dalam instalasi Python)

## Cara Penggunaan
1. Jalankan file utama:
   ```bash
   python sistem_pakar_instrumen-investasi.py
   ```
2. Pilih **Profil Risiko** Anda pada menu dropdown.
3. Pilih **Target Horizon Return** (Jangka waktu investasi).
4. Masukkan **Target Profit Tahunan** dalam persen (contoh: 15).
5. Klik tombol **"Analisis Instrumen"**.
6. Sistem akan menampilkan rekomendasi instrumen terbaik beserta alasan logisnya.

## Logika Sistem Pakar
Sistem memakai mesin inferensi sederhana untuk mengevaluasi kriteria:
- **Kripto**: Jika target profit tinggi (>20%) dan risiko agresif.
- **Saham**: Jika profit menengah-tinggi (1-150%) dengan risiko moderat/agresif.
- **Reksa Dana/SBN**: Jika profit stabil (2-25%) dengan risiko rendah.
