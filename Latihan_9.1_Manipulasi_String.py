# Deskripsi: Program implementasi berbagai operasi manipulasi string di Python.

print("=== PROGRAM MANIPULASI STRING ===\n")

# 1. Mendefinisikan String
teks_utama = "Belajar Python itu Menyenangkan"
teks_tambahan = "Sekali"
print(f"Teks Awal: '{teks_utama}'")

# 2. Menghitung Panjang String (len)
panjang_teks = len(teks_utama)
print(f"\n1. Panjang string: {panjang_teks} karakter (termasuk spasi)")

# 3. Penggabungan (Concatenation) menggunakan '+'
gabungan = teks_utama + " " + teks_tambahan
print(f"2. Penggabungan  : {gabungan}")

# 4. Pengulangan String (Repetition) menggunakan '*'
ulang_teks = "Hore! " * 3
print(f"3. Pengulangan   : {ulang_teks}")

# 5. Indexing (Mengambil satu karakter berdasarkan urutan/indeks)
# Ingat: Komputer mulai menghitung dari angka 0
huruf_pertama = teks_utama[0]
huruf_terakhir = teks_utama[-1]  # -1 mengambil karakter paling belakang
print(f"4. Indexing      : Huruf pertama '{huruf_pertama}', huruf terakhir '{huruf_terakhir}'")

# 6. Slicing (Memotong bagian string)
# Format: teks[awal:akhir] -> akhir tidak diikutkan
potong_kata = teks_utama[8:14]  # Mengambil kata "Python"
print(f"5. Slicing       : '{potong_kata}'")

# 7. Formatting Huruf (Upper, Lower, Title)
huruf_besar = teks_utama.upper()      # SEMUA JADI KAPITAL
huruf_kecil = teks_utama.lower()      # semua jadi kecil
huruf_judul = teks_utama.title()      # Huruf Awal Setiap Kata Kapital
print(f"6. Huruf Besar   : {huruf_besar}")
print(f"7. Huruf Kecil   : {huruf_kecil}")

# 8. Menghapus Karakter Kosong / Spasi berlebih (Strip)
teks_kotor = "   Banyak spasi di kiri dan kanan   "
teks_bersih = teks_kotor.strip()
print(f"8. Fungsi Strip  : '{teks_kotor}' menjadi '{teks_bersih}'")

# 9. Mengganti Kata (Replace)
# Format: teks.replace(kata_lama, kata_baru)
ganti_kata = teks_utama.replace("Menyenangkan", "Mudah")
print(f"9. Fungsi Replace: '{ganti_kata}'")

# 10. Memecah String menjadi List (Split)
# Kita pecah berdasarkan spasi
daftar_kata = teks_utama.split(" ")
print(f"10. Fungsi Split : {daftar_kata}")

# 11. Menggabungkan List menjadi String (Join)
# Kita gabungkan list tadi menggunakan tanda strip (-)
gabung_kembali = "-".join(daftar_kata)
print(f"11. Fungsi Join  : {gabung_kembali}")