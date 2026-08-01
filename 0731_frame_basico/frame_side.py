import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("SENAI - Sistemas")
root.config(bg="skyblue")

frame = tk.Frame(root, width=420, height=220)
frame.pack(padx=10, pady=10)

a_frame = tk.Frame(frame, width=190, height=190, bg="red")
a_frame.pack(side="top", padx=10, pady=10)

#->SIDE<- PODE SER ALTERADO POR: TOP, BOTTOM, LEFT, RIGHT

b_frame = tk.Frame(frame, width=190, height=190, bg="green")
b_frame.pack(side="bottom", padx=10, pady=10)


root.mainloop()