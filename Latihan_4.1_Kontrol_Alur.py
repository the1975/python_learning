# Mengambil input bulan lahir dari pengguna dan mengubahnya menjadi tipe data integer
bulan_lahir = int(input("masukkan bulan lahir saya: "))

# Memulai perulangan for dari angka 1 hingga 100
# Menggunakan range(1, 101) karena perulangan akan berhenti tepat sebelum angka 101
for i in range (1,101):

  # Mengecek apakah angka saat ini (i) adalah kelipatan dari bulan lahir
  if i % bulan_lahir == 0:
    print("bulan")
  else:
    print(i)