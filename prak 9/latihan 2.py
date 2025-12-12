import tkinter as tk
from tkinter import messagebox
import math

# ===================== Utility Functions =====================
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# ===================== Program Latihan 2 (Input User + Teks, Enkripsi Detail) =====================
def run_latihan2():
    try:
        p = int(entry_p.get())
        q = int(entry_q.get())
        e = int(entry_e.get())
        plaintext = entry_plain.get()
    except:
        messagebox.showerror("Error", "Masukkan p, q, e berupa angka dan plaintext berupa teks!")
        return

    # Validasi prima
    if not is_prime(p):
        messagebox.showerror("Error", f"p = {p} bukan bilangan prima!")
        return
    if not is_prime(q):
        messagebox.showerror("Error", f"q = {q} bukan bilangan prima!")
        return
    if not is_prime(e):
        messagebox.showerror("Error", f"e = {e} bukan bilangan prima!")
        return

    n = p * q
    phi = (p - 1) * (q - 1)

    # Konversi plaintext teks ke ASCII
    plaintext_numbers = [ord(char) for char in plaintext]
    if any(m >= n for m in plaintext_numbers):
        messagebox.showerror("Error", f"Semua karakter ASCII harus < n = p*q = {n}")
        return

    # Enkripsi tiap karakter dengan detail
    ciphertext_numbers = []
    cipher_details = []
    for m in plaintext_numbers:
        c = pow(m, e, n)
        ciphertext_numbers.append(c)
        cipher_details.append(f"M = {m}, C = M^e mod n = {m}^{e} mod {n} = {c}")

    # Buat hasil detail
    result = f"Latihan 2 - Input User + Plaintext Teks (Enkripsi Detail)\n\n"
    result += f"p = {p}\nq = {q}\nn = {n}\nphi(n) = {phi}\ne = {e}\n\n"
    result += f"Plaintext ASCII:\n{plaintext_numbers}\n\n"
    result += "=== Enkripsi Detail ===\n" + "\n".join(cipher_details) + "\n\n"
    result += f"Ciphertext akhir:\n{ciphertext_numbers}"

    messagebox.showinfo("Hasil Enkripsi RSA - Detail", result)

# ===================== GUI =====================
root = tk.Tk()
root.title("RSA GUI - Latihan 2 (Enkripsi Detail)")
root.geometry("600x500")

label = tk.Label(root, text="Masukkan p, q, e (prima) dan plaintext (teks)", font=("Arial", 12))
label.pack(pady=10)

entry_p = tk.Entry(root, width=30)
entry_q = tk.Entry(root, width=30)
entry_e = tk.Entry(root, width=30)
entry_plain = tk.Entry(root, width=30)

entry_p.pack(pady=5); entry_p.insert(0,"" )
entry_q.pack(pady=5); entry_q.insert(0, "")
entry_e.pack(pady=5); entry_e.insert(0,"")
entry_plain.pack(pady=5); entry_plain.insert(0,"" )

btn = tk.Button(root, text="Jalankan Enkripsi RSA", command=run_latihan2)
btn.pack(pady=20)

root.mainloop()
