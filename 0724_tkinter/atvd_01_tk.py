import tkinter as tk

#cria a janela principal
root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")

#Cria um rótulo (label) com o texto "Hello, World!"
message = tk.Label(root, text="Hello, World!")
message2 = tk.Label(root, text="Olá, Mundo!")

#posiciona o rótulo na janela
message.pack()
message2.pack()

#define o tamanho da janela (largura x altura + posição x + posição y)
root.geometry("400x200+50+250")

#inicia o loop principal da interface grafica
root.mainloop()