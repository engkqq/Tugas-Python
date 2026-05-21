# LEMBAR SOAL PROYEK KOLABORASI
## (PROJECT-BASED LEARNING)

---

```
════════════════════════════════════════════════════════════════════════════

                             [LOGO SMK NEGERI 1 WANAYASA]

                        LEMBAR SOAL PROYEK KOLABORASI
                           (PROJECT-BASED LEARNING)

              RANCANG BANGUN APLIKASI PYTHON SEDERHANA
          DAN PENYUSUNAN LAPORAN DOKUMENTASI ILMIAH

                         Dengan Integrasi Database Localhost


                          Disusun oleh:
                          • Rizki Muhamad Adam (30)
                          • KafalaFudin (22)

                          Kelas X TJKT

                        SMK NEGERI 1 WANAYASA
                        Jl. Pendidikan, Wanayasa, Purwakarta
                        Tahun Pelajaran 2025/2026

════════════════════════════════════════════════════════════════════════════
```

---

## **KATA PENGANTAR**

Puji syukur kami panjatkan ke hadapan Allah SWT atas rahmat dan hidayah-Nya sehingga kami dapat menyelesaikan proyek kolaborasi ini dengan baik. Proyek ini dibuat sebagai bagian dari pembelajaran Project-Based Learning (PBL) untuk mata pelajaran Informatika dan IKA di kelas X TJKT.

Dalam proyek ini, kami merancang dan membangun dua aplikasi Python yang terintegrasi dengan database MySQL localhost (`rizkima-python`). Aplikasi pertama adalah Sistem Manajemen Karyawan, dan aplikasi kedua adalah Sistem Inventaris & POS (Point of Sale).

Kami mengucapkan terima kasih kepada:
- Instruktur Informatika yang telah memberikan bimbingan teknis
- Instruktur IKA yang telah memberikan arahan makalah
- Rekan-rekan seperjuangan dalam tim
- Semua pihak yang telah mendukung penyelesaian proyek ini

Kami menyadari bahwa masih banyak kekurangan dalam proyek ini. Oleh karena itu, kami mengharapkan saran dan kritik yang membangun untuk perbaikan di masa depan.

**Wanayasa, 21 Mei 2026**

**Penyusun,**

- **Rizki Muhamad Adam** (30)
- **KafalaFudin** (22)

---

## **DAFTAR ISI**

1. Pendahuluan
2. Landasan Teori
3. Analisis Kebutuhan
4. Desain Sistem
5. Implementasi
6. Pengujian Sistem
7. Integrasi Database
8. Perancangan Antarmuka & Pengguna
9. Permasalahan & Solusi
10. Penutup

---

## **DAFTAR GAMBAR & TABEL**

### **Daftar Gambar:**
1. Logo SMK NEGERI 1 WANAYASA
2. Use Case Diagram Sistem Manajemen Karyawan
3. Use Case Diagram Sistem POS Inventaris
4. Entity Relationship Diagram (ERD)
5. Flowchart Menu Utama
6. Flowchart Transaksi Penjualan
7. Screenshot Menu Aplikasi Karyawan
8. Screenshot Menu Aplikasi POS
9. Screenshot Tabel Karyawan
10. Screenshot Tabel Inventaris

### **Daftar Tabel:**
1. Identitas Proyek
2. Spesifikasi Perangkat Keras & Lunak
3. Library Python yang Digunakan
4. Struktur Tabel Database `barang`
5. Struktur Tabel Database `transaksi`
6. Struktur Tabel Database `karyawan`
7. Test Case Sistem Manajemen Karyawan
8. Test Case Sistem POS
9. Kriteria Penilaian RKA
10. Kriteria Penilaian Pelaporan

---

## **BAB I: PENDAHULUAN**

### **1.1 Latar Belakang**

Dalam era digital saat ini, penggunaan aplikasi berbasis komputer telah menjadi kebutuhan utama dalam mengelola data dan proses bisnis. Baik itu di bidang industri, perdagangan, maupun jasa, diperlukan sistem informasi yang dapat mengotomatisasi pekerjaan manual dan meningkatkan efisiensi operasional.

Bahasa pemrograman Python telah terbukti menjadi salah satu bahasa pemrograman yang powerful dan mudah dipelajari. Python dapat diintegrasikan dengan berbagai database untuk menciptakan aplikasi yang robust dan scalable. Database MySQL adalah salah satu database relasional yang paling populer dan banyak digunakan dalam industri IT.

Sebagai siswa kelas X TJKT (Teknik Jaringan Komputer & Telekomunikasi), kami perlu memahami bagaimana mengembangkan aplikasi yang terintegrasi dengan database. Oleh karena itu, proyek kolaborasi ini dirancang untuk memberikan pengalaman praktis dalam:
- Memahami konsep dasar pemrograman Python
- Mengintegrasikan aplikasi dengan database MySQL
- Mengimplementasikan CRUD operations (Create, Read, Update, Delete)
- Mendokumentasikan sebuah proyek secara ilmiah

### **1.2 Rumusan Masalah**

1. Bagaimana merancang dan membangun aplikasi Python yang dapat terkoneksi dengan database MySQL localhost?
2. Bagaimana mengimplementasikan fitur CRUD dalam aplikasi Python?
3. Bagaimana menangani error dan validasi input dalam aplikasi?
4. Bagaimana mendokumentasikan proyek secara ilmiah dan sistematis?
5. Bagaimana mengoptimalkan performa aplikasi dalam mengelola data?

### **1.3 Tujuan Proyek**

1. **Tujuan Umum:**
   - Membangun dua aplikasi Python yang fungsional dan terintegrasi dengan database MySQL
   - Mendokumentasikan proses pengembangan aplikasi secara ilmiah

2. **Tujuan Khusus:**
   - Memahami konsep OOP (Object-Oriented Programming) dalam Python
   - Menguasai teknik koneksi database MySQL dengan Python
   - Mengimplementasikan fitur CRUD dalam aplikasi
   - Membuat UI yang user-friendly dan responsif
   - Melakukan testing dan debugging yang sistematis
   - Menulis dokumentasi teknis yang lengkap dan terstruktur

### **1.4 Manfaat Proyek**

**Bagi Siswa:**
- Mendapatkan pengalaman praktis dalam mengembangkan aplikasi berbasis database
- Meningkatkan kemampuan problem-solving dan critical thinking
- Belajar bekerja dalam tim secara kolaboratif
- Mempersiapkan diri untuk dunia kerja industri IT

**Bagi Sekolah:**
- Menghasilkan portfolio proyek berkualitas untuk akreditasi sekolah
- Meningkatkan standar pembelajaran Project-Based Learning
- Menjadi referensi untuk pembelajaran siswa di tahun depan

**Bagi Industri:**
- Menghasilkan talenta yang siap pakai di industri IT
- Meningkatkan kualitas SDM di bidang teknologi informasi

---

## **BAB II: LANDASAN TEORI**

### **2.1 Konsep Dasar Python**

#### **2.1.1 Pengenalan Python**
Python adalah bahasa pemrograman tingkat tinggi yang diciptakan oleh Guido van Rossum pada tahun 1989. Python dirancang dengan filosofi "simple is better than complex" yang membuat kode Python mudah dibaca dan dipahami.

#### **2.1.2 Tipe Data dalam Python**
- **Integer (int):** Tipe data untuk bilangan bulat (contoh: 10, -5, 0)
- **Float (float):** Tipe data untuk bilangan desimal (contoh: 3.14, -2.5)
- **String (str):** Tipe data untuk teks (contoh: "Rizki", "Hello World")
- **Boolean (bool):** Tipe data untuk nilai kebenaran (True atau False)
- **List:** Tipe data untuk kumpulan elemen yang terurut
- **Dictionary:** Tipe data untuk kumpulan key-value pairs
- **Tuple:** Tipe data untuk kumpulan elemen yang immutable

#### **2.1.3 Kontrol Alur Program**
- **If-Else:** Struktur kondisional untuk membuat keputusan
- **For Loop:** Perulangan yang diketahui jumlah iterasinya
- **While Loop:** Perulangan yang bergantung pada kondisi
- **Break & Continue:** Statement untuk mengontrol loop

#### **2.1.4 Fungsi dalam Python**
Fungsi adalah blok kode yang dapat dipanggil berulang kali dengan input parameter dan mengembalikan output.

```python
def nama_fungsi(parameter1, parameter2):
    """Docstring untuk menjelaskan fungsi"""
    # Kode fungsi
    return hasil
```

#### **2.1.5 Object-Oriented Programming (OOP)**
OOP adalah paradigma pemrograman yang menggunakan konsep objek dan kelas untuk mengorganisir kode.

```python
class NamaKelas:
    def __init__(self, parameter):
        self.atribut = parameter
    
    def method(self):
        # Kode method
        pass
```

### **2.2 Database dan SQL**

#### **2.2.1 Pengenalan Database**
Database adalah kumpulan data yang terorganisir dan dapat diakses melalui sistem database management system (DBMS). Database relasional menggunakan konsep tabel dengan baris dan kolom.

#### **2.2.2 MySQL**
MySQL adalah salah satu DBMS relasional yang open-source dan populer. MySQL menggunakan SQL (Structured Query Language) sebagai bahasa query-nya.

#### **2.2.3 CRUD Operations**
- **Create (INSERT):** Menambahkan data baru ke dalam tabel
- **Read (SELECT):** Membaca dan menampilkan data dari tabel
- **Update (UPDATE):** Mengubah data yang sudah ada
- **Delete (DELETE):** Menghapus data dari tabel

#### **2.2.4 SQL Query Dasar**
```sql
-- INSERT
INSERT INTO tabel (kolom1, kolom2) VALUES (nilai1, nilai2);

-- SELECT
SELECT * FROM tabel;
SELECT kolom1, kolom2 FROM tabel WHERE kondisi;

-- UPDATE
UPDATE tabel SET kolom1 = nilai1 WHERE kondisi;

-- DELETE
DELETE FROM tabel WHERE kondisi;
```

### **2.3 Arsitektur Aplikasi**

Arsitektur aplikasi ini menggunakan model client-server dengan struktur:
1. **Client (Python Application):** Layer yang berinteraksi langsung dengan user
2. **Database (MySQL):** Layer yang menyimpan data

### **2.4 Library & Framework yang Digunakan**

- **mysql-connector-python:** Library untuk koneksi Python ke MySQL
- **datetime:** Library bawaan Python untuk menangani tanggal dan waktu
- **sys:** Library bawaan Python untuk operasi sistem

---

## **BAB III: ANALISIS KEBUTUHAN**

### **3.1 Analisis Sistem Saat Ini**

**Sistem Manajemen Karyawan:**
- Saat ini, manajemen data karyawan masih dilakukan secara manual menggunakan file Excel
- Proses pencarian data karyawan memakan waktu lama
- Sulit untuk membuat laporan statistik gaji secara real-time
- Risiko kehilangan data karena hanya tersimpan di satu file

**Sistem Inventaris & POS:**
- Pencatatan stok barang masih manual menggunakan catatan fisik
- Transaksi penjualan dicatat secara tidak terstruktur
- Sulit mengontrol stok barang yang minim
- Laporan penjualan dibuat secara manual dan memakan waktu

### **3.2 Kebutuhan Fungsional**

**Sistem Manajemen Karyawan:**
1. Menambahkan data karyawan baru
2. Menampilkan daftar semua karyawan
3. Mencari data karyawan berdasarkan nama atau ID
4. Mengupdate status karyawan (Aktif, Cuti, Resign, Pensiun)
5. Menampilkan statistik gaji
6. Menghapus data karyawan

**Sistem POS:**
1. Menambahkan barang ke inventaris
2. Menampilkan daftar inventaris
3. Melakukan transaksi penjualan
4. Mengupdate stok barang
5. Menampilkan laporan penjualan
6. Menampilkan laporan stok barang yang minim

### **3.3 Kebutuhan Non-Fungsional**

1. **Performance:** Aplikasi harus merespons dalam waktu < 2 detik
2. **Security:** Data harus aman dan terlindungi dari akses tidak sah
3. **Usability:** Interface harus mudah digunakan oleh pengguna
4. **Reliability:** Aplikasi harus berjalan tanpa error
5. **Scalability:** Aplikasi dapat ditambah fitur di masa depan

### **3.4 Use Case Diagram**

**Sistem Manajemen Karyawan:**
```
┌─────────────────────────────────────────┐
│         Administrator Karyawan          │
└─────────────────────────────────────────┘
           ▲        │        ▼
      ┌────┴────┬───┴────┬────┴────┐
      │         │        │         │
   Tambah    Lihat   Cari     Update
  Karyawan Karyawan Karyawan Karyawan
      │         │        │         │
      └────┬────┴───┬────┴────┬────┘
           │        │         │
      ┌────▼────────▼─────────▼────┐
      │   SISTEM MANAJEMEN KARYAWAN│
      │      (Database MySQL)       │
      └─────────────────────────────┘
```

**Sistem POS:**
```
┌─────────────────────────────────────────┐
│          Kasir / Admin POS              │
└─────────────────────────────────────────┘
           ▲        │        ▼
      ┌────┴────┬───┴────┬────┴────┐
      │         │        │         │
   Tambah    Lihat   Transaksi  Laporan
   Barang   Barang  Penjualan  Penjualan
      │         │        │         │
      └────┬────┴───┬────┴────┬────┘
           │        │         │
      ┌────▼────────▼─────────▼────┐
      │ SISTEM INVENTARIS & POS    │
      │      (Database MySQL)       │
      └──────────────────────────���──┘
```

---

## **BAB IV: DESAIN SISTEM**

### **4.1 Entity Relationship Diagram (ERD)**

**Database: rizkima-python**

```
┌─────────────────────┐        ┌──────────────────────┐
│      KARYAWAN       │        │       BARANG         │
├─────────────────────┤        ├──────────────────────┤
│ id_karyawan (PK)    │        │ id_barang (PK)       │
│ nama_karyawan       │        │ nama_barang          │
│ posisi              │        │ kategori             │
│ departemen          │        │ harga_jual           │
│ gaji                │        │ stok                 │
│ tanggal_bergabung   │        │ stok_minimal         │
│ status              │        │ tanggal_masuk        │
│ tanggal_dibuat      │        │ tanggal_dibuat       │
└─────────────────────┘        └──────────────────────┘
                                         │
                                         │ 1 : N
                                         │
                               ┌─────────▼──────────────┐
                               │     TRANSAKSI         │
                               ├──────────────────────┤
                               │ id_transaksi (PK)    │
                               │ id_barang (FK)       │
                               │ jumlah_terjual       │
                               │ harga_satuan         │
                               │ total_harga          │
                               │ tanggal_transaksi    │
                               └──────────────────────┘
```

### **4.2 Struktur Database**

**Tabel KARYAWAN:**
```sql
CREATE TABLE karyawan (
    id_karyawan INT AUTO_INCREMENT PRIMARY KEY,
    nama_karyawan VARCHAR(100) NOT NULL,
    posisi VARCHAR(50) NOT NULL,
    departemen VARCHAR(50) NOT NULL,
    gaji INT NOT NULL,
    tanggal_bergabung DATE NOT NULL,
    status ENUM('Aktif', 'Cuti', 'Resign', 'Pensiun') DEFAULT 'Aktif',
    tanggal_dibuat TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Tabel BARANG:**
```sql
CREATE TABLE barang (
    id_barang INT AUTO_INCREMENT PRIMARY KEY,
    nama_barang VARCHAR(100) NOT NULL,
    kategori VARCHAR(50) NOT NULL,
    harga_jual INT NOT NULL,
    stok INT NOT NULL,
    stok_minimal INT DEFAULT 10,
    tanggal_masuk DATE NOT NULL,
    tanggal_dibuat TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Tabel TRANSAKSI:**
```sql
CREATE TABLE transaksi (
    id_transaksi INT AUTO_INCREMENT PRIMARY KEY,
    id_barang INT NOT NULL,
    jumlah_terjual INT NOT NULL,
    harga_satuan INT NOT NULL,
    total_harga INT NOT NULL,
    tanggal_transaksi DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_barang) REFERENCES barang(id_barang)
);
```

### **4.3 Flowchart Aplikasi**

**Flowchart Menu Utama:**
```
┌─────────────────────┐
│     START / MULAI   │
└──────────┬──────────┘
           │
    ┌──────▼──────┐
    │ Koneksi DB  │
    └──────┬──────┘
           │
    ┌──────▼──────────┐
    │  TAMPIL MENU    │
    └──────┬──────────┘
           │
      ┌────┴──────────────────────┐
      │   PILIHAN MENU ?           │
      └────┬──────────────────────┘
      ┌────┴────┬─────┬──────┬─────┐
      │         │     │      │     │
   [1]↓      [2]↓  [3]↓   [4]↓  [7]↓
    ┌──┐    ┌──┐ ┌──┐  ┌──┐ ┌─────┐
    │Tn│    │Lh│ │Cr│  │Ut│ │Exit │
    │Bh│    │t │ │i │  │p │ │ DBS │
    └┬─┘    └┬─┘ └┬─┘  └┬─┘ └─────┘
     │      │    │     │
     └──────┼────┼─────┘
            │    │
        ┌───▼────▼────┐
        │ Kembali Menu│
        └─────┬───────┘
              │
              └──► [Loop kembali ke TAMPIL MENU]
```

### **4.4 Class Diagram**

**Sistem Manajemen Karyawan:**
```
┌─────────────────────────────────────┐
│  SistemManajemenKaryawan            │
├─────────────────────────────────────┤
│ - host: str                         │
│ - user: str                         │
│ - password: str                     │
│ - database: str                     │
│ - conn: Connection                  │
│ - cursor: Cursor                    │
├─────────────────────────────────────┤
│ + __init__()                        │
│ + koneksi_database()                │
│ + buat_tabel()                      │
│ + tambah_karyawan()                 │
│ + lihat_karyawan()                  │
│ + cari_karyawan()                   │
│ + update_status()                   │
│ + statistik_gaji()                  │
│ + hapus_karyawan()                  │
│ + tutup_koneksi()                   │
└─────────────────────────────────────┘
```

**Sistem POS:**
```
┌─────────────────────────────────────┐
│  SistemPOS                          │
├─────────────────────────────────────┤
│ - host: str                         │
│ - user: str                         │
│ - password: str                     │
│ - database: str                     │
│ - conn: Connection                  │
│ - cursor: Cursor                    │
├─────────────────────────────────────┤
│ + __init__()                        │
│ + koneksi_database()                │
│ + buat_tabel()                      │
│ + tambah_barang()                   │
│ + lihat_inventaris()                │
│ + transaksi_penjualan()             │
│ + update_stok()                     │
│ + laporan_penjualan()               │
│ + laporan_stok_kurang()             │
│ + tutup_koneksi()                   │
└─────────────────────────────────────┘
```

---

## **BAB V: IMPLEMENTASI**

### **5.1 Lingkungan Pengembangan**

**Spesifikasi Perangkat:**
- Processor: Intel Core i5 / AMD Ryzen 5
- RAM: 8 GB
- Storage: 256 GB SSD
- OS: Windows 10/11 atau Linux

**Software:**
- Python 3.8+
- MySQL Server 5.7+
- Text Editor: Visual Studio Code / PyCharm
- Git (untuk version control)

### **5.2 Library dan Dependencies**

```
mysql-connector-python==8.0.33
datetime (built-in)
sys (built-in)
```

**Instalasi:**
```bash
pip install mysql-connector-python
```

### **5.3 Struktur File Proyek**

```
engkqq/Tugas-Python/
├── sistem_manajemen_karyawan_db.py
├── sistem_pos_inventaris_db.py
├── PANDUAN_DATABASE_SETUP.md
├── LAPORAN_PROYEK_KOLABORASI.md
└── README.md
```

### **5.4 Potongan Kode Penting**

**Koneksi Database:**
```python
import mysql.connector

def koneksi_database(host, user, password, database):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
```

**CRUD - CREATE:**
```python
def tambah_karyawan(self, nama, posisi, departemen, gaji, tanggal):
    query = """
    INSERT INTO karyawan 
    (nama_karyawan, posisi, departemen, gaji, tanggal_bergabung)
    VALUES (%s, %s, %s, %s, %s)
    """
    self.cursor.execute(query, (nama, posisi, departemen, gaji, tanggal))
    self.conn.commit()
```

**CRUD - READ:**
```python
def lihat_karyawan(self):
    query = "SELECT * FROM karyawan"
    self.cursor.execute(query)
    return self.cursor.fetchall()
```

**CRUD - UPDATE:**
```python
def update_status(self, id_karyawan, status_baru):
    query = "UPDATE karyawan SET status = %s WHERE id_karyawan = %s"
    self.cursor.execute(query, (status_baru, id_karyawan))
    self.conn.commit()
```

**CRUD - DELETE:**
```python
def hapus_karyawan(self, id_karyawan):
    query = "DELETE FROM karyawan WHERE id_karyawan = %s"
    self.cursor.execute(query, (id_karyawan,))
    self.conn.commit()
```

---

## **BAB VI: PENGUJIAN SISTEM**

### **6.1 Test Case Sistem Manajemen Karyawan**

| No | Test Case | Input | Expected Output | Hasil |
|----|-----------|-------|-----------------|-------|
| 1 | Tambah Karyawan | Nama: Rizki, Posisi: IT | ✓ Karyawan berhasil ditambahkan | ✓ PASS |
| 2 | Lihat Karyawan | - | Tampil daftar karyawan | ✓ PASS |
| 3 | Cari Karyawan | ID: 1 | Tampil data karyawan ID 1 | ✓ PASS |
| 4 | Statistik Gaji | - | Tampil total & rata-rata gaji | ✓ PASS |
| 5 | Update Status | ID: 1, Status: Cuti | ✓ Status berhasil diupdate | ✓ PASS |
| 6 | Hapus Karyawan | ID: 1 | ✓ Karyawan berhasil dihapus | ✓ PASS |

### **6.2 Test Case Sistem POS**

| No | Test Case | Input | Expected Output | Hasil |
|----|-----------|-------|-----------------|-------|
| 1 | Tambah Barang | Nama: Keyboard | ✓ Barang berhasil ditambahkan | ✓ PASS |
| 2 | Lihat Inventaris | - | Tampil daftar barang | ✓ PASS |
| 3 | Transaksi Penjualan | ID: 1, Qty: 2 | ✓ Transaksi berhasil | ✓ PASS |
| 4 | Update Stok | ID: 1, Stok: 20 | ✓ Stok berhasil diupdate | ✓ PASS |
| 5 | Laporan Penjualan | - | Tampil laporan penjualan | ✓ PASS |
| 6 | Laporan Stok Kurang | - | Tampil barang stok < minimal | ✓ PASS |

### **6.3 Analisis Hasil Pengujian**

Dari pengujian yang telah dilakukan, semua fitur aplikasi berfungsi dengan baik. Tidak ada bug atau error yang ditemukan dalam testing. Aplikasi dapat:
- Tersambung ke database dengan baik
- Melakukan operasi CRUD dengan sukses
- Menangani error dengan tepat
- Memberikan feedback yang jelas kepada pengguna

---

## **BAB VII: INTEGRASI DATABASE**

### **7.1 Konfigurasi Database `rizkima-python`**

**Membuat Database:**
```sql
CREATE DATABASE `rizkima-python` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

**Konfigurasi Koneksi di Python:**
```python
sistem = SistemManajemenKaryawan(
    host='localhost',
    user='root',
    password='',
    database='rizkima-python'
)
```

### **7.2 Query Database Utama**

**Query Manajemen Karyawan:**
```sql
-- Tambah karyawan
INSERT INTO karyawan (nama_karyawan, posisi, departemen, gaji, tanggal_bergabung)
VALUES ('Rizki Muhamad Adam', 'Teknisi Jaringan', 'IT', 3500000, '2024-01-15');

-- Lihat semua karyawan
SELECT * FROM karyawan ORDER BY id_karyawan;

-- Cari karyawan berdasarkan nama
SELECT * FROM karyawan WHERE nama_karyawan LIKE '%Rizki%';

-- Statistik gaji
SELECT COUNT(*) AS jumlah, SUM(gaji) AS total, AVG(gaji) AS rata_rata FROM karyawan;

-- Update status
UPDATE karyawan SET status = 'Cuti' WHERE id_karyawan = 1;

-- Hapus karyawan
DELETE FROM karyawan WHERE id_karyawan = 1;
```

**Query Sistem POS:**
```sql
-- Tambah barang
INSERT INTO barang (nama_barang, kategori, harga_jual, stok, stok_minimal, tanggal_masuk)
VALUES ('Keyboard Mekanik', 'Elektronik', 450000, 25, 5, '2024-01-20');

-- Transaksi penjualan
INSERT INTO transaksi (id_barang, jumlah_terjual, harga_satuan, total_harga)
VALUES (1, 3, 450000, 1350000);

-- Update stok
UPDATE barang SET stok = 22 WHERE id_barang = 1;

-- Laporan penjualan
SELECT b.nama_barang, t.jumlah_terjual, t.total_harga, t.tanggal_transaksi
FROM transaksi t
JOIN barang b ON t.id_barang = b.id_barang;

-- Barang dengan stok kurang
SELECT * FROM barang WHERE stok <= stok_minimal;
```

### **7.3 Optimasi Database**

**Indexing:**
```sql
ALTER TABLE karyawan ADD INDEX idx_nama (nama_karyawan);
ALTER TABLE barang ADD INDEX idx_kategori (kategori);
ALTER TABLE transaksi ADD INDEX idx_tanggal (tanggal_transaksi);
```

**Query Optimization:**
- Menggunakan LIMIT untuk membatasi hasil
- Menggunakan WHERE clause yang efisien
- Menggunakan JOIN daripada multiple query
- Menghindari SELECT * dan hanya ambil kolom yang diperlukan

---

## **BAB VIII: PERANCANGAN ANTARMUKA & PENGGUNA**

### **8.1 Desain Menu Utama**

**Menu Sistem Manajemen Karyawan:**
```
══════════════════════════════════════════════════════
SISTEM MANAJEMEN KARYAWAN
Database: rizkima-python | Host: localhost
══════════════════════════════════════════════════════
✓ Koneksi database 'rizkima-python' berhasil!
✓ Tabel karyawan siap digunakan!

──────────────────────────────────────────────────────
MENU UTAMA:
──────────────────────────────────────────────────────
1. Tambah Karyawan Baru
2. Tampilkan Semua Karyawan
3. Cari Karyawan
4. Lihat Statistik Gaji
5. Update Status Karyawan
6. Hapus Karyawan
7. Keluar
──────────────────────────────────────────────────────
Pilih menu (1-7):
```

**Menu Sistem POS:**
```
═════════════════════════════════════════════════════════
SISTEM INVENTARIS & POS (POINT OF SALE)
Database: rizkima-python | Host: localhost
═════════════════════════════════════════════════════════
✓ Koneksi database 'rizkima-python' berhasil!
✓ Tabel barang dan transaksi siap digunakan!

─────────────────────────────────────────────────────────
MENU UTAMA POS:
─────────────────────────────────────────────────────────
1. Tambah Barang ke Inventaris
2. Lihat Inventaris
3. Transaksi Penjualan
4. Update Stok Barang
5. Laporan Penjualan
6. Laporan Barang Kurang Stok
7. Keluar
─────────────────────────────────────────────────────────
Pilih menu (1-7):
```

### **8.2 User Flow**

**Flow Tambah Karyawan:**
```
User pilih Menu 1
    ↓
Input Nama Karyawan
    ↓
Input Posisi
    ↓
Input Departemen
    ↓
Input Gaji
    ↓
Input Tanggal Bergabung
    ↓
Validasi Input
    ↓
Insert ke Database
    ↓
Tampil Pesan Sukses
    ↓
Kembali ke Menu Utama
```

**Flow Transaksi Penjualan:**
```
User pilih Menu 3
    ↓
Input ID Barang
    ↓
Input Jumlah Beli
    ↓
Validasi Stok
    ↓
Hitung Total Harga
    ↓
Insert Transaksi
    ↓
Update Stok
    ↓
Tampil Bukti Transaksi
    ↓
Kembali ke Menu Utama
```

### **8.3 Feedback dan Validasi Input**

**Validasi Input:**
```python
# Validasi angka
try:
    jumlah = int(input("Jumlah: "))
except ValueError:
    print("❌ Jumlah harus berupa angka!")

# Validasi string kosong
nama = input("Nama: ").strip()
if not nama:
    print("❌ Nama tidak boleh kosong!")

# Validasi range
if jumlah < 0:
    print("❌ Jumlah tidak boleh negatif!")
```

**Feedback Pengguna:**
```
✓ Operasi berhasil      → Tampil pesan sukses
❌ Operasi gagal         → Tampil pesan error
⚠️  Peringatan          → Tampil pesan warning
📭 Data tidak ditemukan  → Tampil pesan kosong
```

---

## **BAB IX: PERMASALAHAN & SOLUSI**

### **9.1 Hambatan yang Dihadapi**

1. **Hambatan Teknis:**
   - **Masalah:** Koneksi database tidak terkoneksi pada percobaan pertama
     - **Penyebab:** Password MySQL tidak dikonfigurasi dengan benar
     - **Durasi:** 2 jam
   
   - **Masalah:** Error pada query JOIN
     - **Penyebab:** Foreign key belum dikonfigurasi dengan benar
     - **Durasi:** 1 jam

2. **Hambatan Non-Teknis:**
   - **Masalah:** Perbedaan pemahaman struktur database antar anggota tim
     - **Penyebab:** Kurangnya komunikasi tim di awal project
     - **Durasi:** 3 jam
   
   - **Masalah:** Keterlambatan pengumpulan kode karena kesalahpahaman deadline
     - **Penyebab:** Miscommunication dalam tim
     - **Durasi:** 1 hari

### **9.2 Solusi yang Diterapkan**

1. **Untuk Masalah Koneksi Database:**
   - Membuat script test_koneksi.py untuk debugging
   - Mengubah konfigurasi password di setiap aplikasi
   - Testing koneksi berulang kali
   - Dokumentasi credentials di file README

2. **Untuk Error Query JOIN:**
   - Mempelajari dokumentasi MySQL tentang Foreign Key
   - Menguji query secara terpisah di MySQL Workbench
   - Memahami relasi antar tabel dengan lebih baik
   - Menambahkan error handling pada setiap query

3. **Untuk Perbedaan Pemahaman:**
   - Membuat meeting tim untuk alignment
   - Membuat dokumentasi desain database yang jelas
   - Sharing code dan best practice
   - Melakukan code review bersama-sama

4. **Untuk Masalah Deadline:**
   - Membuat timeline yang jelas dan tertulis
   - Melakukan daily standup meeting
   - Menggunakan Google Calendar untuk reminder
   - Komunikasi intensif via WhatsApp/Discord

### **9.3 Pelajaran yang Didapat**

1. **Pelajaran Teknis:**
   - Pentingnya konfigurasi awal yang tepat dalam koneksi database
   - Cara menggunakan Foreign Key untuk relasi antar tabel
   - Teknik debugging yang efektif menggunakan print dan logging
   - Pentingnya error handling dalam setiap operasi database

2. **Pelajaran Non-Teknis:**
   - Komunikasi tim yang baik adalah kunci sukses project
   - Dokumentasi yang jelas memudahkan kolaborasi
   - Perencanaan yang matang menghemat waktu di kemudian hari
   - Testing yang menyeluruh mencegah bug di production
   - Version control (Git) penting untuk team collaboration

3. **Pelajaran untuk Masa Depan:**
   - Akan lebih teliti dalam setup awal project
   - Akan membuat timeline yang lebih detail dengan buffer time
   - Akan melakukan daily standup meeting di setiap project
   - Akan menggunakan Git lebih baik untuk version control
   - Akan membuat test case sebelum coding (TDD approach)

---

## **BAB X: PENUTUP**

### **10.1 Kesimpulan**

Proyek kolaborasi ini telah berhasil menghasilkan dua aplikasi Python yang terintegrasi dengan database MySQL localhost (`rizkima-python`):

1. **Sistem Manajemen Karyawan** - Aplikasi untuk mengelola data karyawan dengan fitur CRUD lengkap, statistik gaji, dan update status.

2. **Sistem Inventaris & POS** - Aplikasi untuk mengelola inventaris barang dan transaksi penjualan dengan fitur CRUD, laporan penjualan, dan alert stok.

Kedua aplikasi telah melalui tahap development, testing, dan deployment. Semua fitur berfungsi dengan baik dan siap digunakan.

Melalui proyek ini, kami telah belajar banyak tentang:
- Konsep dasar Python dan OOP
- Integrasi Python dengan MySQL
- Implementasi CRUD operations
- Teknik error handling dan validasi
- Dokumentasi teknis yang sistematis
- Kolaborasi tim dalam project development

Proyek ini dapat menjadi dasar untuk pengembangan lebih lanjut di masa depan, seperti:
- Menambahkan fitur reporting yang lebih advanced
- Implementasi user authentication
- Migrasi ke web application
- Implementasi REST API
- Deployment ke cloud server

### **10.2 Rekomendasi Pengembangan Lebih Lanjut**

**Jangka Pendek (1-2 minggu):**
1. Menambahkan fitur export data ke Excel/PDF
2. Implementasi backup & restore database otomatis
3. Menambahkan fitur undo/redo untuk operasi

**Jangka Menengah (1 bulan):**
1. Konversi ke Web Application menggunakan Flask/Django
2. Implementasi user login dan permission system
3. Menambahkan fitur advanced reporting dan analytics
4. Implementasi cache untuk performa yang lebih baik

**Jangka Panjang (3-6 bulan):**
1. Deployment ke cloud server (AWS, Google Cloud, Azure)
2. Implementasi REST API untuk mobile app
3. Integrasi dengan payment gateway untuk transaksi online
4. Implementasi machine learning untuk prediksi penjualan

### **10.3 Daftar Pustaka**

1. Lutz, M. (2013). *Learning Python: Powerful Object-Oriented Programming*. O'Reilly Media.
2. Debarshi, R. (2020). *MySQL Database Administration*. Packt Publishing.
3. Real Python Documentation. (2024). Retrieved from https://realpython.com/
4. MySQL Official Documentation. (2024). Retrieved from https://dev.mysql.com/doc/
5. W3Schools Python Tutorial. (2024). Retrieved from https://www.w3schools.com/python/
6. Python Official Documentation. (2024). Retrieved from https://docs.python.org/3/
7. GeeksforGeeks. (2024). *Python Database Programming*. Retrieved from https://www.geeksforgeeks.org/
8. Stack Overflow. (2024). Retrieved from https://stackoverflow.com/
9. GitHub. (2024). Retrieved from https://github.com/
10. YouTube - Programming Tutorials. (2024). Various channels.

---

## **LAMPIRAN**

### **Lampiran A: Code Listing**
- sistem_manajemen_karyawan_db.py (500+ lines)
- sistem_pos_inventaris_db.py (500+ lines)

### **Lampiran B: Test Results**
- Test Case Excel/Screenshot
- Error Log & Debugging Notes

### **Lampiran C: Database Backup**
- Struktur tabel SQL
- Sample data

### **Lampiran D: Dokumentasi Penggunaan**
- User Manual
- Troubleshooting Guide
- FAQ

---

**Disusun oleh:**
- **Rizki Muhamad Adam** (30)
- **KafalaFudin** (22)

**Kelas X TJKT - SMK NEGERI 1 WANAYASA**

**Wanayasa, 21 Mei 2026**

---

*Laporan ini merupakan bagian dari Proyek Kolaborasi Project-Based Learning untuk Mata Pelajaran Informatika dan IKA.*

*© 2026 SMK NEGERI 1 WANAYASA. All Rights Reserved.*
