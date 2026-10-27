#variabel dan tipe data


print('============Nilai Mahasiswa=============')

#nama_mhs = "chacha" 
#kelas = "C1"

nalgoritma = 90
nagama = 95
bahasaindonesia = 80
BasisData = 85
nlogikainformatika = 92
npancasila = 87
nbahasainggris = 80

NamaMhs = input("Masukkan nama mahasiswa : ")
NilaiAlgoritma = int(input("Masukkan nilai algoritma : "))
NilaiAgama = int(input("Masukkan nilai agama : "))
NilaiBahasaIndonesia = int(input("Masukkan nilai bahasa indonesia : "))
NilaiBasisData = int(input("Masukkan nilai basis data : "))
NilaiLogikaInformatika = int(input("Masukkan nilai logika informatika : "))
NilaiPancasila = int(input("Masukkan nilai pancasila : "))
NilaiBahasaInggris = int(input("Masukkan nilai bahasa inggris : "))

Rata_rata = ( NilaiAlgoritma + NilaiAgama + NilaiBahasaIndonesia + NilaiBasisData + NilaiLogikaInformatika + NilaiPancasila + NilaiBahasaInggris) / 7
#print(rata_rata)
#nilai = int(input("Masukkan nilai : "))

#penentuan lulus atau tidak
if Rata_rata >= 80 and Rata_rata <= 100:
    print("Nilai  : A")
elif Rata_rata >= 70 and Rata_rata < 80:
    print("Nilai  : B")
elif Rata_rata >= 50 and Rata_rata < 70:
    print("Nilai  : C")
elif Rata_rata >= 30 and Rata_rata < 50:
    print("Nilai  : D")
else :
    #cukup menampilkan hasil
    #maka
    print("Nilai  : E")