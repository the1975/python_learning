# Latihan 2.1 Operator
# Program untuk menghitung harga setelah diskon

harga_awal = float(input("Masukkan harga awal: "))
diskon = float(input("Masukkan diskon (%): "))

# Mengubah persen ke bentuk desimal
diskon = diskon / 100

# Menghitung harga akhir
harga_akhir = harga_awal - (harga_awal * diskon)

# Menampilkan hasil
print("Harga setelah diskon =", harga_akhir)
