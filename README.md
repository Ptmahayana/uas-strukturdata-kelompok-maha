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
