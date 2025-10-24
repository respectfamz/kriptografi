# Konversi Biner ke Desimal dan Heksadesimal

while input("Apakah Anda ingin memulai operasi konversi? (y/n): ").lower() == 'y':
    try:
        biner = input("Masukkan bilangan biner: ")

        # Pastikan input hanya terdiri dari 0 dan 1
        if all(ch in '01' for ch in biner):
            desimal = int(biner, 2)
            heksadesimal = hex(desimal)[2:].upper()
            print(f"Desimal     : {desimal}")
            print(f"Heksadesimal: {heksadesimal}")
        else:
            print("Input bukan bilangan biner yang valid!")

    except Exception as e:
        print("Terjadi kesalahan dalam perhitungan:", e)

print("Program selesai. Terima kasih!")
