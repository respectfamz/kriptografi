import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

# ============================
# DES TABLES & FUNCTIONS
# ============================

IP = [
    58,50,42,34,26,18,10,2,
    60,52,44,36,28,20,12,4,
    62,54,46,38,30,22,14,6,
    64,56,48,40,32,24,16,8,
    57,49,41,33,25,17,9,1,
    59,51,43,35,27,19,11,3,
    61,53,45,37,29,21,13,5,
    63,55,47,39,31,23,15,7
]

FP = [
    40,8,48,16,56,24,64,32,
    39,7,47,15,55,23,63,31,
    38,6,46,14,54,22,62,30,
    37,5,45,13,53,21,61,29,
    36,4,44,12,52,20,60,28,
    35,3,43,11,51,19,59,27,
    34,2,42,10,50,18,58,26,
    33,1,41,9,49,17,57,25
]

E = [
    32,1,2,3,4,5,
    4,5,6,7,8,9,
    8,9,10,11,12,13,
    12,13,14,15,16,17,
    16,17,18,19,20,21,
    20,21,22,23,24,25,
    24,25,26,27,28,29,
    28,29,30,31,32,1
]

P = [
    16,7,20,21,
    29,12,28,17,
    1,15,23,26,
    5,18,31,10,
    2,8,24,14,
    32,27,3,9,
    19,13,30,6,
    22,11,4,25
]

PC_1 = [
    57,49,41,33,25,17,9,
    1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,
    19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,
    7,62,54,46,38,30,22,
    14,6,61,53,45,37,29,
    21,13,5,28,20,12,4
]

PC_2 = [
    14,17,11,24,1,5,
    3,28,15,6,21,10,
    23,19,12,4,26,8,
    16,7,27,20,13,2,
    41,52,31,37,47,55,
    30,40,51,45,33,48,
    44,49,39,56,34,53,
    46,42,50,36,29,32
]

SHIFTS = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

S_BOX = [
[
 [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
 [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
 [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
 [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
],
[
 [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
 [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
 [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
 [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
],
[
 [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
 [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
 [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
 [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
],
[
 [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
 [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
 [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
 [3,15,0,6,10,1,13,8,9,5,11,12,7,2,14]
],
[
 [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
 [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
 [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
 [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
],
[
 [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
 [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
 [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
 [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
],
[
 [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
 [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
 [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
 [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
],
[
 [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
 [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
 [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
 [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
]
]

# ----------------------- Utilities -----------------------

def str_to_bits(s):
    bits = []
    for b in s:
        for i in range(7, -1, -1):
            bits.append((b >> i) & 1)
    return bits

def bits_to_bytes(bits):
    res = bytearray()
    for i in range(0, len(bits), 8):
        val = 0
        for j in range(8):
            val = (val << 1) | bits[i+j]
        res.append(val)
    return bytes(res)

def permute(bits, table):
    return [bits[i-1] for i in table]

def xor(a, b):
    return [i ^ j for i,j in zip(a,b)]

def left_shift(bits, n):
    return bits[n:] + bits[:n]

# ----------------------- Core functions with validation -----------------------

def feistel(R, K):
    # R must be 32 bits, K must be 48 bits
    if len(R) != 32:
        raise ValueError(f"R harus 32 bit, tapi len(R)={len(R)}")
    if len(K) != 48:
        raise ValueError(f"K harus 48 bit, tapi len(K)={len(K)}")

    details = {}
    E_R = permute(R, E)
    if len(E_R) != 48:
        raise ValueError(f"E(R) harus 48 bit, tapi len(E_R)={len(E_R)}")
    details['E(R)'] = ''.join(map(str, E_R))

    X = xor(E_R, K)
    if len(X) != 48:
        raise ValueError(
            "ERROR: E(R) ^ K bukan 48 bit.\n"
            f"len(E_R)={len(E_R)}, len(K)={len(K)}, len(X)={len(X)}\n"
            f"E_R={''.join(map(str,E_R))}\nK  ={''.join(map(str,K))}\nX  ={''.join(map(str,X))}"
        )
    details['E(R)^K'] = ''.join(map(str, X))

    s_out_bits = []
    s_details = []
    for i in range(8):
        block = X[i*6:(i+1)*6]
        if len(block) != 6:
            raise ValueError(f"Block ke-{i} pada X tidak 6 bit (len={len(block)}). X={''.join(map(str,X))}")
        row = (block[0] << 1) | block[5]
        col = (block[1] << 3) | (block[2] << 2) | (block[3] << 1) | block[4]
        if not (0 <= row <= 3) or not (0 <= col <= 15):
            raise ValueError(f"S-box index out of range: i={i}, row={row}, col={col}, block={block}")
        val = S_BOX[i][row][col]
        bits4 = [ (val >> k) & 1 for k in range(3, -1, -1) ]
        s_out_bits.extend(bits4)
        s_details.append({
            'box': i+1,
            'in': ''.join(map(str, block)),
            'row': row,
            'col': col,
            'val': val,
            'out': ''.join(map(str, bits4))
        })

    details['S_boxes'] = s_details
    details['S_out'] = ''.join(map(str, s_out_bits))
    P_out = permute(s_out_bits, P)
    details['P(S)'] = ''.join(map(str, P_out))
    details['f'] = ''.join(map(str, P_out))
    return P_out, details

def generate_subkeys(key_bytes):
    # key_bytes must be exactly 8 bytes (64 bits). Normalize here.
    if not isinstance(key_bytes, (bytes, bytearray)):
        raise TypeError("Key harus bytes.")
    if len(key_bytes) > 8:
        key_bytes = key_bytes[:8]
    elif len(key_bytes) < 8:
        key_bytes = key_bytes + b'\x00' * (8 - len(key_bytes))

    key_bits = str_to_bits(key_bytes)  # 64 bits
    pc1 = permute(key_bits, PC_1)      # 56 bits
    if len(pc1) != 56:
        raise ValueError(f"PC-1 menghasilkan panjang {len(pc1)} (harus 56)")
    C = pc1[:28]
    D = pc1[28:]
    subkeys = []
    for s in SHIFTS:
        C = left_shift(C, s)
        D = left_shift(D, s)
        CD = C + D
        K = permute(CD, PC_2)
        if len(K) != 48:
            raise ValueError(f"PC-2 menghasilkan panjang {len(K)} (harus 48)")
        subkeys.append(K)
    return subkeys, pc1

def des_encrypt_block(block_bytes, subkeys, key_labels=None):
    if len(block_bytes) != 8:
        raise ValueError(f"Block harus 8 bytes, tapi len={len(block_bytes)}")
    bits = str_to_bits(block_bytes)
    bits = permute(bits, IP)
    L = bits[:32]
    R = bits[32:]
    logs = []

    for rnd in range(16):
        f_out, inter = feistel(R, subkeys[rnd])
        newR = xor(L, f_out)

        if key_labels:
            klabel = key_labels[rnd]
        else:
            klabel = f"K{rnd+1:02d}"

        lg = []
        lg.append(f"Round {rnd+1:02d} | using {klabel}")
        lg.append(f"  Before: L = {''.join(map(str,L))}")
        lg.append(f"          R = {''.join(map(str,R))}")
        lg.append(f"  E(R)           = {inter['E(R)']}")
        lg.append(f"  E(R) ^ {klabel} = {inter['E(R)^K']}")
        lg.append(f"  S-box results:")
        for sd in inter['S_boxes']:
            lg.append(f"    S{sd['box']:02d}: in={sd['in']} row={sd['row']} col={sd['col']} val={sd['val']} out={sd['out']}")
        lg.append(f"  S_out (32bit)  = {inter['S_out']}")
        lg.append(f"  P(S_out)       = {inter['P(S)']}")
        lg.append(f"  f(R,{klabel})  = {inter['f']}")
        lg.append(f"  After : L = {''.join(map(str,R))}")
        lg.append(f"          R = {''.join(map(str,newR))}")
        logs.append('\n'.join(lg) + '\n')

        L = R
        R = newR

    final = permute(R + L, FP)
    return final, logs

def pad(b):
    padlen = 8 - (len(b) % 8)
    return b + bytes([padlen])*padlen

def unpad(b):
    if not b:
        return b
    last = b[-1]
    if last < 1 or last > 8:
        return b
    if b[-last:] != bytes([last])*last:
        return b
    return b[:-last]

# ============================ GUI FUNCTIONS ============================

def encrypt_gui():
    try:
        text = entry_plain.get()
        key = entry_key.get()

        if len(key) == 0:
            messagebox.showerror("Error", "Key tidak boleh kosong")
            return

        # normalize key berdasarkan bytes (truncate/pad)
        key_bytes = key.encode('utf-8')
        if len(key_bytes) > 8:
            key_bytes = key_bytes[:8]
        elif len(key_bytes) < 8:
            key_bytes = key_bytes + b'\x00' * (8 - len(key_bytes))

        subkeys, pc1 = generate_subkeys(key_bytes)
        key_labels = [f"K{i+1:02d}" for i in range(16)]

        output.configure(state='normal')
        output.delete("1.0", tk.END)
        output.insert(tk.END, "=== PC-1 (56 bit) ===\n")
        output.insert(tk.END, ''.join(map(str, pc1)) + "\n\n")
        output.insert(tk.END, "=== 16 Subkey ===\n")
        for i, K in enumerate(subkeys):
            output.insert(tk.END, f"{key_labels[i]}: {''.join(map(str,K))}\n")
        output.insert(tk.END, "\n")

        plaintext_bytes = text.encode('utf-8')
        padded = pad(plaintext_bytes)
        cipher_bits_all = []

        output.insert(tk.END, "=== Proses Encrypt ===\n\n")
        for i in range(0, len(padded), 8):
            block = padded[i:i+8]
            cbits, logs = des_encrypt_block(block, subkeys, key_labels=key_labels)
            cipher_bits_all.extend(cbits)

            output.insert(tk.END, f"--- Block {i//8 + 1} ---\n")
            for lg in logs:
                output.insert(tk.END, lg + "\n")

        cipher_hex = bits_to_bytes(cipher_bits_all).hex().upper()
        cipher_bin = ''.join(map(str, cipher_bits_all))

        output.insert(tk.END, "\n=== HASIL AKHIR (ENCRYPT) ===\n")
        output.insert(tk.END, f"Cipher (HEX): {cipher_hex}\n")
        output.insert(tk.END, f"Cipher (BIN): {cipher_bin}\n")
        output.configure(state='disabled')

    except Exception as e:
        output.configure(state='normal')
        output.insert(tk.END, f"\nERROR: {e}\n")
        output.configure(state='disabled')
        messagebox.showerror("Error saat encrypt", str(e))

def decrypt_gui():
    try:
        text = entry_plain.get().strip().replace(" ", "")
        key = entry_key.get()

        if len(key) == 0:
            messagebox.showerror("Error", "Key tidak boleh kosong")
            return
        if len(text) == 0:
            messagebox.showerror("Error", "Masukkan ciphertext (HEX) di kotak Plaintext untuk dekripsi.")
            return

        try:
            cipher_bytes = bytes.fromhex(text)
        except Exception:
            messagebox.showerror("Error", "Ciphertext tidak valid HEX.")
            return

        key_bytes = key.encode('utf-8')
        if len(key_bytes) > 8:
            key_bytes = key_bytes[:8]
        elif len(key_bytes) < 8:
            key_bytes = key_bytes + b'\x00' * (8 - len(key_bytes))

        subkeys, pc1 = generate_subkeys(key_bytes)
        key_labels_enc = [f"K{i+1:02d}" for i in range(16)]
        key_labels_dec = key_labels_enc[::-1]
        subkeys_rev = subkeys[::-1]

        output.configure(state='normal')
        output.delete("1.0", tk.END)
        output.insert(tk.END, "=== PC-1 (56 bit) ===\n")
        output.insert(tk.END, ''.join(map(str, pc1)) + "\n\n")
        output.insert(tk.END, "=== Subkeys (used for decrypt in this order) ===\n")
        for i, K in enumerate(subkeys_rev):
            output.insert(tk.END, f"{key_labels_dec[i]}: {''.join(map(str,K))}\n")
        output.insert(tk.END, "\n")

        output.insert(tk.END, "=== Proses Decrypt ===\n\n")
        plain_bytes_all = bytearray()

        for i in range(0, len(cipher_bytes), 8):
            block = cipher_bytes[i:i+8]
            if len(block) < 8:
                messagebox.showerror("Error", f"Ciphertext length invalid: block {i//8 + 1} is less than 8 bytes.")
                output.configure(state='disabled')
                return
            pbits, logs = des_encrypt_block(block, subkeys_rev, key_labels=key_labels_dec)
            block_bytes = bits_to_bytes(pbits)
            plain_bytes_all.extend(block_bytes)

            output.insert(tk.END, f"--- Block {i//8 + 1} ---\n")
            for lg in logs:
                output.insert(tk.END, lg + "\n")

        unp = unpad(bytes(plain_bytes_all))
        plain_result = unp.decode('utf-8', errors='replace')

        output.insert(tk.END, "\n=== HASIL AKHIR (DECRYPT) ===\n")
        output.insert(tk.END, f"Plaintext: {plain_result}\n")
        output.configure(state='disabled')

        entry_plain.delete(0, tk.END)
        entry_plain.insert(0, plain_result)

    except Exception as e:
        output.configure(state='normal')
        output.insert(tk.END, f"\nERROR: {e}\n")
        output.configure(state='disabled')
        messagebox.showerror("Error saat decrypt", str(e))

def reset_gui():
    entry_plain.delete(0, tk.END)
    entry_key.delete(0, tk.END)
    output.configure(state='normal')
    output.delete("1.0", tk.END)
    output.configure(state='disabled')

def exit_gui():
    root.destroy()

# ============================ Tkinter Window ============================

root = tk.Tk()
root.title("DES Encryption - GUI Fixed")

frame = ttk.Frame(root, padding=12)
frame.grid(sticky="nsew")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(frame, text="Plaintext / Cipher (HEX for Decrypt):").grid(column=0, row=0, sticky="w", pady=(0,6))
entry_plain = ttk.Entry(frame, width=60)
entry_plain.grid(column=1, row=0, padx=(6,0), sticky="w", pady=(0,6))

ttk.Label(frame, text="Key (max 8 chars):").grid(column=0, row=1, sticky="w", pady=(0,6))
entry_key = ttk.Entry(frame, width=24)
entry_key.grid(column=1, row=1, padx=(6,0), sticky="w", pady=(0,6))

button_frame = ttk.Frame(frame)
button_frame.grid(column=0, row=2, columnspan=2, pady=(6,10))

btn_encrypt = tk.Button(button_frame, text="Encrypt", bg="#4CAF50", fg="white",
                        width=12, command=encrypt_gui)
btn_encrypt.grid(column=0, row=0, padx=6)

btn_decrypt = tk.Button(button_frame, text="Decrypt", bg="#2196F3", fg="white",
                        width=12, command=decrypt_gui)
btn_decrypt.grid(column=1, row=0, padx=6)

btn_reset = tk.Button(button_frame, text="Reset", bg="#FF9800", fg="white",
                      width=12, command=reset_gui)
btn_reset.grid(column=2, row=0, padx=6)

btn_exit = tk.Button(button_frame, text="Keluar", bg="#F44336", fg="white",
                     width=12, command=exit_gui)
btn_exit.grid(column=3, row=0, padx=6)

output = scrolledtext.ScrolledText(frame, width=100, height=28, wrap='none')
output.grid(column=0, row=3, columnspan=2, pady=(6,0))
output.configure(state='disabled')

frame.columnconfigure(0, weight=0)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(3, weight=1)

root.mainloop()
