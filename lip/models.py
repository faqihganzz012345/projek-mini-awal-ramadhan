from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, nama, id_user):
        self.nama = nama
        self.__id_user = id_user 

    @property
    def id_user(self):
        return self.__id_user

    @abstractmethod
    def get_info(self):
        pass

class Santri(User):
    def __init__(self, nama, id_user, asrama):
        super().__init__(nama, id_user)
        self.asrama = asrama

    def get_info(self):
        return f"[Santri] {self.nama} | Asrama: {self.asrama}"


class Kitab:
    def __init__(self, judul, kategori, stok_awal):
        self.judul = judul
        self.kategori = kategori
        self.__stok = stok_awal 

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, jumlah_baru):

        if jumlah_baru >= 0:
            self.__stok = jumlah_baru
        else:

            raise ValueError("Maaf, stok kitab ini sudah habis (0).")

    def __str__(self):
        return f"{self.judul:20} | {self.kategori:12} | Stok: {self.__stok}"