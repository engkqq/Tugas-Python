import mysql.connector
from mysql.connector import Error
from datetime import datetime

class SistemPOS:
    """
    Sistem Inventaris & POS (Point of Sale)
    Database: rizkima-python (localhost)
    """
    
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None
        self.koneksi_database()
        self.buat_tabel()
    
    def koneksi_database(self):
        """Membuat koneksi ke database MySQL"""
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            
            if self.conn.is_connected():
                self.cursor = self.conn.cursor()
                print(f"\n✓ Koneksi database '{self.database}' berhasil!")
                return True
        except Error as e:
            print(f"\n✗ Error koneksi database: {e}")
            return False
    
    def buat_tabel(self):
        """Membuat tabel barang dan transaksi jika belum ada"""
        try:
            # Tabel Barang
            query_barang = """
            CREATE TABLE IF NOT EXISTS barang (
                id_barang INT AUTO_INCREMENT PRIMARY KEY,
                nama_barang VARCHAR(100) NOT NULL,
                kategori VARCHAR(50) NOT NULL,
                harga_jual INT NOT NULL,
                stok INT NOT NULL,
                stok_minimal INT DEFAULT 10,
                tanggal_masuk DATE NOT NULL,
                tanggal_dibuat TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
            self.cursor.execute(query_barang)
            
            # Tabel Transaksi
            query_transaksi = """
            CREATE TABLE IF NOT EXISTS transaksi (
                id_transaksi INT AUTO_INCREMENT PRIMARY KEY,
                id_barang INT NOT NULL,
                jumlah_terjual INT NOT NULL,
                harga_satuan INT NOT NULL,
                total_harga INT NOT NULL,
                tanggal_transaksi DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (id_barang) REFERENCES barang(id_barang)
            );
            """
            self.cursor.execute(query_transaksi)
            self.conn.commit()
            print("✓ Tabel barang dan transaksi siap digunakan!")
        except Error as e:
            print(f"✗ Error membuat tabel: {e}")
    
    def tambah_barang(self, nama, kategori, harga, stok, stok_min, tanggal):
        """Menambahkan barang ke inventaris"""
        try:
            query = """
            INSERT INTO barang 
            (nama_barang, kategori, harga_jual, stok, stok_minimal, tanggal_masuk)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (nama, kategori, harga, stok, stok_min, tanggal)
            self.cursor.execute(query, values)
            self.conn.commit()
            print(f"\n✓ Barang '{nama}' berhasil ditambahkan ke inventaris!")
            return True
        except Error as e:
            print(f"✗ Error menambah barang: {e}")
            return False
    
    def lihat_inventaris(self):
        """Menampilkan semua barang di inventaris"""
        try:
            query = "SELECT * FROM barang ORDER BY id_barang"
            self.cursor.execute(query)
            hasil = self.cursor.fetchall()
            
            if not hasil:
                print("\n📭 Inventaris kosong!\n")
                return
            
            print("\n" + "="*130)
            print(f"{'ID':<5} {'NAMA BARANG':<20} {'KATEGORI':<15} {'HARGA':<12} {'STOK':<8} {'STOK MIN':<10} {'STATUS':<12} {'TGL MASUK':<12}")
            print("="*130)
            
            for row in hasil:
                status = "✓ OK" if row[4] > row[5] else "⚠️ KURANG"
                print(f"{row[0]:<5} {row[1]:<20} {row[2]:<15} Rp {row[3]:>9,}  {row[4]:<8} {row[5]:<10} {status:<12} {row[6]:<12}")
            
            print("="*130 + "\n")
        except Error as e:
            print(f"✗ Error menampilkan inventaris: {e}")
    
    def transaksi_penjualan(self, id_barang, jumlah):
        """Melakukan transaksi penjualan"""
        try:
            # Cek ketersediaan barang
            query_cek = "SELECT nama_barang, harga_jual, stok FROM barang WHERE id_barang = %s"
            self.cursor.execute(query_cek, (id_barang,))
            hasil = self.cursor.fetchone()
            
            if not hasil:
                print(f"❌ Barang ID {id_barang} tidak ditemukan!\n")
                return False
            
            nama_barang, harga, stok = hasil
            
            if stok < jumlah:
                print(f"❌ Stok tidak cukup! Stok tersedia: {stok}\n")
                return False
            
            # Hitung total
            total_harga = harga * jumlah
            
            # Insert transaksi
            query_transaksi = """
            INSERT INTO transaksi 
            (id_barang, jumlah_terjual, harga_satuan, total_harga)
            VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(query_transaksi, (id_barang, jumlah, harga, total_harga))
            
            # Update stok
            stok_baru = stok - jumlah
            query_update = "UPDATE barang SET stok = %s WHERE id_barang = %s"
            self.cursor.execute(query_update, (stok_baru, id_barang))
            
            self.conn.commit()
            
            # Tampilkan bukti transaksi
            print("\n" + "="*60)
            print("✓ TRANSAKSI BERHASIL")
            print("="*60)
            print(f"Barang         : {nama_barang}")
            print(f"Jumlah         : {jumlah} pcs")
            print(f"Harga Satuan   : Rp {harga:>12,}")
            print(f"Total Harga    : Rp {total_harga:>12,}")
            print(f"Waktu          : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("="*60 + "\n")
            
            return True
        except Error as e:
            print(f"✗ Error transaksi penjualan: {e}")
            return False
    
    def update_stok(self, id_barang, stok_baru):
        """Update stok barang"""
        try:
            query_cek = "SELECT nama_barang, stok FROM barang WHERE id_barang = %s"
            self.cursor.execute(query_cek, (id_barang,))
            hasil = self.cursor.fetchone()
            
            if not hasil:
                print(f"❌ Barang ID {id_barang} tidak ditemukan!\n")
                return False
            
            nama_barang, stok_lama = hasil
            
            query = "UPDATE barang SET stok = %s WHERE id_barang = %s"
            self.cursor.execute(query, (stok_baru, id_barang))
            self.conn.commit()
            
            perubahan = stok_baru - stok_lama
            tanda = "+" if perubahan > 0 else ""
            print(f"✓ Stok '{nama_barang}' berhasil diupdate! ({tanda}{perubahan})\n")
            return True
        except Error as e:
            print(f"✗ Error update stok: {e}")
            return False
    
    def laporan_penjualan(self):
        """Menampilkan laporan penjualan"""
        try:
            query = """
            SELECT 
                t.id_transaksi,
                b.nama_barang,
                t.jumlah_terjual,
                t.harga_satuan,
                t.total_harga,
                t.tanggal_transaksi
            FROM transaksi t
            JOIN barang b ON t.id_barang = b.id_barang
            ORDER BY t.tanggal_transaksi DESC
            """
            self.cursor.execute(query)
            hasil = self.cursor.fetchall()
            
            if not hasil:
                print("\n📭 Belum ada transaksi!\n")
                return
            
            print("\n" + "="*120)
            print("LAPORAN PENJUALAN")
            print("="*120)
            print(f"{'ID':<5} {'BARANG':<20} {'JUMLAH':<8} {'HARGA SAT':<12} {'TOTAL':<15} {'TANGGAL':<19}")
            print("="*120)
            
            total_penjualan = 0
            for row in hasil:
                print(f"{row[0]:<5} {row[1]:<20} {row[2]:<8} Rp {row[3]:>9,}  Rp {row[4]:>12,}  {row[5]}")
                total_penjualan += row[4]
            
            print("="*120)
            print(f"{'TOTAL PENJUALAN:':<46} Rp {total_penjualan:>12,}\n")
        except Error as e:
            print(f"✗ Error menampilkan laporan: {e}")
    
    def laporan_stok_kurang(self):
        """Menampilkan laporan barang dengan stok kurang"""
        try:
            query = "SELECT * FROM barang WHERE stok <= stok_minimal ORDER BY stok"
            self.cursor.execute(query)
            hasil = self.cursor.fetchall()
            
            if not hasil:
                print("\n✓ Semua barang stoknya aman!\n")
                return
            
            print("\n" + "="*100)
            print("⚠️  LAPORAN BARANG DENGAN STOK KURANG")
            print("="*100)
            print(f"{'ID':<5} {'NAMA BARANG':<25} {'KATEGORI':<15} {'STOK':<8} {'STOK MIN':<10} {'SELISIH':<8}")
            print("="*100)
            
            for row in hasil:
                selisih = row[5] - row[4]
                print(f"{row[0]:<5} {row[1]:<25} {row[2]:<15} {row[4]:<8} {row[5]:<10} {selisih:<8}")
            
            print("="*100 + "\n")
        except Error as e:
            print(f"✗ Error menampilkan laporan stok kurang: {e}")
    
    def tutup_koneksi(self):
        """Menutup koneksi database"""
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("\n✓ Koneksi database ditutup.\n")

def menu_utama():
    """Menampilkan menu utama aplikasi POS"""
    
    print("\n" + "="*70)
    print("SISTEM INVENTARIS & POS (POINT OF SALE)")
    print("Database: rizkima-python | Host: localhost")
    print("="*70)
    
    # Inisialisasi sistem
    try:
        sistem = SistemPOS(
            host='localhost',
            user='root',
            password='',
            database='rizkima-python'
        )
    except:
        print("❌ Gagal terkoneksi ke database!")
        return
    
    while True:
        print("\n" + "-"*70)
        print("MENU UTAMA POS:")
        print("-"*70)
        print("1. Tambah Barang ke Inventaris")
        print("2. Lihat Inventaris")
        print("3. Transaksi Penjualan")
        print("4. Update Stok Barang")
        print("5. Laporan Penjualan")
        print("6. Laporan Barang Kurang Stok")
        print("7. Keluar")
        print("-"*70)
        
        pilihan = input("Pilih menu (1-7): ").strip()
        
        if pilihan == '1':
            print("\n--- TAMBAH BARANG ---")
            nama = input("Nama Barang: ").strip()
            kategori = input("Kategori (Elektronik/Makanan/Pakaian/Lainnya): ").strip()
            
            try:
                harga = int(input("Harga Jual (Rp): "))
                stok = int(input("Jumlah Stok: "))
                stok_min = int(input("Stok Minimal (default 10): ") or "10")
            except ValueError:
                print("❌ Harga dan stok harus berupa angka!")
                continue
            
            tanggal = input("Tanggal Masuk (YYYY-MM-DD): ").strip()
            
            if nama and kategori:
                sistem.tambah_barang(nama, kategori, harga, stok, stok_min, tanggal)
            else:
                print("❌ Nama dan kategori tidak boleh kosong!")
        
        elif pilihan == '2':
            print("\n--- DAFTAR INVENTARIS ---")
            sistem.lihat_inventaris()
        
        elif pilihan == '3':
            print("\n--- TRANSAKSI PENJUALAN ---")
            try:
                id_barang = int(input("ID Barang yang dijual: "))
                jumlah = int(input("Jumlah yang dibeli: "))
                sistem.transaksi_penjualan(id_barang, jumlah)
            except ValueError:
                print("❌ ID dan jumlah harus berupa angka!")
        
        elif pilihan == '4':
            print("\n--- UPDATE STOK BARANG ---")
            try:
                id_barang = int(input("ID Barang: "))
                stok_baru = int(input("Stok Baru: "))
                sistem.update_stok(id_barang, stok_baru)
            except ValueError:
                print("❌ ID dan stok harus berupa angka!")
        
        elif pilihan == '5':
            sistem.laporan_penjualan()
        
        elif pilihan == '6':
            sistem.laporan_stok_kurang()
        
        elif pilihan == '7':
            print("\n👋 Terima kasih telah menggunakan Sistem POS!")
            sistem.tutup_koneksi()
            break
        
        else:
            print("❌ Pilihan tidak valid! Silakan pilih 1-7.")

if __name__ == "__main__":
    menu_utama()
