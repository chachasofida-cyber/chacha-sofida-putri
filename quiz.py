nama =input("masukan nama mahasiswa :    ")

if nama == "Andi" :
    target =70

elif nama == "Budi":
    target =75

elif nama == "Citra":
    target =80

else :
    target = 0  

if target == 0:
    print("Nama mahasiswa tidak ditemukan dalam daftar")

else :
    print("Nama mahasiswa :", nama)
    print("Target Nilai :", target)

    percobaan = 0
    lulus = False

while percobaan < 3 and not lulus :
    nilai =int(input("Masukkan nilai ujian : "))
    percobaan += 1
    print("Percobaan ke-", percobaan)

    if nilai >= target:
        lulus = True
        print("Selamat", nama, "Anda Lulus")
    else:
        print("Maaf", nama, "Anda belum mencapai target nilai. Silakan coba lagi.")

    if lulus :
        print(nama,"Anda dinyatakan LULUS setelah", percobaan, " kali percobaan.")
    else :
        print(nama,"Anda dinyatakan TIDAK LULUS setelah 3 kali percobaan.")
