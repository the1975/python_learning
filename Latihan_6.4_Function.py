# Deskripsi: Program dengan implementasi Parameter Dinamis (*args).

def hitung_total_belanja(*harga_barang):
    # Parameter *harga_barang akan menampung semua input dalam bentuk Tuple
    # Fungsi sum() digunakan untuk menjumlahkan semua angka di dalam Tuple tersebut
    total = sum(harga_barang)

    print("Daftar harga yang dimasukkan:", harga_barang)
    print("Total belanja Anda adalah   : Rp", total)

# Memanggil function dengan jumlah argumen (input) yang berbeda-beda
print("Pelanggan 1:")
hitung_total_belanja(15000, 20000, 5000)

print("\nPelanggan 2:")
hitung_total_belanja(50000, 120000) # Hanya 2 argumen