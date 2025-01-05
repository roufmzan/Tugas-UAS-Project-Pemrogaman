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