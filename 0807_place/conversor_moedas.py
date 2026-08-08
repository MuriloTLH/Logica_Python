import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("SENAI - Sistemas")
root.geometry("350x220")

l_valor = tk.Label(root, text="Valor: ")
l_valor.grid(row=0, column=0, sticky="w", padx=6, pady=6)

l_moeda_or = tk.Label(root, text="Moeda de Origem: ")
l_moeda_or.grid(row=1, column=0, sticky="w", padx=6, pady=6)

l_moeda_des = tk.Label(root, text="Moeda de Destino: ")
l_moeda_des.grid(row=2, column=0, sticky="w", padx=6, pady=6)

entry_valor = tk.Entry(root)
entry_valor.grid(row=0, column=1, sticky="s", padx=6, pady=6)

combo_mo = ttk.Combobox(root, values=["BRL", "USD", "JPY"], state="readonly")
combo_mo.grid(row=1, column=1, sticky="e", padx=6, pady=6)

combo_md = ttk.Combobox(root, values=["BRL", "USD", "JPY"], state="readonly")
combo_md.grid(row=2, column=1, sticky="e", padx=6, pady=6)

def button_command():
    valor = entry_valor.get() 
    messagebox.showinfo("Info", valor)

converter = tk.Button(root, text="Converter", command=button_command)
converter.grid(row=3, column=0, rowspan=2, columnspan=2, sticky="ew", padx=6, pady=6)

root.mainloop()