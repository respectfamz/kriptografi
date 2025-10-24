while input("Apakah Anda ingin memulai operasi perhitungan? (y/n): ").lower() == 'y':
    ekspresi = input("Masukkan ekspresi matematika : ")

    try:
        hasil = eval(ekspresi)
        print("Hasil dari operasi adalah:", hasil)
    except Exception as e:
        print("Terjadi kesalahan dalam perhitungan:", e)

print("Program selesai. Terima kasih!")
