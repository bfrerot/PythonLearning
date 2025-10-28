import tkinter as tk
from tkinter import messagebox


def question():
    answer = messagebox.showwarning("Be careful!", "Big Brother is watching you!") # print the msg with a warning icon 
    print(answer) # prints 'ok' when the user clicks 'OK' or closes the dialog


window = tk.Tk()
button = tk.Button(window, text="What's going on?", command=question)
button.pack()
window.mainloop()
# ok
# ok