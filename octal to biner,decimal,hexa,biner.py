# Konversi Biner ke Desimal dan Hexadesimal
while input("Apakah Anda ingin memulai operasi konversi? (y/n): ").lower() == 'y':
    try:
        octal = input("Masukkan bilangan octal: ")

# Pastikan input hanya terdiri dari 0 dan 1
        if all(ch in '01234567' for ch in octal):
            desimal = int(octal, 8)
            biner = bin(desimal)[2:]
            heksadesimal = hex(desimal)[2:].upper()
            print(f"Desimal : {desimal}")
            print(f"biner: {biner}")
            print(f"Heksadesimal: {heksadesimal}")
    
        else:
            print("Input bukan bilangan biner yang valid!")
    except Exception as e:
        print("Terjadi kesalahan dalam perhitungan:", e)

print("Program selesai. Terima kasih!")
