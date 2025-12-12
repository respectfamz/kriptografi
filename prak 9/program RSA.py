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
    for d in range(1, m):
        if (a * d) % m == 1:
            return d
    return None

# ===================== Program Latihan 3 (RSA Lengkap Teks dengan Detail) =====================
def run_latihan3():
    try:
        p = int(entry_p.get())
        q = int(entry_q.get())
        e = int(entry_e.get())
        plaintext = entry_plain.get()
    except:
        messagebox.showerror("Error", "p, q, e harus angka dan plaintext berupa teks!")
        return

    # Validasi prima
    if not is_prime(p) or not is_prime(q):
        messagebox.showerror("Error", "p dan q harus bilangan prima!")
        return

    n = p * q
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)
    if d is None:
        messagebox.showerror("Error", "Tidak ada modular inverse untuk e mod phi(n). Pilih e lain!")
        return

    # Konversi plaintext ke ASCII
    plaintext_numbers = [ord(c) for c in plaintext]
    if any(m >= n for m in plaintext_numbers):
        messagebox.showerror("Error", f"Semua karakter ASCII harus < n = {n}")
        return

    # Enkripsi per karakter dengan detail
    cipher_details = []
    ciphertext_numbers = []
    for m in plaintext_numbers:
        c = pow(m, e, n)
        ciphertext_numbers.append(c)
        cipher_details.append(f"M = {m}, C = M^e mod n = {m}^{e} mod {n} = {c}")

    # Dekripsi per karakter dengan detail
    decrypt_details = []
    decrypted_numbers = []
    decrypted_text = ""
    for c in ciphertext_numbers:
        m = pow(c, d, n)
        decrypted_numbers.append(m)
        decrypted_text += chr(m)
        decrypt_details.append(f"C = {c}, M = C^d mod n = {c}^{d} mod {n} = {m}")

    # Gabungkan semua detail
    result = f"Latihan 3 - RSA Lengkap (Teks)\n\n"
    result += f"p = {p}, q = {q}\nn = {n}, phi(n) = {phi}\ne = {e}, d = {d}\n\n"
    result += "Plaintext ASCII:\n" + str(plaintext_numbers) + "\n\n"
    result += "=== Enkripsi Detail ===\n" + "\n".join(cipher_details) + "\n\n"
    result += "Ciphertext (per ASCII):\n" + str(ciphertext_numbers) + "\n\n"
    result += "=== Dekripsi Detail ===\n" + "\n".join(decrypt_details) + "\n\n"
    result += f"Plaintext setelah Dekripsi:\n{decrypted_text}"

    messagebox.showinfo("Hasil RSA Lengkap dengan Detail", result)

# ===================== GUI =====================
root = tk.Tk()
root.title("RSA GUI - Latihan 3 (RSA Lengkap Teks Detail)")
root.geometry("600x600")

label = tk.Label(root, text="Latihan 3 - RSA Lengkap (Plaintext Teks, Detail)", font=("Arial", 12))
label.pack(pady=10)

entry_p = tk.Entry(root, width=30)
entry_q = tk.Entry(root, width=30)
entry_e = tk.Entry(root, width=30)
entry_plain = tk.Entry(root, width=30)

entry_p.pack(pady=5); entry_p.insert(0, )
entry_q.pack(pady=5); entry_q.insert(0, )
entry_e.pack(pady=5); entry_e.insert(0, )
entry_plain.pack(pady=5); entry_plain.insert(0, )

btn = tk.Button(root, text="Jalankan RSA dengan Detail", command=run_latihan3)
btn.pack(pady=20)

root.mainloop()
