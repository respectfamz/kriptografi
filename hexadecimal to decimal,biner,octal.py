while input("Apakah Anda ingin memulai operasi konversi? (y/n): ").lower() == 'y':
    try:
        hexa = input("Masukkan bilangan hexa: ")

# Pastikan input hanya terdiri dari 0 dan 1
        if all(ch in '0123456789ABCDEF' for ch in hexa):
            desimal = int(hexa, 16)
            biner = bin(desimal)[2:]
            oktal = oct(desimal)[2:]
            print(f"Desimal: {desimal}")
            print(f"Biner  : {biner}")
            print(f"Oktal  : {oktal}")
        else:
            print("Input bukan bilangan biner yang valid!")
    except Exception as e:
        print("Terjadi kesalahan dalam perhitungan:", e)

print("Program selesai. Terima kasih!")