X = 'Y'

while X == 'Y':
    print('1. Penjumlahan')
    print('2. Pengurangan')
    print('3. Perkalian')
    print('4. Pembagian')
    print('5. Modulus')
   
    a = float(input("Masukkan nilai a: "))
    b = float(input("Masukkan nilai b: "))
    y = int(input('Pilih operasi (1-5): '))

    if y == 1:
        hasil = a + b
        print("Hasil penjumlahan:", hasil)
    elif y == 2:
        hasil = a - b
        print("Hasil pengurangan:", hasil)
    elif y == 3:
        hasil = a * b
        print("Hasil perkalian:", hasil)
    elif y == 4:
        if b != 0:
            hasil = a / b
            print("Hasil pembagian:", hasil)
        else:
            print("Error: Tidak bisa dibagi dengan nol!")
    elif y == 5:
        hasil = a % b
        print("Hasil modulus:", hasil)
    else:
        print("Pilihan tidak valid!")

    # tanya lagi apakah ingin melanjutkan
    X = input('Ingin melanjutkan? (Y/N): ').upper()

print("Program selesai. Terima kasih!")
