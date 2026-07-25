import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.geometry("400x300")

#conteúdo do botão
def button_command():
    messagebox.showinfo(
        "informação",
        "Você clicou no botão!"
    )

#conteúdo do botão
def button_command2():
    messagebox.showwarning(
        "Aviso",
        "Seu cartão foi clonado"
    )

#criar o botão
button = tk.Button(
    root,
    text="Clique aqui",
    command=button_command
)

#criar o botão
button2 = tk.Button(
    root,
    text="Clique aqui",
    command=button_command2
)

#exibir os botões
button.pack()
button2.pack()

root.mainloop()