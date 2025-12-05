# Fungsi Substitusi Cipher
def substitusi_cipher(plaintext, aturan):
    ciphertext = ""
    for char in plaintext.upper().replace(" ", ""):
        if char in aturan:
            ciphertext += aturan[char]
        else:
            ciphertext += char
    return ciphertext

# Fungsi Transposisi Cipher
def transposisi_cipher(plaintext):
    plaintext = plaintext.replace(" ", "")
    
    part_length = len(plaintext) // 4
    if len(plaintext) % 4 != 0:
        part_length += 1

    parts = [plaintext[i:i + part_length] for i in range(0, len(plaintext), part_length)]

    ciphertext = ""
    for col in range(4):
        for part in parts:
            if col < len(part):
                ciphertext += part[col]
    return ciphertext

# Aturan substitusi
aturan_substitusi = {
    'U': 'K',
    'N': 'N',
    'I': 'I',
    'K': 'K',
    'A': 'B'
}

# Input plaintext
plaintext = "UNIKA SANTO THOMAS"

# Proses substitusi
cipher_substitusi = substitusi_cipher(plaintext, aturan_substitusi)

# Proses transposisi dari hasil substitusi
cipher_transposisi = transposisi_cipher(cipher_substitusi)

# Output
print(f"Plaintext                       : {plaintext}")
print(f"Ciphertext Substitusi          : {cipher_substitusi}")
print(f"Ciphertext Substitusi+Transpos : {cipher_transposisi}")
