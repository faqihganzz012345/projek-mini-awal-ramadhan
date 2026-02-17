from datetime import datetime

class LayananPerpustakaan:
    def __init__(self):
        self.daftar_kitab = []
        self.riwayat_pinjam = []

    def registrasi_kitab(self, kitab_obj):
        self.daftar_kitab.append(kitab_obj)

    def cari_kitab(self, keyword):
        return [k for k in self.daftar_kitab if keyword.lower() in k.judul.lower() 
                or keyword.lower() in k.kategori.lower()]

    def proses_peminjaman(self, peminjam, kitab_target):
        """
        Logika inti peminjaman dengan pencatatan tanggal otomatis
        """
        try:

            kitab_target.stok -= 1
            

            tanggal_sekarang = datetime.now().strftime("%d-%m-%Y %H:%M")
            
            log = {
                "nama": peminjam.nama,
                "kitab": kitab_target.judul,
                "tanggal": tanggal_sekarang
            }
            self.riwayat_pinjam.append(log)
            return True, f"Berhasil! Dipinjam pada {tanggal_sekarang}"
        
        except ValueError as e:
            return False, str(e)

    def proses_pengembalian(self, judul_kitab):
        for kitab in self.daftar_kitab:
            if kitab.judul.lower() == judul_kitab.lower():
                kitab.stok += 1
                return True, f"Terima kasih, kitab '{kitab.judul}' telah kembali."
        return False, "Judul kitab tidak ditemukan di sistem."