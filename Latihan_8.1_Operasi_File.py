# Nama File: Latihan8.1.operasi_file.py
# Deskripsi: Belajar 4 mode file (w, a, r+, r) dengan analogi Buku Catatan.

# ==============================================================
# 1. Mode 'w' (Write) -> Membuat dan menulis (Menimpa yang lama)
# Analogi: Membeli buku baru dan mulai menulis di halaman pertama.
# ==============================================================
with open("buku_catatan.txt", "w") as buku:
    buku.write("Baris 1: Aku mulai belajar Python hari ini.\n")
print("Sukses: Mode 'w' berhasil membuat file dan menulis isi pertama!")


# ==============================================================
# 2. Mode 'a' (Append) -> Menambah tulisan di bagian bawah
# Analogi: Melanjutkan tulisan di hari berikutnya tanpa menghapus yang kemarin.
# ==============================================================
with open("buku_catatan.txt", "a") as buku:
    buku.write("Baris 2: Oh, ternyata menambah tulisan itu pakai mode 'a'.\n")
print("Sukses: Mode 'a' berhasil menambahkan tulisan di bawahnya!")


# ==============================================================
# 3. Mode 'r+' (Read + Write) -> Membaca sekaligus menulis
# Analogi: Membaca buku dari awal, lalu menambahkan kesimpulan di akhir.
# ==============================================================
with open("buku_catatan.txt", "r+") as buku:
    buku.read() # Kita "baca" dulu sampai habis agar posisi pulpen turun ke paling bawah
    buku.write("Baris 3: Ini adalah baris tambahan menggunakan mode 'r+'.\n")
print("Sukses: Mode 'r+' berhasil membaca dan menambah tulisan!")


# ==============================================================
# 4. Mode 'r' (Read) -> Hanya untuk membaca
# Analogi: Cuma melihat isi buku, kita tidak boleh memegang pensil.
# ==============================================================
print("\n--- Mari kita buka dan baca seluruh isi bukunya pakai Mode 'r' ---")

with open("buku_catatan.txt", "r") as buku:
    isi_buku = buku.read()
    print(isi_buku) # Menampilkan teks ke layar