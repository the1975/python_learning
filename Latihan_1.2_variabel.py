nama = str(input("Siapa nama adik anda?"))
umur = int(input("Berapa umur adik anda?"))
berat = float(input("Berapa berat badan adik anda?"))
gender = bool(input("Apakah adik anda laki laki?"))

#sintaks (input) digunakan untuk menginput atau memasukan data kedalam variabel
#input bila tidak diubah tipe datanya akan selalu berupa tipe data string
#sintaks int, float, dan bool digunakan untuk merubah tipe data yang sudah di input menjadi data yang sesuai dengan sintaksnya
#str = string, int = integer, float = float, bool = boolean

print("Nama adik saya adalah", nama)
print("Saat ini adik saya berusia", umur, "tahun")
print("Berat badannya", berat, "Kg")
print("Dia", gender, "berkelamin laki-laki")
