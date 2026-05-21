# PANDUAN SETUP DATABASE & INSTALASI APLIKASI
## Untuk Database localhost dengan nama: `rizkima-python`

---

## 📋 DAFTAR ISI
1. [Persiapan Database](#1-persiapan-database)
2. [Instalasi Library Python](#2-instalasi-library-python)
3. [Konfigurasi Aplikasi](#3-konfigurasi-aplikasi)
4. [Menjalankan Aplikasi](#4-menjalankan-aplikasi)
5. [Troubleshooting](#5-troubleshooting)

---

## 1. PERSIAPAN DATABASE

### 1.1 Pastikan MySQL/MariaDB Terinstal
Periksa versi MySQL:
```bash
mysql --version
```

### 1.2 Buat Database `rizkima-python`

**Metode 1: Via Command Line**
```bash
mysql -u root -p
```

Kemudian ketik SQL:
```sql
CREATE DATABASE `rizkima-python` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
SHOW DATABASES;
USE `rizkima-python`;
```

**Metode 2: Via phpmyadmin**
1. Buka `http://localhost/phpmyadmin`
2. Klik "New" atau "Create new database"
3. Nama: `rizkima-python`
4. Collation: `utf8mb4_unicode_ci`
5. Klik Create

### 1.3 Verifikasi Database
```sql
USE rizkima-python;
SHOW TABLES;
```

---

## 2. INSTALASI LIBRARY PYTHON

### 2.1 Install mysql-connector-python

Buka Command Prompt/Terminal dan jalankan:

```bash
pip install mysql-connector-python
```

### 2.2 Verifikasi Instalasi
```bash
python -c "import mysql.connector; print('✓ mysql-connector berhasil terinstal')"
```

---

## 3. KONFIGURASI APLIKASI

### 3.1 Sesuaikan Kredensial Database

Edit file Python Anda dan ubah bagian koneksi:

**Untuk `sistem_manajemen_karyawan_db.py`:**
```python
sistem = SistemManajemenKaryawan(
    host='localhost',           # Nama host
    user='root',                # Username MySQL (ubah jika berbeda)
    password='',                # Password MySQL (ubah jika ada password)
    database='rizkima-python'   # Nama database
)
```

**Untuk `sistem_pos_inventaris_db.py`:**
```python
sistem = SistemPOS(
    host='localhost',
    user='root',                # Username MySQL
    password='',                # Password MySQL
    database='rizkima-python'
)
```

### 3.2 Contoh Konfigurasi Berbeda

Jika MySQL Anda punya password:
```python
# Username: root
# Password: password123
# Host: localhost

SistemManajemenKaryawan(
    host='localhost',
    user='root',
    password='password123',    # Isi password Anda
    database='rizkima-python'
)
```

Jika MySQL di server lain:
```python
SistemManajemenKaryawan(
    host='192.168.1.100',      # IP server MySQL
    user='admin',
    password='secure_pass',
    database='rizkima-python'
)
```

---

## 4. MENJALANKAN APLIKASI

### 4.1 Menjalankan Aplikasi Manajemen Karyawan

```bash
python sistem_manajemen_karyawan_db.py
```

**Output yang diharapkan:**
```
============================================================
SISTEM MANAJEMEN KARYAWAN - DENGAN DATABASE LOCALHOST
Database: rizkima-python | Host: localhost
============================================================
✓ Koneksi database 'rizkima-python' berhasil!
✓ Tabel karyawan siap digunakan!

------------------------------------------------------------
MENU UTAMA:
------------------------------------------------------------
1. Tambah Karyawan Baru
2. Tampilkan Semua Karyawan
3. Cari Karyawan
4. Lihat Statistik Gaji
5. Update Status Karyawan
6. Hapus Karyawan
7. Keluar
------------------------------------------------------------
Pilih menu (1-7):
```

### 4.2 Menjalankan Aplikasi POS

```bash
python sistem_pos_inventaris_db.py
```

**Output yang diharapkan:**
```
======================================================================
SISTEM INVENTARIS & POS (Point of Sale)
Database: rizkima-python | Host: localhost
======================================================================
✓ Koneksi database 'rizkima-python' berhasil!
✓ Tabel barang dan transaksi siap digunakan!

----------------------------------------------------------------------
MENU UTAMA POS:
----------------------------------------------------------------------
1. Tambah Barang ke Inventaris
2. Lihat Inventaris
3. Transaksi Penjualan
4. Update Stok Barang
5. Laporan Penjualan
6. Laporan Barang Kurang Stok
7. Keluar
----------------------------------------------------------------------
Pilih menu (1-7):
```

### 4.3 Contoh Penggunaan Aplikasi Manajemen Karyawan

```
Pilih menu (1-7): 1

--- TAMBAH KARYAWAN BARU ---
Nama Karyawan: Budi Santoso
Posisi: Teknisi Jaringan
Departemen: IT
Gaji: 3500000
Tanggal Bergabung (YYYY-MM-DD): 2024-01-15
✓ Karyawan 'Budi Santoso' berhasil ditambahkan!

Pilih menu (1-7): 2

--- DAFTAR SEMUA KARYAWAN ---
====================================================================================================
ID    NAMA                 POSISI          DEPARTEMEN      GAJI            TGL BERGABUNG
====================================================================================================
1     Budi Santoso         Teknisi Jaringan IT              3.500.000,00    2024-01-15
====================================================================================================

Pilih menu (1-7): 4

📊 STATISTIK GAJI KARYAWAN
==================================================
Jumlah Karyawan Aktif: 1
Total Gaji Semua: Rp 3.500.000,00
Rata-rata Gaji: Rp 3.500.000,00
==================================================
```

### 4.4 Contoh Penggunaan Aplikasi POS

```
Pilih menu (1-7): 1

--- TAMBAH BARANG ---
Nama Barang: Keyboard Mekanik
Kategori (Elektronik/Makanan/Pakaian/Lainnya): Elektronik
Harga Jual (Rp): 450000
Jumlah Stok: 25
Stok Minimal (default 10): 5
✓ Barang 'Keyboard Mekanik' berhasil ditambahkan!

Pilih menu (1-7): 2

--- DAFTAR INVENTARIS ---
====================================================================================================================
ID    NAMA BARANG          KATEGORI        HARGA           STOK     STOK MIN  STATUS         
====================================================================================================================
1     Keyboard Mekanik     Elektronik      Rp    450.000   25       5         ✓ OK           
====================================================================================================================

Pilih menu (1-7): 3

--- TRANSAKSI PENJUALAN ---
ID Barang yang dijual: 1
Jumlah yang dibeli: 3
==================================================
✓ TRANSAKSI BERHASIL
==================================================
Barang: Keyboard Mekanik
Jumlah: 3
Harga Satuan: Rp 450.000,00
Total: Rp 1.350.000,00
Waktu: 2024-01-20 10:30:45
==================================================
```

---

## 5. TROUBLESHOOTING

### 5.1 Error: "Access denied for user 'root'@'localhost'"

**Masalah:** Password MySQL salah atau belum dikonfigurasi

**Solusi:**
```python
# Cek credential MySQL Anda di Command Prompt
mysql -u root -p
# Masukkan password jika ada

# Kemudian ubah di file Python:
sistem = SistemManajemenKaryawan(
    host='localhost',
    user='root',
    password='password_anda',  # Isi password yang benar
    database='rizkima-python'
)
```

### 5.2 Error: "Unknown database 'rizkima-python'"

**Masalah:** Database belum dibuat

**Solusi:**
```bash
# Buka MySQL
mysql -u root -p

# Buat database
CREATE DATABASE `rizkima-python` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 5.3 Error: "No module named 'mysql'"

**Masalah:** Library mysql-connector-python belum terinstal

**Solusi:**
```bash
pip install mysql-connector-python
```

### 5.4 Error: "Connection timeout"

**Masalah:** MySQL service tidak berjalan

**Solusi:**
- **Windows:** Buka Services → MySQL → Start
- **Linux:** `sudo service mysql start`
- **macOS:** Buka System Preferences → MySQL → Start MySQL Server

### 5.5 Error: "Table already exists"

**Masalah:** Tabel sudah dibuat sebelumnya

**Solusi:** 
- Jalankan aplikasi sekali saja untuk membuat tabel
- Atau hapus database dan buat ulang

---

## 6. DATA SAMPLE UNTUK TESTING

### 6.1 Data Karyawan
```
Nama: Rina Wijaya
Posisi: Admin IT
Departemen: Administrasi
Gaji: 2500000
Tanggal: 2023-06-01

Nama: Ahmad Pratama
Posisi: Support Teknis
Departemen: Support
Gaji: 2200000
Tanggal: 2023-09-15
```

### 6.2 Data Barang POS
```
Nama: Mouse Wireless
Kategori: Elektronik
Harga: 150000
Stok: 50
Stok Min: 10

Nama: Kabel LAN Cat6
Kategori: Elektronik
Harga: 25000
Stok: 100
Stok Min: 20

Nama: Router TP-Link
Kategori: Elektronik
Harga: 350000
Stok: 15
Stok Min: 5
```

---

## 7. COMMAND PENTING

### Cek Status MySQL
```bash
# Windows (PowerShell as Admin)
Get-Service | Where-Object {$_.Name -like '*mysql*'} | fl

# Linux
sudo systemctl status mysql

# macOS
brew services list
```

### Backup Database
```bash
mysqldump -u root -p rizkima-python > backup_rizkima.sql
```

### Restore Database
```bash
mysql -u root -p rizkima-python < backup_rizkima.sql
```

### Cek Tabel Database
```bash
mysql -u root -p rizkima-python -e "SHOW TABLES;"
```

---

## 8. KONEKSI TEST

Buat file `test_koneksi.py`:
```python
import mysql.connector

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='rizkima-python'
    )
    
    if conn.is_connected():
        print("✓ Koneksi berhasil!")
        print(f"Database Info: {conn.get_server_info()}")
        
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print(f"✓ Tabel yang ada: {tables}")
        
        cursor.close()
        conn.close()
        
except Exception as e:
    print(f"✗ Error: {e}")
```

Jalankan:
```bash
python test_koneksi.py
```

---

## 📝 CATATAN PENTING

1. **Pastikan MySQL berjalan** sebelum menjalankan aplikasi
2. **Ubah credential** sesuai dengan konfigurasi MySQL Anda
3. **Database `rizkima-python` HARUS sudah dibuat** sebelum menjalankan aplikasi
4. **Tabel akan dibuat otomatis** saat aplikasi dijalankan pertama kali
5. **Simpan file backup** database secara berkala

---

## 🎓 UNTUK JURUSAN TJKT

Kedua aplikasi ini dirancang untuk melatih:
- ✅ Koneksi Database dengan Python
- ✅ CRUD Operations (Create, Read, Update, Delete)
- ✅ SQL Queries
- ✅ Data Management
- ✅ Sistem Informasi Bisnis
- ✅ Troubleshooting & Debugging

**Cocok untuk proyek kolaborasi TJKT karena:**
- Relevan dengan industri IT
- Menggunakan teknologi real-world (MySQL + Python)
- Dapat diperluas dengan fitur tambahan
- Simulasi sistem informasi perusahaan

---

**Untuk pertanyaan lebih lanjut atau error yang tidak tercantum, silakan hubungi instruktur!** 🚀
