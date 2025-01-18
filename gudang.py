class Barang:
    def __init__(self, id_barang, nama, jumlah):
        self.id_barang = id_barang
        self.nama = nama
        self.jumlah = jumlah

    def __repr__(self):
        return f"{self.id_barang} - {self.nama} - {self.jumlah}"


class Gudang:
    def __init__(self):
        self.barang_list = []
        self.stack = []
        self.queue = []

    def tambah_barang(self, id_barang, nama, jumlah):
        if jumlah < 0:
            print("Jumlah tidak boleh negatif.")
            return
        barang = Barang(id_barang, nama, jumlah)
        self.barang_list.append(barang)
        self.stack.append(barang)
        print(f"Barang {nama} ditambahkan.")

    def edit_barang(self, id_barang, nama=None, jumlah=None):
        for barang in self.barang_list:
            if barang.id_barang == id_barang:
                if nama:
                    barang.nama = nama
                if jumlah is not None:
                    if jumlah < 0:
                        print("Jumlah tidak boleh negatif.")
                        return
                    barang.jumlah = jumlah
                print(f"Barang {id_barang} telah diperbarui.")
                return
        print("Barang tidak ditemukan.")

    def hapus_barang(self, id_barang):
        for barang in self.barang_list:
            if barang.id_barang == id_barang:
                self.barang_list.remove(barang)
                print(f"Barang {id_barang} telah dihapus.")
                return
        print("Barang tidak ditemukan.")

    def cari_barang(self, nama):
        hasil_cari = [barang for barang in self.barang_list if nama.lower() in barang.nama.lower()]
        return hasil_cari if hasil_cari else "Barang tidak ditemukan."

    def urutkan_barang(self):
        self.barang_list.sort(key=lambda x: x.nama)
        print("Barang telah diurutkan.")

    def barang_masuk(self):
        if self.stack:
            barang = self.stack.pop()
            self.queue.append(barang)
            print(f"Barang {barang.nama} telah masuk ke antrian keluar.")
        else:
            print("Tidak ada barang dalam stack.")

    def barang_keluar(self):
        if self.queue:
            barang = self.queue.pop(0)
            print(f"Barang {barang.nama} telah keluar dari gudang.")
        else:
            print("Tidak ada barang dalam antrian keluar.")


gudang = Gudang()


gudang.tambah_barang(1, "Laptop", 10)
gudang.tambah_barang(2, "Printer", 5)
gudang.tambah_barang(3, "Keyboard", 20)


print(gudang.cari_barang("Laptop"))


gudang.urutkan_barang()


gudang.barang_masuk()
gudang.barang_keluar()


gudang.edit_barang(1, jumlah=8)
gudang.hapus_barang(2)


print(gudang.barang_list)