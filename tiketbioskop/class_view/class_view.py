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