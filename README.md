# Tugas-UAS-Project-Pemrogaman
# DATA DIRI
## Nama : RO'UF MUHAMMAD FAUZAN
## Kelas : TI.24.A1
## NIM : 312410157
## Program akan meminta masukan data yang terdiri dari nama produk, harga produk, dan jumlah stok produk.
![output UAS project](https://github.com/user-attachments/assets/3a81cfd1-d824-49ad-95c1-c78e24f1b830)
## Class Data
## _init.py
```Python
# class_data/__init__.py
from .class_data import Data
```
## class_data.py
```Python
import random

class Data:
    def __init__(self):
        self.database_member = {}
        self.riwayat_pembelian = []

    def generate_card_number(self):
        """Menghasilkan nomor kartu member secara acak."""
        return f"MC-{random.randint(1000, 9999)}"

    def tambah_member(self, nama):
        """Menambahkan nama member ke dalam database."""
        if nama not in self.database_member:
            nomor_kartu = self.generate_card_number()
            self.database_member[nama] = nomor_kartu
            return f"{nama} telah ditambahkan sebagai member dengan nomor kartu {nomor_kartu}."
        else:
            return f"{nama} sudah terdaftar sebagai member."

    def daftar_member(self):
        """Menampilkan daftar member yang terdaftar."""
        if self.database_member:
            return self.database_member
        else:
            return "Belum ada member yang terdaftar."

    def simpan_riwayat(self, pembelian):
        """Menyimpan riwayat pembelian."""
        self.riwayat_pembelian.append(pembelian)

    def lihat_riwayat(self):
        """Menampilkan riwayat pembelian tiket."""
        return self.riwayat_pembelian
```
## Class Process
## _init.py
```Python
# class_process/__init__.py
from .class_process import Process
```
## class_process.py
```Python
class Process:
    def __init__(self, data):
        self.data = data

    def hitung_harga_tiket(self, tipe_tiket, status_member):
        """Menghitung harga tiket bioskop berdasarkan tipe dan status member."""
        harga_dasar = 50000 if tipe_tiket == "1" else 100000
        diskon = 0.2 if status_member == "ya" else 0
        total_harga = harga_dasar - (harga_dasar * diskon)
        return total_harga, harga_dasar, diskon

    def beli_tiket(self, tipe_tiket, status_member, jumlah_tiket):
        """Mengelola pembelian tiket."""
        total_harga = 0
        for _ in range(jumlah_tiket):
            harga, harga_dasar, diskon = self.hitung_harga_tiket(tipe_tiket, status_member)
            total_harga += harga
        return total_harga
```
## Class View
##  _init.py
```Python
# class view/__init__.py
from .class_view import View
```
## class_view.py
```Python
class View:
    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def display_member_list(members):
        print("\n=== Daftar Member ===")
        print(f"{'Nama Member':<20} {'Nomor Kartu':<15}")
        print("=" * 35)
        
        for member, nomor_kartu in members.items():
            print(f"{member:<20} {nomor_kartu:<15}")

    @staticmethod
    def display_purchase_history(history):
        print("\n=== Riwayat Pembelian Tiket ===")
        print(f"{'No':<5} {'Tipe Tiket':<20} {'Status Member':<15} {'Jumlah Tiket':<15} {'Total Harga':<15}")
        print("=" * 80)
        
        for index, pembelian in enumerate(history, start=1):
            print(f"{index:<5} {pembelian['tipe_tiket']:<20} {'Ya' if pembelian['status_member'] == 'ya' else 'Tidak':<15} {pembelian['jumlah_tiket']:<15} Rp{pembelian['total_harga']:,.0f}")

    @staticmethod
    def display_ticket_receipt(pembelian):
        print("\n=== Struk Pembelian Tiket ===")
        print(f"{'Detail':<30} {'Informasi':<15}")
        print("=" * 50)
        
        print(f"{'Tipe Tiket':<30} {pembelian['tipe_tiket']:<15}")
        print(f"{'Status Member':<30} {'Ya' if pembelian['status_member'] == 'ya' else 'Tidak':<15}")
        print(f"{'Jumlah Tiket':<30} {pembelian['jumlah_tiket']:<15}")
        
        # Hitung total harga awal
        total_harga_awal = pembelian['total_harga']
        print(f"{'Total Harga Awal':<30} Rp{total_harga_awal:,.0f}")

        # Hitung potongan harga jika member
        if pembelian['status_member'] == 'ya':
            potongan_harga = total_harga_awal * 0.2  # Potongan 20%
            total_harga_setelah_diskon = total_harga_awal - potongan_harga
            print(f"{'Potongan Harga':<30} Rp{potongan_harga:,.0f}")
            print(f"{'Total Harga Setelah Diskon':<30} Rp{total_harga_setelah_diskon:,.0f}")
        else:
            print(f"{'Total Harga':<30} Rp{total_harga_awal:,.0f}")

        print("Terima kasih telah membeli tiket!")
```
## main.py
```Python
from class_data import Data
from class_view import View
from class_process import Process

def main():
    data = Data()
    process = Process(data)

    while True:
        print("\n=== Menu Utama ===")
        print("1. Beli Tiket")
        print("2. Tambah Member")
        print("3. Lihat Daftar Member")
        print("4. Lihat Riwayat Pembelian Tiket")
        print("5. Keluar")

        pilihan = input("Pilih menu (1/2/3/4/5): ")
        if pilihan == "1":
            # Logika untuk membeli tiket
            tipe_tiket = input("Masukkan tipe tiket (1 untuk Reguler, 2 untuk VIP): ")
            status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower()
            
            if status_member == 'ya':
                nama_member = input("Masukkan nama member: ")
                nomor_kartu = input("Masukkan nomor kartu member: ")
                
                # Verifikasi member
                members = data.daftar_member()  # Ambil daftar member
                if (nama_member not in members) or (nomor_kartu != members[nama_member]):
                    View.display_message("Nama atau nomor kartu member tidak terdaftar. Anda tidak dapat menggunakan status member.")
                    status_member = 'tidak'  # Set status_member ke 'tidak' jika tidak terdaftar

            # Validasi jumlah tiket
            while True:
                try:
                    jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dibeli: "))
                    if jumlah_tiket > 0:
                        break
                    else:
                        print("Jumlah tiket harus lebih dari 0.")
                except ValueError:
                    print("Input tidak valid! Silakan masukkan angka.")

            # Hitung total harga
            total_harga = process.beli_tiket(tipe_tiket, status_member, jumlah_tiket)
            
            # Simpan riwayat pembelian
            pembelian = {
                'tipe_tiket': 'Reguler' if tipe_tiket == "1" else 'VIP',
                'status_member': status_member,
                'jumlah_tiket': jumlah_tiket,
                'total_harga': total_harga
            }
            data.simpan_riwayat(pembelian)
            
            # Tampilkan total harga
            View.display_message(f"Total harga untuk {jumlah_tiket} tiket: Rp{total_harga:,.0f}")
            
            # Tampilkan struk pembelian
            View.display_ticket_receipt(pembelian)
            
        elif pilihan == "2":
            nama = input("Masukkan nama member: ")
            message = data.tambah_member(nama)
            View.display_message(message)
        elif pilihan == "3":
            members = data.daftar_member()
            View.display_member_list(members)
        elif pilihan == "4":
            history = data.lihat_riwayat()
            View.display_purchase_history(history)
        elif pilihan == "5":
            View.display_message("Terima kasih! Sampai jumpa.")
            break
        else:
            View.display_message("Pilihan tidak valid! Silakan pilih menu yang tersedia.")

if __name__ == "__main__":
    main()  # Pastikan untuk memanggil fungsi main dengan tanda kurung
```
# Penjelasan Code
Input Data Produk

Saat menjalankan program, pengguna akan diminta untuk memberikan informasi mengenai nama produk, harga, dan stok yang tersedia. Input Data Produk
1. Inisiasi Input: Program memulai dengan menampilkan prompt yang meminta pengguna untuk memasukkan nama produk.
2. Input Nama Produk: Pengguna memasukkan nama produk melalui perangkat input standar (misalnya, keyboard). Nama produk direpresentasikan sebagai string.
3. Validasi Input Nama (Opsional): Sistem dapat menerapkan validasi untuk memastikan nama produk tidak kosong atau memenuhi kriteria tertentu (misalnya, panjang karakter, format).
4. Input Harga Produk: Setelah nama produk diinput, program meminta pengguna untuk memasukkan harga produk. Harga produk direpresentasikan sebagai tipe data numerik (biasanya float atau decimal untuk menangani nilai desimal).
5. Validasi Input Harga (Penting): Validasi sangat disarankan pada tahap ini untuk memastikan input harga berupa angka valid dan biasanya bernilai positif. Penanganan kesalahan (error handling) diperlukan untuk mencegah program berhenti jika input tidak valid.
6. Input Stok Produk: Program meminta pengguna untuk memasukkan jumlah stok produk. Stok direpresentasikan sebagai tipe data integer.
7. Validasi Input Stok (Penting): Validasi juga disarankan untuk input stok, memastikan input berupa angka integer dan biasanya bernilai non-negatif.
8. Penyimpanan Data: Data yang telah diinput (nama, harga, dan stok) disimpan dalam sebuah struktur data yang sesuai.
9. Pengulangan Input: Proses input (langkah 2-8) diulang sampai pengguna memberikan sinyal untuk berhenti. Sinyal ini biasanya berupa input khusus, seperti kata kunci "exit" atau perintah lainnya.
10. Terminasi Input: Setelah pengguna memberikan sinyal berhenti, proses input data diakhiri.
