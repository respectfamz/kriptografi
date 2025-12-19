import tkinter as tk

# ===================== UTILITY =====================
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
        yscrollcommand=y_scroll.set,
        xscrollcommand=x_scroll.set
    )
    text.pack(expand=True, fill=tk.BOTH)

    y_scroll.config(command=text.yview)
    x_scroll.config(command=text.xview)

    text.insert(tk.END, content)
    text.config(state=tk.DISABLED)

# ===================== ELGAMAL FIXED =====================
def run_elgamal_fixed():
    # Parameter ditentukan
    p = 467
    g = 2
    x = 127
    k = 53
    plaintext = "YUDIYOHANNES"

    output = ""
    output += "ELGAMAL - NILAI DITENTUKAN\n"
    output += "="*60 + "\n\n"

    output += "=== PEMBENTUKAN KUNCI ===\n"
    output += f"p = {p} (prima)\n"
    output += f"g = {g} (generator)\n"
    output += f"x = {x} (private key)\n"
    output += f"k = {k} (bilangan acak)\n\n"

    output += "Rumus public key:\n"
    output += "y = g^x mod p\n"
    y = pow(g, x, p)
    output += f"y = {g}^{x} mod {p} = {y}\n\n"

    ascii_vals = [ord(c) for c in plaintext]
    output += "=== KONVERSI PLAINTEXT KE ASCII ===\n"
    output += f"Plaintext = {plaintext}\n"
    output += f"ASCII     = {ascii_vals}\n\n"

    output += "=== ENKRIPSI ===\n"
    output += "Rumus:\n"
    output += "a = g^k mod p\n"
    a = pow(g, k, p)
    output += f"a = {g}^{k} mod {p} = {a}\n\n"

    output += "Rumus:\n"
    output += "b = m × y^k mod p\n"
    yk = pow(y, k, p)
    output += f"y^k = {y}^{k} mod {p} = {yk}\n\n"

    cipher = []
    for i, m in enumerate(ascii_vals, start=1):
        b = (m * yk) % p
        cipher.append((a, b))
        output += f"[{i}] m = {m}\n"
        output += f"    b = {m} × {yk} mod {p} = {b}\n\n"

    output += "=== DEKRIPSI ===\n"
    output += "Rumus:\n"
    output += "m = b × (a^x)^(-1) mod p\n\n"

    ax = pow(a, x, p)
    ax_inv = mod_inverse(ax, p)
    output += f"a^x = {a}^{x} mod {p} = {ax}\n"
    output += f"(a^x)^(-1) mod {p} = {ax_inv}\n\n"

    decrypted = ""
    for i, (_, b) in enumerate(cipher, start=1):
        m = (b * ax_inv) % p
        decrypted += chr(m)
        output += f"[{i}] m = {b} × {ax_inv} mod {p} = {m}\n"

    output += "\nPLAINTEXT HASIL DEKRIPSI:\n"
    output += decrypted + "\n"

    show_scrollable_result("ElGamal - Nilai Ditentukan", output)

# ===================== GUI =====================
root = tk.Tk()
root.title("ElGamal GUI - Nilai Ditentukan")
root.geometry("400x250")

tk.Label(root, text="ElGamal\nNilai Ditentukan", font=("Arial", 12)).pack(pady=20)
tk.Button(root, text="Jalankan ElGamal", command=run_elgamal_fixed).pack(pady=20)

root.mainloop()
