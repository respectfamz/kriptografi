import tkinter as tk
from tkinter import messagebox

# ==============================
#   CLASS VIGENERE (PBO)
# ==============================
class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper().replace(" ", "")

    def encrypt(self, text):
        text = text.upper()
        result = ""
        ki = 0
        for ch in text:
            if ch.isalpha():
                p = ord(ch) - 65
                k = ord(self.key[ki % len(self.key)]) - 65
                c = (p + k) % 26
                result += chr(c + 65)
                ki += 1
            else:
                result += ch
        return result

    def decrypt(self, text):
        text = text.upper()
        result = ""
        ki = 0
        for ch in text:
            if ch.isalpha():
                c = ord(ch) - 65
                k = ord(self.key[ki % len(self.key)]) - 65
                p = (c - k) % 26
                result += chr(p + 65)
                ki += 1
            else:
                result += ch
        return result

# ==============================
#             GUI
# ==============================
root = tk.Tk()
root.title("Tugas Praktikum 5 - Vigenère Cipher")
root.geometry("650x600")
root.configure(bg="#F0F0F0")

label_title = tk.Label(
    root,
    text="TUGAS PRAKTIKUM 5\nIMPLEMENTASI Vigenère Cipher (ENKRIPSI / DEKRIPSI)",
    font=("Arial", 14, "bold"),
    bg="#F0F0F0"
)
label_title.pack(pady=10)

frame = tk.Frame(root, bg="#F0F0F0")
frame.pack(pady=10)

lbl_plain = tk.Label(frame, text="Input Text:", font=("Arial", 11), bg="#F0F0F0")
lbl_plain.grid(row=0, column=0, sticky="w")
entry_plain = tk.Entry(frame, width=50, font=("Arial", 11))
entry_plain.grid(row=0, column=1, pady=5)

lbl_key = tk.Label(frame, text="Key:", font=("Arial", 11), bg="#F0F0F0")
lbl_key.grid(row=1, column=0, sticky="w")
entry_key = tk.Entry(frame, width=50, font=("Arial", 11))
entry_key.grid(row=1, column=1, pady=5)

lbl_result = tk.Label(frame, text="Result:", font=("Arial", 11), bg="#F0F0F0")
lbl_result.grid(row=2, column=0, sticky="w")
entry_result = tk.Entry(frame, width=50, font=("Arial", 11))
entry_result.grid(row=2, column=1, pady=5)

lbl_log = tk.Label(root, text="Detail Proses:", font=("Arial", 11, "bold"), bg="#F0F0F0")
lbl_log.pack()
text_log = tk.Text(root, width=75, height=15, font=("Consolas", 10))
text_log.pack()

# ==============================
#        FUNCTIONS
# ==============================
def encrypt_action():
    text = entry_plain.get()
    key = entry_key.get().replace(" ", "").upper()

    if not text or not key:
        messagebox.showerror("Error", "Input dan key harus diisi!")
        return

    vc = VigenereCipher(key)
    result = vc.encrypt(text)

    entry_result.delete(0, tk.END)
    entry_result.insert(0, result)

    text_log.delete("1.0", tk.END)
    header = f"ENKRIPSI\nPlaintext : {text}\nKey       : {key}\nCipher    : {result}\n"
    text_log.insert(tk.END, header)

    detail = "\nDETAIL PER HURUF:\n"
    ki = 0
    for ch in text.upper():
        if ch.isalpha():
            p = ord(ch) - 65
            k = ord(key[ki % len(key)]) - 65
            c = (p + k) % 26
            detail += f"{ch} (p={p}) + {key[ki%len(key)]} (k={k}) = {chr(c+65)} (c={c})\n"
            ki += 1
    text_log.insert(tk.END, detail)


def decrypt_action():
    text = entry_plain.get()
    key = entry_key.get().replace(" ", "").upper()

    if not text or not key:
        messagebox.showerror("Error", "Input dan key harus diisi!")
        return

    vc = VigenereCipher(key)
    result = vc.decrypt(text)

    entry_result.delete(0, tk.END)
    entry_result.insert(0, result)

    text_log.delete("1.0", tk.END)
    header = f"DEKRIPSI\nCipher   : {text}\nKey      : {key}\nPlain    : {result}\n"
    text_log.insert(tk.END, header)

    detail = "\nDETAIL PER HURUF:\n"
    ki = 0
    for ch in text.upper():
        if ch.isalpha():
            c = ord(ch) - 65
            k = ord(key[ki % len(key)]) - 65
            p = (c - k) % 26
            detail += f"{ch} (c={c}) - {key[ki%len(key)]} (k={k}) = {chr(p+65)} (p={p})\n"
            ki += 1
    text_log.insert(tk.END, detail)


def reset_action():
    entry_plain.delete(0, tk.END)
    entry_key.delete(0, tk.END)
    entry_result.delete(0, tk.END)
    text_log.delete("1.0", tk.END)


def exit_action():
    root.destroy()

# ==============================
#           BUTTONS
# ==============================
btn_frame = tk.Frame(root, bg="#F0F0F0")
btn_frame.pack(pady=15)

btn_encrypt = tk.Button(btn_frame, text="ENKRIPSI", width=15, bg="#4CAF50", fg="white", font=("Arial", 11), command=encrypt_action)
btn_encrypt.grid(row=0, column=0, padx=10)

btn_decrypt = tk.Button(btn_frame, text="DEKRIPSI", width=15, bg="#2196F3", fg="white", font=("Arial", 11), command=decrypt_action)
btn_decrypt.grid(row=0, column=1, padx=10)

btn_reset = tk.Button(btn_frame, text="RESET", width=15, bg="#F44336", fg="white", font=("Arial", 11), command=reset_action)
btn_reset.grid(row=0, column=2, padx=10)

btn_exit = tk.Button(btn_frame, text="KELUAR", width=15, bg="#555555", fg="white", font=("Arial", 11), command=exit_action)
btn_exit.grid(row=0, column=3, padx=10)

root.mainloop()