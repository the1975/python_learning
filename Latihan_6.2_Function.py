# Deskripsi: Program dengan implementasi Function dengan Parameter dan Return.

def hitung_pangkat(angka, pangkat):
    # Parameter 'angka' dan 'pangkat' digunakan untuk proses perhitungan
    hasil = angka ** pangkat

    # Mengembalikan nilai hasil perhitungan agar bisa digunakan di luar function
    return hasil

# Memanggil function dengan memasukkan angka 3 dan pangkat 4
hasil_akhir = hitung_pangkat(3, 4)

# Menampilkan hasil yang dikembalikan oleh function
print("Hasil 3 pangkat 4 adalah:", hasil_akhir)