# Nama File: Latihan3.1.kontrol_alur.py
# Deskripsi: Program untuk mengelompokkan generasi berdasarkan tahun lahir
print("--- Program Pengelompokan Generasi ---\n")
# Mengambil input tahun lahir dari user
# Kita menggunakan int() untuk memastikan input yang masuk berupa angka bulat
tahun_lahir = int(input("Masukkan tahun lahir Anda: "))

# Struktur Kontrol Alur untuk menentukan kategori generasi
if 1928 <= tahun_lahir <= 1945:
    print("Generasi : Silent Generation")
    print("Deskripsi: Tumbuh selama Depresi Besar dan Perang Dunia II, dikenal pekerja keras, sabar, dan hemat.")

elif 1946 <= tahun_lahir <= 1964:
    print("Generasi : Baby Boomers")
    print("Deskripsi: Lahir setelah Perang Dunia II, mengalami lonjakan kelahiran dan fokus pada pencapaian personal.")

elif 1965 <= tahun_lahir <= 1980:
    print("Generasi : Generasi X")
    print("Deskripsi: Dikenal mandiri, tumbuh di masa peralihan teknologi tradisional ke digital (komputer/internet).")

elif 1981 <= tahun_lahir <= 1996:
    print("Generasi : Generasi Y / Milenial")
    print("Deskripsi: Generasi yang melek teknologi (digital natives) dan peduli isu sosial.")

elif 1997 <= tahun_lahir <= 2012:
    print("Generasi : Generasi Z")
    print("Deskripsi: Tumbuh langsung di dunia internet dan teknologi canggih (iGeneration), sangat terhubung secara digital.")

elif 2013 <= tahun_lahir <= 2024:
    print("Generasi : Generasi Alpha")
    print("Deskripsi: Generasi pertama yang sepenuhnya lahir di abad ke-21, sangat dipengaruhi teknologi cerdas sejak kecil.")

elif 2025 <= tahun_lahir <= 2039:
    print("Generasi : Generasi Beta")
    print("Deskripsi: Generasi mendatang yang diprediksi akan melanjutkan keterhubungan digital tingkat lanjut.")

else:
    # Jika tahun yang dimasukkan di luar rentang yang ditentukan
    print("Tahun lahir tidak terdefinisi dalam kategori generasi ini.")