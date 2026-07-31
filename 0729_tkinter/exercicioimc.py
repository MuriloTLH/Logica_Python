import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("SENAI-Sistemas")
root.geometry("400x300")

peso = tk.Label(root, text="peso[Kg]")
peso .pack()

peso_e = tk.Entry(root)
peso_e.bind("<<Return>>")
peso_e.pack()


altura = tk.Label(root, text="Altura(m)")
altura.pack(
    # expand=True
    )

altura_e = tk.Entry(root)
altura_e.bind("<<Return>>")
altura_e.pack()

# def calcular_peso():
    

    
calcular = tk.Button(
    root,
    text="calcular"
    # command=
    )
calcular.pack()

root.mainloop()