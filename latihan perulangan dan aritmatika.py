while input("Apakah Anda ingin memulai operasi perhitungan? (y/n): ").lower() == 'y':
    a = input("Masukkan nilai a: ")
    b = input("Masukkan nilai b: ")
    operator = input("Masukkan operator (+, -, *, /): ")
    if operator not in ['+', '-', '*', '/']:
        print("Error: operator tidak valid!")
else:
    ekspresi = a + operator + b
    hasil = eval(ekspresi)

    print("Hasil dari operasi adalah:", hasil)

print("Program selesai. Terima kasih!")
