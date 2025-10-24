import tkinter as tk
from tkinter import messagebox

def hitung(operasi):
    try:
        a = float(entry_a.get() or 0)
        b = float(entry_b.get() or 0)

        if operasi == "tambah":
            hasil = a + b
        elif operasi == "kurang":
            hasil = a - b
        elif operasi == "kali":
            hasil = a * b
        elif operasi == "bagi":
            if b != 0:
                hasil = a / b
            else:
                messagebox.showerror("Error", "Pembagian dengan nol tidak boleh!")
                return
        else:
            hasil = "?"

        label_hasil.config(text=f"Hasil: {hasil}")

    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

def reset():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    label_hasil.config(text="")

root = tk.Tk()
root.title("Operasi Dasar (File 1)")
root.geometry("300x300")

tk.Label(root, text="Operasi Dasar", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Angka Pertama:").pack()
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="Angka Kedua:").pack()
entry_b = tk.Entry(root)
entry_b.pack()

frame_btn = tk.Frame(root)
frame_btn.pack(pady=10)

tk.Button(frame_btn, text="Tambah", width=10, command=lambda: hitung("tambah")).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_btn, text="Kurang", width=10, command=lambda: hitung("kurang")).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_btn, text="Kali", width=10, command=lambda: hitung("kali")).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame_btn, text="Bagi", width=10, command=lambda: hitung("bagi")).grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, text="Reset", width=10, command=reset).pack(pady=5)
tk.Button(root, text="Exit", width=10, command=root.destroy).pack(pady=5)

label_hasil = tk.Label(root, text="", font=("Arial", 12))
label_hasil.pack(pady=10)

root.mainloop()
