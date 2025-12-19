import tkinter as tk
import math

# ===================== Utility =====================
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def show_scrollable_result(title, content):
    win = tk.Toplevel()
    win.title(title)
    win.geometry("900x700")
    win.minsize(800, 600)

    y_scroll = tk.Scrollbar(win, orient=tk.VERTICAL)
    y_scroll.pack(side=tk.RIGHT, fill=tk.Y)

    x_scroll = tk.Scrollbar(win, orient=tk.HORIZONTAL)
    x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

    text = tk.Text(
        win,
        wrap=tk.NONE,
        font=("Courier New", 10),
        xscrollcommand=x_scroll.set,
        yscrollcommand=y_scroll.set
    )
    text.pack(expand=True, fill=tk.BOTH)

    y_scroll.config(command=text.yview)
    x_scroll.config(command=text.xview)

    text.insert(tk.END, content)
    text.config(state=tk.DISABLED)

# ===================== ElGamal Input =====================
def run_elgamal_input():
    p = int(entry_p.get())
    g = int(entry_g.get())
    x = int(entry_x.get())
    k = int(entry_k.get())
    plaintext = entry_plain.get()

    if not is_prime(p):
        return

    result = ""
    result += "ELGAMAL - INPUT USER\n"
    result += "=" * 60 + "\n\n"

    result += "=== PARAMETER INPUT ===\n"
    result += f"p = {p} (bilangan prima)\n"
    result += f"g = {g} (generator)\n"
    result += f"x = {x} (private key)\n"
    result += f"k = {k} (bilangan acak)\n\n"

    y = pow(g, x, p)
    result += "Public key:\n"
    result += f"y = g^x mod p = {g}^{x} mod {p} = {y}\n\n"

    ascii_vals = [ord(c) for c in plaintext]
    result += "=== KONVERSI PLAINTEXT KE ASCII ===\n"
    result += f"Plaintext : {plaintext}\n"
    result += f"ASCII     : {ascii_vals}\n\n"

    a = pow(g, k, p)
    yk = pow(y, k, p)

    result += "=== ENKRIPSI ===\n"
    result += f"a = g^k mod p = {g}^{k} mod {p} = {a}\n"
    result += f"y^k mod p = {y}^{k} mod {p} = {yk}\n\n"

    cipher = []
    for i, m in enumerate(ascii_vals, start=1):
        b = (m * yk) % p
        cipher.append((a, b))
        result += f"Karakter ke-{i}: b = {m} × {yk} mod {p} = {b}\n"

    ax = pow(a, x, p)
    ax_inv = mod_inverse(ax, p)

    result += "\n=== DEKRIPSI ===\n"
    result += f"a^x = {a}^{x} mod {p} = {ax}\n"
    result += f"(a^x)^(-1) mod {p} = {ax_inv}\n\n"

    decrypted = ""
    for i, (_, b) in enumerate(cipher, start=1):
        m = (b * ax_inv) % p
        decrypted += chr(m)
        result += f"Karakter ke-{i}: m = {b} × {ax_inv} mod {p} = {m}\n"

    result += "\n" + "=" * 60 + "\n"
    result += f"PLAINTEXT HASIL DEKRIPSI:\n{decrypted}\n"

    show_scrollable_result("ElGamal Detail - Input User", result)

# ===================== GUI =====================
root = tk.Tk()
root.title("ElGamal GUI - Input User")
root.geometry("450x450")

title = tk.Label(root, text="ELGAMAL - INPUT USER", font=("Arial", 12, "bold"))
title.pack(pady=10)

# ===== Form Input =====
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="p (bilangan prima)").grid(row=0, column=0, sticky="w", pady=5)
entry_p = tk.Entry(frame, width=30)
entry_p.grid(row=0, column=1)
entry_p.insert(0, "467")

tk.Label(frame, text="g (generator)").grid(row=1, column=0, sticky="w", pady=5)
entry_g = tk.Entry(frame, width=30)
entry_g.grid(row=1, column=1)
entry_g.insert(0, "2")

tk.Label(frame, text="x (private key)").grid(row=2, column=0, sticky="w", pady=5)
entry_x = tk.Entry(frame, width=30)
entry_x.grid(row=2, column=1)
entry_x.insert(0, "127")

tk.Label(frame, text="k (bilangan acak)").grid(row=3, column=0, sticky="w", pady=5)
entry_k = tk.Entry(frame, width=30)
entry_k.grid(row=3, column=1)
entry_k.insert(0, "53")

tk.Label(frame, text="Plaintext").grid(row=4, column=0, sticky="w", pady=5)
entry_plain = tk.Entry(frame, width=30)
entry_plain.grid(row=4, column=1)
entry_plain.insert(0, "YUDIYOHANNES")

# ===== Button =====
tk.Button(root, text="Jalankan ElGamal", command=run_elgamal_input).pack(pady=20)

root.mainloop()
