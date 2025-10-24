import tkinter as tk
import subprocess

def buka_file1():
    subprocess.Popen(["python", "latihan krypto dan stegano.py"])

def buka_file2():
    subprocess.Popen(["python", "latihan.3 visual program.py"])

def buka_file3():
    subprocess.Popen(["python", "latihan2.krypto.py"])

root = tk.Tk()
root.title("Menu Utama")
root.geometry("300x250")

tk.Label(root, text="Menu Utama", font=("Arial", 16, "bold")).pack(pady=20)

tk.Button(root, text="Operasi Dasar (File 1)", width=25, command=buka_file1).pack(pady=5)
tk.Button(root, text="Kalkulator Sederhana (File 2)", width=25, command=buka_file2).pack(pady=5)
tk.Button(root, text="Nilai Mahasiswa (File 3)", width=25, command=buka_file3).pack(pady=5)

tk.Button(root, text="Keluar", width=25, command=root.destroy).pack(pady=20)

root.mainloop()
