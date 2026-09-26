# Deskripsi: Program sangat sederhana untuk menangkap SEMUA jenis error

print("--- Program Bagi-Bagi Angka ---")

try:
    # 1. Kita minta user memasukkan angka
    teks_input = input("Masukkan angka pembagi (coba masukkan huruf atau angka 0): ")

    # 2. Kita coba ubah input menjadi angka (Bisa error kalau user memasukkan huruf)
    angka = int(teks_input)

    # 3. Kita coba membagi angka 100 (Bisa error kalau user memasukkan angka 0)
    hasil = 100 / angka
    print("Berhasil! 100 dibagi", angka, "hasilnya adalah", hasil)

# Inilah kunci dari tugasmu! 
# 'Exception' adalah induk dari semua error. Jadi, error apapun pasti tertangkap di sini.
except Exception as error_nya:
    print("\n[WADUH!] Terjadi kesalahan, tapi program tidak crash/berhenti paksa.")
    print("Alasan error-nya adalah:", error_nya)
    print("Silakan jalankan ulang program dan masukkan angka yang benar.")