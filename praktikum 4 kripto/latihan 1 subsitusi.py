def substitusi_cipher(plaintext, aturan):
    ciphertext = ''
    for char in plaintext.upper():
        if char in aturan:
            ciphertext += aturan[char]
        else:
            ciphertext += char
    return ciphertext


# === Input aturan substitusi dari user ===
print("=== PROGRAM SUBSTITUSI CIPHER ===")
jumlah = int(input("Masukkan jumlah huruf yang akan disubstitusi: "))

aturan_substitusi = {}
for i in range(jumlah):
    huruf_asli = input(f"Masukkan huruf asli ke-{i+1}: ").upper()
    huruf_pengganti = input(f"Masukkan huruf pengganti untuk '{huruf_asli}': ").upper()
    aturan_substitusi[huruf_asli] = huruf_pengganti

# === Input plaintext ===
plaintext = input("\nMasukkan plaintext: ").upper()
ciphertext = substitusi_cipher(plaintext, aturan_substitusi)

print("\n--- HASIL ---")
print(f"Plaintext  : {plaintext}")
print(f"Ciphertext : {ciphertext}")
