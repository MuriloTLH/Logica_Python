import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("SENAI-Sistemas")
root.geometry("400x300")

def calcular_imc():
    valor_peso = float(peso_e.get())
    valor_altura = float(altura_e.get())
    
    resultado = valor_peso / (valor_altura ** 2)

    if resultado <= 18.5:
        exibe_class.config(text="Abaixo do peso")
    elif resultado <= 24.9:
        exibe_class.config(text="Saudável")
    elif resultado <= 29.9:
        exibe_class.config(text="Sobrepeso")
    elif resultado >= 30:
        exibe_class.config(text="Obesidade")
    res.config(text=f"IMC: {resultado:.1f}")

peso = tk.Label(root, text="peso[Kg]")
peso .pack()

peso_e = tk.Entry(root)
peso_e.bind("<<Return>>")
peso_e.pack()

altura = tk.Label(root, text="Altura(m)")
altura.pack()

altura_e = tk.Entry(root)
altura_e.bind("<<Return>>")
altura_e.pack()

calcular = tk.Button(
    root,
    text="calcular",
    command=calcular_imc
    )
calcular.pack()

res = tk.Label(root, text="Preencha os campos")
exibe_class = tk.Label(root, text=" ")

res.pack()
exibe_class.pack()


root.mainloop()