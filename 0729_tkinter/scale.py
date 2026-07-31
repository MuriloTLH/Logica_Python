import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("SENAI-Sistemas")
root.geometry("400x300")

def valor_mudou(evento):
    label.config(text=evento)
    
scale = tk.Scale(root,
    from_=0,
    to=10,
    orient="vertical",
    command=valor_mudou)
scale.pack()

label = tk.Label(root, text="0")
label.pack()

root.mainloop()