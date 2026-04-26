import tkinter as tk
from tkinter import ttk, messagebox

def proses_rekomendasi():
    risiko = combo_risiko.get()
    target_waktu = combo_target_waktu.get()
    try:
        input_teks = entry_profit.get().replace("%", "").strip() 
        profit = float(input_teks)
    except ValueError:
        messagebox.showwarning("Peringatan", "Harap masukkan angka yang valid untuk Target Profit.")
        return

    if not risiko or not target_waktu:
        messagebox.showwarning("Peringatan", "Harap lengkapi semua kriteria identifikasi.")
        return

    instrumen = ""
    alasan = ""

    if profit >= 20 and risiko == "Agresif (Risiko Tinggi)":
        instrumen = "Aset Kripto (Bitcoin/Ethereum)"
        alasan = f"Target profit {profit}% sesuai dengan histori volatilitas Crypto (20-200%)."

    elif 1 <= profit <= 150 and risiko in ["Moderat (Risiko Menengah)", "Agresif (Risiko Tinggi)"]:
        if target_waktu == "Jangka Pendek (< 1 Tahun)":
            instrumen = "Saham Trading (Scalping/Day Trade)"
        else:
            instrumen = "Saham Investasi (Bluechip/Growth Stock)"
        alasan = f"Target profit {profit}% masuk dalam rentang pertumbuhan saham (1-150%)."

    elif 2 <= profit <= 25:
        if risiko == "Konservatif (Risiko Rendah)":
            instrumen = "Reksa Dana Pasar Uang atau SBN"
        else:
            instrumen = "Reksa Dana Campuran / Saham"
        alasan = f"Target profit {profit}% ideal untuk instrumen Reksa Dana (2-25%) yang lebih stabil."

    else:
        instrumen = "Diversifikasi Portofolio"
        alasan = "Target profit dan profil risiko Anda memerlukan kombinasi beberapa instrumen."

    label_hasil.config(text=instrumen)
    label_alasan.config(text=alasan)

root = tk.Tk()
root.title("Sistem Pakar - Rekomendasi Instrumen Investasi")
root.geometry("1200x600")
root.configure(bg="#0d1117")

style = ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground="#161b22", background="#30363d", 
                foreground="black", bordercolor="#30363d", arrowcolor="black", padding=5)

tk.Label(root, text="Rekomendasi Instrumen Investasi", font=("Poppins", 16, "bold"), 
         bg="#0d1117", fg="#58a6ff").pack(pady=(25, 15))

tk.Label(root, text="Identifikasi Profil Risiko:", font=("Poppins", 10, "bold"), 
         bg="#0d1117", fg="#c9d1d9").pack(anchor="w", padx=50)
combo_risiko = ttk.Combobox(root, values=[
    "Konservatif (Risiko Rendah)", 
    "Moderat (Risiko Menengah)", 
    "Agresif (Risiko Tinggi)"
], state="readonly", width=40, font=("Poppins", 10))
combo_risiko.pack(pady=5, padx=50)

tk.Label(root, text="Target Horizon Return:", font=("Poppins", 10, "bold"), 
         bg="#0d1117", fg="#c9d1d9").pack(anchor="w", padx=50, pady=(10, 0))
combo_target_waktu = ttk.Combobox(root, values=[
    "Jangka Pendek (< 1 Tahun)", 
    "Jangka Menengah (1 - 3 Tahun)", 
    "Jangka Panjang (> 3 Tahun)"
], state="readonly", width=40, font=("Poppins", 10))
combo_target_waktu.pack(pady=5, padx=50)

tk.Label(root, text="Target Profit Tahunan (%):", font=("Poppins", 10, "bold"), 
         bg="#0d1117", fg="#c9d1d9").pack(anchor="w", padx=50, pady=(10, 0))
entry_profit = tk.Entry(root, width=43, font=("Poppins", 10), bg="#161b22", fg="white", 
                        insertbackground="white", borderwidth=1, relief="solid")
entry_profit.pack(pady=5, padx=50)
tk.Label(root, text="Contoh: 15 untuk 15%", font=("Poppins", 8), bg="#0d1117", fg="#8b949e").pack(anchor="w", padx=50)

btn = tk.Button(root, text="Analisis Instrumen", command=proses_rekomendasi, 
                bg="#238636", fg="white", font=("Poppins", 10, "bold"), 
                relief="flat", activebackground="#2ea043", activeforeground="white", cursor="hand2")
btn.pack(pady=20, ipadx=15, ipady=8)

tk.Label(root, text="Rekomendasi Utama:", font=("Poppins", 9), 
         bg="#0d1117", fg="#8b949e").pack()
label_hasil = tk.Label(root, text="-", font=("Poppins", 13, "bold"), 
                       bg="#0d1117", fg="#58a6ff")
label_hasil.pack(pady=2)

label_alasan = tk.Label(root, text="", font=("Poppins", 9, "italic"), 
                        bg="#0d1117", fg="#c9d1d9", wraplength=400, justify="center")
label_alasan.pack(pady=5)

root.mainloop()
