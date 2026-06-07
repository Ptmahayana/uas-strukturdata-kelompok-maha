@echo off
title DSS Pemilihan Supplier Berbasis Graph
color 0A

echo ===============================================
echo    DSS PEMILIHAN SUPPLIER BERBASIS GRAPH
 echo ===============================================
 echo.
 echo Memulai aplikasi...
 echo.
 echo Jika browser tidak terbuka otomatis, buka:
 echo http://localhost:8501
 echo.
 echo Tekan Ctrl+C untuk menghentikan aplikasi
 echo ===============================================
 echo.

cd /d C:\Users\Pongo\Desktop\DSS
python -m streamlit run app.py

pause