import tkinter as tk
from tkinter import messagebox

def hitung():
    try:
        a = float(entry_a.get() or 0)
        b = float(entry_b.get() or 0)
        op = entry_op.get().strip()

        if op == "+":
            hasil = a + b
        elif op == "-":
            hasil = a - b
        elif op == "*":
            hasil = a * b
        elif op == "/":
            if b != 0:
                hasil = a / b
            else:
                messagebox.showerror("Error", "Pembagian dengan nol tidak boleh!")
                return
        else:
            messagebox.showerror("Error", "Operator tidak valid! Gunakan + - * /")
            return

        label_hasil.config(text=f"Hasil: {hasil}")

    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

def reset():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_op.delete(0, tk.END)
    label_hasil.config(text="")

root = tk.Tk()
root.title("Kalkulator Sederhana (File 2)")
root.geometry("300x300")

tk.Label(root, text="Kalkulator Sederhana", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Angka Pertama:").pack()
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="Angka Kedua:").pack()
entry_b = tk.Entry(root)
entry_b.pack()

tk.Label(root, text="Operator (+, -, *, /):").pack()
entry_op = tk.Entry(root)
entry_op.pack()

tk.Button(root, text="Hitung", width=10, command=hitung).pack(pady=5)
tk.Button(root, text="Reset", width=10, command=reset).pack(pady=5)
tk.Button(root, text="Exit", width=10, command=root.destroy).pack(pady=5)

label_hasil = tk.Label(root, text="", font=("Arial", 12))
label_hasil.pack(pady=10)

root.mainloop()
