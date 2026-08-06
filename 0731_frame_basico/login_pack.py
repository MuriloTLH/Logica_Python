import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("SENAI - Sistemas")
root.geometry("300x400")

def button_command():
    nome = message1.get()
    messagebox.showinfo("Login", nome)

checkbox_estado = tk.IntVar()

def mostrar_estado():
    checkbox.config(
        text=f"Lembrar-me")
checkbox = tk.Checkbutton(root,
    text="Lembrar-me",
    variable=checkbox_estado,
    command=mostrar_estado)





label1 = tk.Label(root, text="Faça seu login",font=("Helvetica", 30))
label1.pack()

minha_imagem = tk.PhotoImage(file="pngwing.com.png").subsample(6, 6)
label2 = tk.Label(root, image=minha_imagem)
label2.pack(expand=False)

usuario = tk.Label(root, text="Usuário")
message1 = tk.Entry(root)
message2 = tk.Entry(root)
senha = tk.Label(root, text="Senha")
button = tk.Button(root, text="Entrar", command=button_command)



usuario.pack(anchor="w", padx=30)
message1.pack()
senha.pack(anchor="w", padx=30)
message2.pack()
button.pack()
checkbox.deselect()
checkbox.pack(padx=20, side="left")
tk.Label(root, text="Esqueceu sua senha?", fg="blue", cursor="hand2").pack(side="right", padx=20)



root.mainloop()