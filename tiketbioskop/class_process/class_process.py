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