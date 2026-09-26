# Deskripsi: Program dengan implementasi Function menggunakan Keyword Argument.

def profil_mahasiswa(nama, jurusan, kota_asal):
    # Menampilkan profil berdasarkan parameter yang diberikan
    print(f"Nama Mahasiswa : {nama}")
    print(f"Jurusan        : {jurusan}")
    print(f"Kota Asal      : {kota_asal}\n")

# 1. Pemanggilan normal (harus urut)
print("Pemanggilan Normal:")
profil_mahasiswa("Budi", "Sistem Informasi", "Kediri")

# 2. Pemanggilan dengan Keyword Argument (urutan boleh acak)
print("Pemanggilan Keyword Argument:")
profil_mahasiswa(kota_asal="Kediri", nama="Budi", jurusan="Sistem Informasi")