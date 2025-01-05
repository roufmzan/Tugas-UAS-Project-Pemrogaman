# Tugas-UAS-Project-Pemrogaman
# DATA DIRI
## Nama : Sheila Antica Oktaviani
## Kelas : TI.24.A1
## NIM : 312410002
## Program akan meminta masukan data yang terdiri dari nama produk, harga produk, dan jumlah stok produk.
![output UAS project](https://github.com/user-attachments/assets/3a81cfd1-d824-49ad-95c1-c78e24f1b830)
## Class Data
## _init.py
```Python
# class_data/__init__.py
from .class_data import Produk
```
## class_data.py
```Python
# class_data/class_data.py
class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok
```
## Class Process
## _init.py
```Python
# class_process/__init__.py
from .class_process import ProdukProcess
```
## class_process.py
```Python
# class_process/class_process.py
from class_data import Produk

class ProdukProcess:
    def __init__(self):
        self.produk_list = []

    def tambah_produk(self, nama, harga, stok):
        if not nama:
            raise ValueError("Nama produk tidak boleh kosong.")
        if harga <= 0:
            raise ValueError("Harga produk harus lebih besar dari 0.")
        if stok < 0:
            raise ValueError("Stok produk tidak boleh negatif.")
        
        produk = Produk(nama, harga, stok)
        self.produk_list.append(produk)

    def get_produk(self):
        return self.produk_list
```
## Class View
##  _init.py
```Python
# class_view/__init__.py
from .class_view import ProdukView
```
## class_view.py
```Python
# class_view/class_view.py
class ProdukView:
    def tampilkan_produk(self, produk_list):
        print(f"{'Nama Produk':<20} {'Harga':<10} {'Stok':<10}")
        print("-" * 40)
        for produk in produk_list:
            print(f"{produk.nama:<20} {produk.harga:<10.2f} {produk.stok:<10}")
```
## main.py
```Python
from class_data import Produk
from class_process import ProdukProcess
from class_view import ProdukView

def main():
    process = ProdukProcess()  # Membuat instance dari ProdukProcess
    view = ProdukView()        # Membuat instance dari ProdukView

    while True:
        try:
            # Meminta input nama produk
            nama = input("Masukkan nama produk (atau ketik 'exit' untuk keluar): ")
            if nama.lower() == 'exit':
                break
            
            # Meminta input harga produk
            harga = float(input("Masukkan harga produk: "))
            
            # Meminta input stok produk
            stok = int(input("Masukkan stok produk: "))
            
            # Menambahkan produk ke dalam daftar
            process.tambah_produk(nama, harga, stok)
        except ValueError as e:
            print(f"Error: {e}")

    # Tampilkan data produk
    print("\nDaftar Produk:")
    view.tampilkan_produk(process.get_produk())

if __name__ == "__main__":
    main()
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
