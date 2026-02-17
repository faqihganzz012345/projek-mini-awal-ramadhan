from models import Santri, Kitab
from services import LayananPerpustakaan

def run():

    perpus = LayananPerpustakaan()
    perpus.registrasi_kitab(Kitab("Fathul ali", "Fiqh", 2))
    perpus.registrasi_kitab(Kitab("Aqidatuna", "Aqidah", 2))
    perpus.registrasi_kitab(Kitab("Jurumiyah", "Nahwu", 3))


    santri_aktif = Santri("Ahmad Zubair", "S-001", "Ibnu tayyib")

    while True:
        print(f"\n{'='*35}")
        print(f"     SISTEM PERPUSTAKAAN KITAB    ")
        print(f"{'='*35}")
        print(f"Login: {santri_aktif.get_info()}")
        print("-" * 25)
        print("1. Cari Kitab")
        print("2. Pinjam Kitab")
        print("3. Kembalikan Kitab")
        print("4. Lihat Log Peminjaman")
        print("5. Keluar")
        
        pilihan = input("\nPilih Menu (1-5): ")

        if pilihan == "1":
            key = input("Masukkan Judul/Kategori: ")
            hasil = perpus.cari_kitab(key)
            print(f"\n{'JUDUL':10} | {'KATEGORI':7} | STOK")
            for k in hasil: print(k)

        elif pilihan == "2":
            judul = input("Ketik judul kitab yang ingin dipinjam: ")
            hasil_cari = perpus.cari_kitab(judul)
            
            if hasil_cari:
                kitab_terpilih = hasil_cari[0]

                tanya = input(f"Pinjam '{kitab_terpilih.judul}'? (iya/tidak): ").lower()
                
                if tanya == "iya":
                    sukses, pesan = perpus.proses_peminjaman(santri_aktif, kitab_terpilih)
                    print(f"STATUS: {pesan}")
                else:
                    print("Peminjaman dibatalkan.")
            else:
                print("Kitab tidak ditemukan.")

        elif pilihan == "3":
            judul = input("Judul kitab yang dikembalikan: ")
            sukses, pesan = perpus.proses_pengembalian(judul)
            print(f"STATUS: {pesan}")

        elif pilihan == "4":
            print("\n--- RIWAYAT TIDAK DI TEMUKAN ---")
            for log in perpus.riwayat_pinjam:
                print(f"[{log['tanggal']}] {log['nama']} -> {log['kitab']}")

        elif pilihan == "5":
            print("Syukron! Sistem dimatikan.")
            break
        else:
            print("Pilihan menu salah!")

if __name__ == "__main__":
    run()