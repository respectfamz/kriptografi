import tkinter as tk
from tkinter import messagebox

def hitung_nilai():
    try:
        uts = float(entry_uts.get() or 0)
        uas = float(entry_uas.get() or 0)
        tugas = float(entry_tugas.get() or 0)
        sikap = float(entry_sikap.get() or 0)

        # Hitung nilai akhir
        nilai_seluruh = (0.1 * sikap) + (0.3 * tugas) + (0.25 * uts) + (0.35 * uas)

        # Tentukan nilai huruf
        if nilai_seluruh >= 81:
            nilai_huruf = "A"
        elif nilai_seluruh >= 75:
            nilai_huruf = "B+"
        elif nilai_seluruh >= 70:
            nilai_huruf = "B"
        elif nilai_seluruh >= 65:
            nilai_huruf = "C+"
        elif nilai_seluruh >= 55:
            nilai_huruf = "C"
        elif nilai_seluruh >= 40:
            nilai_huruf = "D"
        else:
            nilai_huruf = "E"

        # Tampilkan hasil
        label_hasil.config(
            text=f"Nilai Akhir: {nilai_seluruh:.2f}\nNilai Huruf: {nilai_huruf}"
        )

    except ValueError:
        messagebox.showerror("Error", "Input harus berupa angka!")

def reset():
    entry_uts.delete(0, tk.END)
    entry_uas.delete(0, tk.END)
    entry_tugas.delete(0, tk.END)
    entry_sikap.delete(0, tk.END)
    label_hasil.config(text="")

# GUI utama
root = tk.Tk()
root.title("Kalkulator Nilai Mahasiswa")
root.geometry("320x350")

# Judul
tk.Label(root, text="Kalkulator Nilai Mahasiswa", font=("Arial", 14, "bold")).pack(pady=10)

# Input UTS
tk.Label(root, text="Nilai UTS:").pack()
entry_uts = tk.Entry(root)
entry_uts.pack()

# Input UAS
tk.Label(root, text="Nilai UAS:").pack()
entry_uas = tk.Entry(root)
entry_uas.pack()

# Input Tugas
tk.Label(root, text="Nilai Tugas:").pack()
entry_tugas = tk.Entry(root)
entry_tugas.pack()

# Input Sikap
tk.Label(root, text="Nilai Sikap:").pack()
entry_sikap = tk.Entry(root)
entry_sikap.pack()

# Tombol Hitung, Reset, Exit
frame_btn = tk.Frame(root)
frame_btn.pack(pady=15)

tk.Button(frame_btn, text="Hitung", width=10, command=hitung_nilai).grid(row=0, column=0, padx=5)
tk.Button(frame_btn, text="Reset", width=10, command=reset).grid(row=0, column=1, padx=5)
tk.Button(frame_btn, text="Exit", width=10, command=root.destroy).grid(row=0, column=2, padx=5)

# Label Hasil
label_hasil = tk.Label(root, text="", font=("Arial", 12))
label_hasil.pack(pady=10)

root.mainloop()
