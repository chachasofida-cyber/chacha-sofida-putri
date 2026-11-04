# ==========================================
#       PROGRAM APLIKASI KASIR RESTORAN
# ==========================================

# Daftar menu makanan
menu = {
    1: ("Nasi Goreng", 25000),
    2: ("Mie Ayam", 15000),
    3: ("Ayam Geprek", 20000),
    4: ("Sate Ayam", 30000),
    5: ("Bakso", 18000)
}

# Variabel untuk menyimpan total belanja
total = 0

# Menyimpan daftar pesanan
pesanan = []


# ==========================================
#              MULAI PROGRAM
# ==========================================

print("=" * 45)
print("       SELAMAT DATANG DI RESTORAN")
print("          APLIKASI KASIR RESTORAN")
print("=" * 45)
nama = input("Nama Pelanggan : ")
nomor = int(input("Nomor Meja     : "))
# ==========================================
#             TAMPILKAN MENU
# ==========================================

while True:

    print("\n========== DAFTAR MENU MAKANAN ==========")

    for nomor, (nama, harga) in menu.items():
        print(f"{nomor}. {nama:<15} : Rp{harga:,}".replace(",", "."))

    print("0. Selesai Memilih")
    print("=" * 45)

    # Input pilihan menu
    try:
        pilihan = int(input("Pilih menu (0-5): "))

        # Jika memilih 0, maka pemesanan selesai
        if pilihan == 0:
            break

        # Memeriksa pilihan menu
        if pilihan not in menu:
            print("Pilihan tidak tersedia! Silakan pilih kembali.")
            continue

        # Input jumlah pesanan
        jumlah = int(input("Masukkan jumlah pesanan: "))

        if jumlah <= 0:
            print("Jumlah pesanan harus lebih dari 0!")
            continue

        # Mengambil nama dan harga menu
        nama, harga = menu[pilihan]

        # Menghitung subtotal
        subtotal = harga * jumlah

        # Menambahkan subtotal ke total belanja
        total += subtotal

        # Menyimpan detail pesanan
        pesanan.append((nama, harga, jumlah, subtotal))

        print("\nPesanan berhasil ditambahkan!")
        print(f"Menu       : {nama}")
        print(f"Jumlah     : {jumlah}")
        print(f"Subtotal   : Rp{subtotal:,}".replace(",", "."))

    except ValueError:
        print("Input harus berupa angka!")


# ==========================================
#             MENGHITUNG DISKON
# ==========================================

print("\n" + "=" * 45)
print("             STRUK PEMBAYARAN")
print("=" * 45)

# Menghitung diskon
if total > 50000:
    diskon = total * 20 / 100
else:
    diskon = 0

# Menghitung total pembayaran
total_bayar = total - diskon


# ==========================================
#          MENAMPILKAN STRUK
# ==========================================

if total == 0:
    print("Tidak ada pesanan.")
else:
    print("\nDaftar Belanja:")

    for nama, harga, jumlah, subtotal in pesanan:
        print(f"\n{nama}")
        print(f"  {jumlah} x Rp{harga:,}".replace(",", "."))
        print(f"  Subtotal: Rp{subtotal:,}".replace(",", "."))

    print("\n" + "-" * 45)
    print(f"Total Belanja : Rp{total:,.0f}".replace(",", "."))
    print(f"Diskon        : Rp{diskon:,.0f}".replace(",", "."))
    print(f"Potongan      : {20 if diskon > 0 else 0}%")
    print("-" * 45)
    print(f"TOTAL BAYAR   : Rp{total_bayar:,.0f}".replace(",", "."))
    print("=" * 45)

    print("       TERIMA KASIH TELAH BERBELANJA!")
    print("             SELAMAT MENIKMATI")
    print("=" * 45)
