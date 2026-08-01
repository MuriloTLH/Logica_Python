import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("SENAI - Sistemas")
root.geometry("340x100")

tk.Button(root, text="Top Button!").pack()
tk.Label(root, text="Hello, Left!").pack(side="left")
tk.Label(root, text="Hello, Right!").pack(side="right")
tk.Checkbutton(root, text="Uma opção na parte inferior!").pack(side=tk.BOTTOM)

root.mainloop()