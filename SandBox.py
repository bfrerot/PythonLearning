import tkinter as tk

def digits_only(*args):
    global last_string        
    string = text.get()
    if string == '' or string.isalnum() :  # Field's content is valid.
        last_string = string
    else:
        text.set(last_string)

last_string = ''
window = tk.Tk()
text = tk.StringVar()
entry = tk.Entry(window, textvariable=text)
text.set(last_string)
text.trace_add('write', digits_only)
entry.pack()
entry.focus_set()
window.mainloop()
