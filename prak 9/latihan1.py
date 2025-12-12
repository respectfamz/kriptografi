import tkinter as tk
from tkinter import messagebox

# ===================== Latihan 1 - p,q,e ditentukan =====================
p = 17
q = 11
e = 7
plaintext = "yudiyohanness"

def run_latihan1():
    # Langkah 1: Hitung n
    n = p * q
    step1 = f"Langkah 1: Hitung n = p * q = {p} * {q} = {n}\n"

    # Langkah 2: Hitung phi(n)
    phi = (p - 1) * (q - 1)
    step2 = f"Langkah 2: Hitung phi(n) = (p-1)*(q-1) = ({p}-1)*({q}-1) = {phi}\n"

    # Langkah 3: Tampilkan e
    step3 = f"Langkah 3: Nilai e = {e}\n"

    # Langkah 4: Ubah plaintext ke ASCII
    plaintext_numbers = [ord(char) for char in plaintext]
    step4 = f"Langkah 4: Ubah plaintext ke angka ASCII\n{plaintext} → {plaintext_numbers}\n"

    # Langkah 5: Enkripsi tiap angka dengan detail
    ciphertext_numbers = []
    cipher_details = []
    for m in plaintext_numbers:
        c = pow(m, e, n)
        ciphertext_numbers.append(c)
        cipher_details.append(f"M = {m}, C = M^e mod n = {m}^{e} mod {n} = {c}")
    step5 = "Langkah 5: Enkripsi tiap angka\n" + "\n".join(cipher_details) + "\n"
    step5 += f"Ciphertext akhir: {ciphertext_numbers}"

    # Gabungkan semua langkah
    result = step1 + step2 + step3 + step4 + step5
    messagebox.showinfo("Hasil Enkripsi RSA - Detail", result)

# ===================== GUI =====================
root = tk.Tk()
root.title("RSA GUI - Latihan 1 (Enkripsi Detail)")
root.geometry("700x500")

label = tk.Label(root, text="Latihan 1 - p,q,e sudah ditentukan (Enkripsi Detail)", font=("Arial", 12))
label.pack(pady=20)

btn = tk.Button(root, text="Jalankan Enkripsi RSA", command=run_latihan1)
btn.pack(pady=10)

root.mainloop()
