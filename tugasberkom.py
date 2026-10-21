# Program Kasir Warung/Minimarket Mini untuk Mahasiswa ITB
# Fitur: diskon saat membeli, pajak saat membayar cashless

# ===== DATA MENU (Dibuat dalam bentuk list supaya sintaks lebih rapih) =====
menu_warung = [
    # Makanan
    ("Nasi Goreng", 12000),
    ("Ayam Geprek", 15000),
    ("Sate Taichan", 14000),
    ("Nasi Ayam Teriyaki", 13000),
    ("Nasi Bakar", 12000),
    
    # Minuman
    ("Air Mineral", 6000),
    ("Es Teh", 5000),
    ("Es Jeruk", 6000),
    ("Es Kopi Susu", 10000),

    # Dessert
    ("Roti Bakar", 8000),
    ("Dubai Chewy Cookie", 12000),
    ("Mochi", 8000)
]

# ===== Aturan Diskon dan Pajak =====
batas_diskon = 50000    # Diskon didapatkan jika total harga >= batas_diskon
diskon = 5 / 100
pajak = 3 / 100         # Pajak dikenakan jika pembayaran menggunakan cashless

print("=" * 40)
print("Selamat datang di Warung Mahasiswa ITB!".center(40))
print("Warung ini bersifat Self-Service yaa!!!".center(40))
print("Jadi pilih menu sesuai budgetmu!!!".center(40))
print("=" * 40)

# Periksa total uang yang dimiliki User
uang = float(input("\nMasukkan uang yang Anda miliki: "))
while uang < 1:
    if uang < 1:
       uang = float(input("Mohon maaf, tolong masukkan uang yang Anda miliki dengan benar: "))
    else:
        break

# Jalankan program membeli pesanan

# Print Menu
print("""\nBerikut adalah Menu yang kami sajikan di Warung Mahasiswa ITB:
      
      A. Makanan
        1. Nasi Goreng          (Rp12.000)
        2. Ayam Geprek          (Rp15.000)
        3. Sate Taichan         (Rp14.000)
        4. Nasi Ayam Teriyaki   (Rp13.000)
        5. Nasi Bakar           (Rp12.000)
        
      B. Minuman
        6. Air Mineral          (Rp6.000)
        7. Es Teh               (Rp5.000)
        8. Es Jeruk             (Rp6.000)
        9. Es Kopi Susu         (Rp10.000)
        
      C. Dessert
        10. Roti Bakar           (Rp8.000)
        11. Dubai Chewy Cookie   (Rp12.000)
        12. Mochi                (Rp8.000)
      """)

pesanan = []
pesanan_selesai = False
total_harga = 0

# Perulangan pemesanan
while not pesanan_selesai:
  pesan = int(input("Pilih menu yang ingin anda pesan: "))
  jumlah = int(input(f"Berapa banyak yang ingin Anda pesan: "))
  
  nama_menu = menu_warung[pesan - 1][0]
  harga_menu = menu_warung[pesan - 1][1]
  
  # Cek menu sudah dipesan atau belum
  menu_ditemukan = False
  
  for i in range(len(pesanan)):
    if pesanan[i][0] == nama_menu:
      pesanan[i] = (nama_menu, pesanan[i][1] + jumlah)
      menu_ditemukan = True
      break
  
  # Jika pesanan belum ada, tambahkan sebagai pesanan baru
  if not menu_ditemukan:
    pesanan.append((nama_menu, jumlah))
    
  harga_pesanan = harga_menu * jumlah
  total_harga += harga_pesanan
  
  while not pesanan_selesai:
    checking = input("\nApakah ada yang ingin Anda pesan lagi? (y/n): ").lower()
    if checking == "y":
      break
    elif checking == "n":
      
      print("\nPesanan sementara Anda:")
      print("-" * 35)
      
      i = 1
      
      for nama, banyak_pesanan in pesanan:
        print(f"{i}. {nama} sebanyak {banyak_pesanan}")
        i += 1
        
      print("-" * 35)
      print(f"Total harga: Rp{total_harga:,}\n".replace(",", "."))
      pesanan_selesai = True
      break
    else:
      print("Tolong pilih jawaban antara Y (Yes) atau N (No)")
      continue

while True:
  ganti_menu = input("Apakah Anda ingin mengubah pesanan Anda? (y/n): ").lower()
  
  if ganti_menu == "y":
    # Tampilkan pesanan sementara
    print("\nDaftar pesanan Anda:")
    print("-" * 35)
    
    j = 1
    
    for nama, banyak_pesanan in pesanan:
      print(f"{j}. {nama} sebanyak {banyak_pesanan}")
      j += 1
      
    print("-" * 35)
    
    no_pesanan = int(input("Pilih nomor pesanan yang ingin diubah: ")) - 1
    
    if 0 <= no_pesanan < len(pesanan):
      nama_lama, jumlah_lama = pesanan[no_pesanan]
      
      # Cari harga dari menu lama
      for nama, harga in menu_warung:
        if nama == nama_lama:
          harga_lama = harga
          break
      
      print("\nApa yang ingin Anda ubah?")
      print("1. Mengubah menu")
      print("2. Mengubah jumlah pesanan")
      
      pilihan_ubah = input("Silahkan pilih opsi 1 atau 2: ")

      # Pilihan 1: Mengubah Menu
      if pilihan_ubah == "1":
        
        # Keluarkan harga pesanan lama dari total
        total_harga -= harga_lama *  jumlah_lama
        print("\nDaftar Menu:")
        
        k = 1
        
        for nama, harga in menu_warung:
          print(f"{k}. {nama} - Rp{harga:,}".replace(",", "."))
          k += 1

        menu_baru = int(input("\n Pilih nomor untuk menu pengganti: ")) - 1
        
        if 0 <= menu_baru < len(menu_warung):
          nama_baru, harga_baru = menu_warung[menu_baru]
          
          # Jumlah pesanan untuk menu baru
          jumlah_baru = int(input(f"Berapa banyak {nama_baru} yang ingin dipesan? "))
          
          # Ganti menu dan jumlah pesanan lama
          pesanan[no_pesanan] = (nama_baru, jumlah_baru)
          
          # Tambahkan harga dari pesanan baru
          total_harga += harga_baru * jumlah_baru
          
          print("\nMenu berhasil diubah!")
          
          print("\nData Pesanan Saat Ini:")
          
          print("-" * 35)
          l = 1
          for nama, jumlah in pesanan:
              print(f"{l}. {nama} sebanyak {jumlah}")
              l += 1

          print("-" * 35)
          print(f"Total harga: Rp{total_harga:,}\n".replace(",", "."))

        else:
          # Kembalikan harga lama jika nomor menu yang diberikan tidak valid
          total_harga += harga_lama * jumlah_lama
          print("Nomor menu tidak valid")
          
      # Mengubah jumlah pesanan
      elif pilihan_ubah == "2":
        print(f"\nMenu yang dipilih: {nama_lama}")
        print(f"Jumlah saat ini: {jumlah_lama}")
        
        jumlah_baru = int(input("Masukkan jumlah pesanan yang baru: "))
        
        if jumlah_baru >= 0:
          
          # Hitung selisih jumlah pesanan
          selisih = jumlah_baru - jumlah_lama
          
          # Update jumlah pesanan pada daftar pesanan
          pesanan[no_pesanan] = (nama_lama, jumlah_baru)
          
          # Update total harga
          total_harga += selisih * harga_lama

          # Hapus menu jika jumlahnya 0
          if jumlah_baru == 0:
            pesanan.pop(no_pesanan)
          print("\nJumlah pesanan berhasil diubah!")
          
        else:
          print("Jumlah pesanan tidak boleh negatif")
          
      else:
        print("Pilihan tidak valid.")
      
    else:
      print("Nomor pesanan yang dipilih tidak valid.")
  elif ganti_menu == "n":
    break
  else:
    print("\nTolong pilih jawaban antara Y (Yes) atau N (No).")
    continue
          
# Perhitungan Harga
print("\nRincian pembayaran:")
print("-" * 35)

m = 1

for nama, jumlah in pesanan:
    print(f"{m}. {nama} sebanyak {jumlah}")
    m += 1

print("-" * 35)
print(f"Total harga awal: Rp{total_harga:,}".replace(",", "."))

# ===== PEMBAYARAN DAN PEMERIKSAAN ANGGARAN =====
# Pilih metode pembayaran
while True:
    metode_pembayaran = input("\nPilih metode pembayaran (cash/cashless): ").lower()
    if metode_pembayaran in ["cash", "cashless"]:
        break

    print("Pilihan tidak valid. Masukkan cash atau cashless.")

# Periksa total belanja 
while True:
    # Hitung ulang total harga berdasarkan daftar pesanan
    total_harga = 0
    for nama, jumlah in pesanan:
        for nama_menu, harga_menu in menu_warung:
            if nama == nama_menu:
                total_harga += harga_menu * jumlah
                break

    # Hitung diskon
    if total_harga >= batas_diskon:
        diskon_nominal = total_harga * diskon
    else:
        diskon_nominal = 0

    subtotal = total_harga - diskon_nominal

    # Hitung pajak jika cashless
    if metode_pembayaran == "cashless":
        pajak_nominal = subtotal * pajak
    else:
        pajak_nominal = 0

    total_bayar = subtotal + pajak_nominal
    kembalian = uang - total_bayar

    # Tampilkan rincian pembayaran
    print("\n" + "=" * 35)
    print("RINCIAN PEMBAYARAN".center(35))
    print("=" * 35)

    print(f"Total harga awal: Rp{total_harga:,.0f}".replace(",", "."))
    print(f"Diskon (5%): Rp{diskon_nominal:,.0f}".replace(",", "."))
    print(f"Subtotal: Rp{subtotal:,.0f}".replace(",", "."))

    if metode_pembayaran == "cashless":
        print(f"Pajak (3%): Rp{pajak_nominal:,.0f}".replace(",", "."))

    print(f"Total pembayaran: Rp{total_bayar:,.0f}".replace(",", "."))
    print(f"Anggaran Anda: Rp{uang:,.0f}".replace(",", "."))
    print(f"Sisa anggaran Anda: Rp{kembalian:,.0f}".replace(",", "."))
    
    # Periksa apakah uang cukup
    if uang >= total_bayar:

        if metode_pembayaran == "cash":
            print("\nAnggaran Anda mencukupi!")
            kembalian = uang - total_bayar
            print(f"Kembalian: Rp{kembalian:,.0f}".replace(",", "."))

        print("\nPemabayaran Berhasil! Terimakasih Telah Berbelanja di Warung Mahasiswa ITB!")
        break

    # Jika uang kurang
    kekurangan = total_bayar - uang

    print("\nMaaf, uang Anda tidak cukup.")
    print(f"Kekurangan: Rp{kekurangan:,.0f}".replace(",", "."))

    pilihan = input(
        "\nApakah Anda ingin mengubah pesanan agar sesuai anggaran? (y/n): "
    ).lower()

    if pilihan == "n":
        print("Silakan sesuaikan anggaran atau pesanan Anda sebelum membayar.")
        break

    elif pilihan == "y":

        # Tampilkan daftar pesanan
        print("\nDaftar pesanan Anda:")
        print("-" * 35)

        for i, (nama, jumlah) in enumerate(pesanan, start=1):
            print(f"{i}. {nama} sebanyak {jumlah}")

        print("-" * 35)

        # Pilih pesanan yang ingin diubah
        no_pesanan = int(input("Pilih nomor pesanan yang ingin diubah: ")) - 1

        if not 0 <= no_pesanan < len(pesanan):
            print("Nomor pesanan tidak valid.")
            continue

        nama_lama, jumlah_lama = pesanan[no_pesanan]

        # Cari harga menu lama
        for nama_menu, harga_menu in menu_warung:
            if nama_menu == nama_lama:
                harga_lama = harga_menu
                break

        print("\nApa yang ingin Anda ubah?")
        print("1. Mengubah menu")
        print("2. Mengubah jumlah pesanan")

        pilihan_ubah = input("Pilih opsi 1 atau 2: ")

        if pilihan_ubah == "1":

            # Tampilkan menu pengganti
            print("\nDaftar menu:")

            for i, (nama, harga) in enumerate(menu_warung, start=1):
                print(f"{i}. {nama} - Rp{harga:,.0f}".replace(",", "."))

            menu_baru = int(input("Pilih nomor menu pengganti: ")) - 1

            if not 0 <= menu_baru < len(menu_warung):
                print("Nomor menu tidak valid.")
                continue

            nama_baru, harga_baru = menu_warung[menu_baru]

            jumlah_baru = int(input(f"Berapa banyak {nama_baru} yang ingin dipesan? "))

            if jumlah_baru < 0:
                print("Jumlah pesanan tidak boleh negatif.")
                continue

            # Hapus pesanan lama
            pesanan.pop(no_pesanan)

            # Gabungkan jika menu pengganti sudah ada
            if jumlah_baru > 0:
                menu_ditemukan = False

                for i in range(len(pesanan)):
                    if pesanan[i][0] == nama_baru:
                        pesanan[i] = (
                            nama_baru,
                            pesanan[i][1] + jumlah_baru
                        )
                        menu_ditemukan = True
                        break

                if not menu_ditemukan:
                    pesanan.append((nama_baru, jumlah_baru))

            print("Menu berhasil diubah!")

        elif pilihan_ubah == "2":

            print(f"\nMenu: {nama_lama}")
            print(f"Jumlah saat ini: {jumlah_lama}")

            jumlah_baru = int(input("Masukkan jumlah pesanan yang baru: "))

            if jumlah_baru < 0:
                print("Jumlah pesanan tidak boleh negatif.")
                continue

            if jumlah_baru == 0:
                pesanan.pop(no_pesanan)
            else:
                pesanan[no_pesanan] = (nama_lama, jumlah_baru)

            print("Jumlah pesanan berhasil diubah!")

        else:
            print("Pilihan tidak valid.")
            continue

        # Tampilkan pesanan setelah perubahan
        print("\nData pesanan saat ini:")
        print("-" * 35)

        for i, (nama, jumlah) in enumerate(pesanan, start=1):
            print(f"{i}. {nama} sebanyak {jumlah}")

        print("-" * 35)

        # Kembali ke awal while untuk menghitung ulang pembayaran
    else:
        print("Masukkan y atau n.")