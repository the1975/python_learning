tas = ["Buku", "Pensil", "Penggaris"]
print("Isi tas awal:", tas)

# Operasi 1: Tambah barang (append akan menaruhnya di paling belakang)
tas.append("Penghapus")
print("Setelah ditambah penghapus:", tas)

# Operasi 2: Melihat barang urutan pertama (komputer mulai berhitung dari 0)
print("Barang paling pertama adalah:", tas[0])

# Operasi 3: Membuang barang
tas.remove("Pensil")
print("Setelah pensil dibuang:", tas)