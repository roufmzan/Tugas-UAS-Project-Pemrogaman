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