import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("SENAI - Sistemas")
root.geometry("550x300")
root.config(bg="black")


minha_imagem = tk.PhotoImage(file="pngwing.com.png").subsample(4, 4)
img = tk.Label(root, image=minha_imagem, relief=tk.RAISED)
img.grid(row=0, column=0, rowspan= 5, sticky="ew", padx=5, pady=5)

l_nome = tk.Label(root, text="Nome: ")
l_nome.grid(row=0, column=1, sticky="e", padx=5, pady=5)

l_genero = tk.Label(root, text="Gênero: ")
l_genero.grid(row=1, column=1, sticky="e", padx=5, pady=5)

l_cor_olhos = tk.Label(root, text="Cor dos olhos: ")
l_cor_olhos.grid(row=2, column=1, sticky="e", padx=5, pady=5)

l_altura = tk.Label(root, text="Altura(cm): ")
l_altura.grid(row=3, column=1, sticky="e", padx=5, pady=5)

l_peso = tk.Label(root, text="Peso(kg): ")
l_peso.grid(row=4, column=1, sticky="e", padx=5, pady=5)

entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=2, sticky="ew", padx=5, pady=5)

combo_genero = ttk.Combobox(root, values=["Homi", "Muie"], state="readonly")
combo_genero.grid(row=1, column=2, sticky="ew", padx=5, pady=5)

combo_cor = ttk.Combobox(root, values=["Azul", "Castanho"], state="readonly")
combo_cor.grid(row=2, column=2, sticky="ew", padx=5, pady=5)

entry_altura = tk.Entry(root)
entry_altura.grid(row=3, column=2, sticky="ew", padx=5, pady=5)

entry_peso = tk.Entry(root)
entry_peso.grid(row=4, column=2, sticky="ew", padx=5, pady=5)

enviar = tk.Button(text="Enviar")
enviar.grid(row=5, column=2, sticky="e", padx=5, pady=5)

root.mainloop()