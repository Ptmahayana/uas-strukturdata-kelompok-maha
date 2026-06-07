# 📦 DSS Pemilihan Supplier Berbasis Graph

## 📋 Deskripsi Proyek

Aplikasi Decision Support System (DSS) untuk membantu perusahaan memilih supplier terbaik berdasarkan 4 kriteria:
- **Harga** (semakin murah semakin baik)
- **Jarak** (semakin dekat semakin baik)  
- **Kualitas** (semakin tinggi semakin baik)
- **Waktu Kirim** (semakin cepat semakin baik)

Proyek ini menggunakan **Struktur Data Graph** dengan algoritma **Dijkstra** untuk pencarian jalur terpendek dan **Weighted Sum Model (WSM)** untuk perhitungan skor supplier.

---

## 🛠️ Teknologi yang Digunakan

| Teknologi | Fungsi |
|-----------|--------|
| Python 3.x | Bahasa pemrograman utama |
| Streamlit | Framework untuk antarmuka web |
| Pandas | Manipulasi dan analisis data |
| NetworkX + Matplotlib | Visualisasi graph |
| Plotly | Visualisasi interaktif |

---

## 📁 Struktur File
DSS/

├── app.py # Aplikasi utama Streamlit

├── graph_model.py # Class Graph & Algoritma Dijkstra

├── data_supplier.py # Data supplier & fungsi normalisasi

├── requirements.txt # Daftar package yang dibutuhkan

├── run_dss.bat # Shortcut untuk menjalankan aplikasi (Windows)

└── README.md # Dokumentasi proyek


---

## 🚀 Cara Menjalankan Aplikasi

### **Persiapan (Install Package)**

```bash
pip install streamlit pandas plotly networkx matplotlib
```
### **Jika Menggunakan Requirement.txt**
```bash
pip install -r requirements.txt
```
## 🎯 Fitur Aplikasi
### Fitur	Keterangan

✅ Tabel Data Supplier	Menampilkan 5 supplier dengan 4 kriteria

✅ Atur Bobot Kriteria	User bisa mengatur bobot via sidebar

✅ Perhitungan Skor Otomatis	Skor berubah real-time saat bobot diubah

✅ Rekomendasi Supplier Terbaik	Menampilkan supplier dengan skor tertinggi

✅ Visualisasi Graph	Menampilkan jalur Pabrik → Supplier

✅ Pencarian Jalur Terpendek	Algoritma Dijkstra untuk mencari rute optimal

## 📊 Data Supplier

## 📊 Data Supplier

Berikut adalah data 5 supplier yang digunakan dalam sistem:

| Supplier | Harga (Rp) | Jarak (km) | Kualitas (0-100) | Waktu Kirim (hari) |
|----------|------------|------------|------------------|-------------------|
| Supplier A | 85.000 | 10 | 90 | 3 |
| Supplier B | 70.000 | 25 | 75 | 5 |
| Supplier C | 90.000 | 15 | 95 | 2 |
| Supplier D | 60.000 | 40 | 65 | 7 |
| Supplier E | 80.000 | 20 | 85 | 4 |

### Keterangan Kriteria

| Kriteria | Jenis | Keterangan |
|----------|-------|-------------|
| Harga | Cost ↓ | Semakin kecil nilai, semakin baik |
| Jarak | Cost ↓ | Semakin kecil nilai, semakin baik |
| Kualitas | Benefit ↑ | Semakin besar nilai, semakin baik |
| Waktu Kirim | Cost ↓ | Semakin kecil nilai, semakin baik |

## 🧮 Metode Perhitungan
Normalisasi Min-Max
Kriteria Cost (Harga, Jarak, Waktu Kirim):

```text
Normalized = (Max - Value) / (Max - Min)
Kriteria Benefit (Kualitas):
```
```text
Normalized = (Value - Min) / (Max - Min)
Weighted Sum Model (WSM)
text
Total Score = Σ (Bobot_i × Normalized_i)
```
## 🔍 Algoritma Dijkstra
Digunakan untuk mencari jalur terpendek dari Pabrik Pusat ke supplier yang dipilih.

Kompleksitas Waktu: O((V + E) log V)

Kompleksitas Ruang: O(V)

## 📸 Screenshot Aplikasi
(Tambahkan screenshot hasil running aplikasi di sini)
