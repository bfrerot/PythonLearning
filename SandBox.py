import tkinter as tk
from tkinter import messagebox

def hello(dummy):
    messagebox.showinfo("", "Hello!")

window = tk.Tk()
button = tk.Button(window, text="On/Off")
button.pack()
label = tk.Label(window, text="Label")
label.pack()
frame = tk.Frame(window, bg="yellow", width=100, height=20)
frame.pack()
window.bind_all("<Button-1>", hello)
window.mainloop()