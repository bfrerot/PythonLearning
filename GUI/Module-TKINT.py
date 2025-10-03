########## TKINT MODULE ##########


import tkinter


# The GUI application itself consists of four essential elements:
#  - importing the needed tkinter components
#  - creating an application’s main window
#  - adding a set of necessary widgets to the window
#  - launching the event controller



### basic empty

skylight = tkinter.Tk() # main application window is created by the tkinter method named Tk()
skylight.mainloop() # starts the controller



### setting a title


skylight = tkinter.Tk()
skylight.title("Skylight")
skylight.mainloop()



### setting a button

# To bring a button to life we have to:
#   - create a Button class object (it'll be done by the class's constructor)
#   - place the button inside the main window (it'll be done by one of the window's methods)
#   - Note the distinction: it can be said that the button creates itself, but to make it visible, we need the window's method

import tkinter

skylight = tkinter.Tk()       # creates the window
skylight.title("Skylight")    # creates the window's title
button = tkinter.Button(skylight, text="Bye!")     # creates a button into "skylight" window, and names it with text value
button.place(x=10, y=10)                           # button's position
skylight.mainloop()



### event handler

# An event handler is a piece of code responsible for responding to all clicks addressed to buttons
# This operation is done with a main window method called "destroy()" = parameterless method
# This function will be invoked only by the controller
# we call it "handler" or "callback" ==> when exectuted by someone/somethingelse
import tkinter

def Click():                 # function to associate action to button
    skylight.destroy();
    
skylight = tkinter.Tk()
skylight.title("Skylight")
button = tkinter.Button(skylight, text="Bye!", command=Click)
button.place(x=10, y=10)
skylight.mainloop()



### messagebox

# permits to interact with user



### settling widgets

# 3*methods
#   - place() => forces to precisely declare a widget's location, pixel by pixel
#                however, doesn't protect from common mistakes causing widgets to overlap each other or to place some of them, partially or fully, outside the window
#   - pack() => tries to guess the developer's intentions and to find the best location for each widget
#   - grid() => permits to express general wishes and tries to deploy the widgets according to them


## place()

# height=h = the widget's desired height measured in pixels; if the parameter is omitted, the widget's height will be determined automatically
# width=w  = the widget's desired width measured in pixels; if the parameter is omitted, the widget's width will be determined automatically
# x=x      = the widget's top-left pixel's horizontal coordinate measured relative to the home window's top-left corner
# y=y      = the widget's top-left pixel's vertical coordinate measured relative to the home window's top-left corner

import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")
button_1.place(x=10, y=10)   # x from left to right, y from up to down
button_2.place(x=20, y=40)
button_3.place(x=30, y=90)
window.mainloop()


## grid()

# column=c        = deploys the widget in the column number c; start from zero, and if we omit this argument, the manager will assume 0 (the left-most column)
# row=r           = deploys the widget in the row number r; if we omit this argument, the manager will assume the first free row starting from the top
# columnspan=cs   = determines how many neighboring columns the widget occupies; the parameter defaults to 1 (the widget won't cross a single grid's cell)
# rowspan=rs      = works as columnspan but refers to rows

import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")
button_1.grid(row=0, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=2, column=2)
window.mainloop()

# if a duplicate, the last is on the top
button_2.grid(row=1, column=0)
button_3.grid(row=1, column=0)  # ==> this one will appear

# we cannot jump columns
button_1.grid(row=0, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=2, column=5) # => remains on column 2

# to play with placement, with columnspan
button_1.grid(row=0, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=2, column=0, columnspan=2) # manager will consider the window has 2 columns


## pack()

# side = s – forces the manager to pack the widgets in a specified direction, where s can be specified as:
#       TOP – the widget is packed toward the window's top = default
#       BOTTOM – the widget is packed toward the window's bottom
#       LEFT – toward the window's left boundary
#       RIGHT – toward the window's right boundary

# fill = f – suggests to the manager how to expand the widget if you want it to occupy more space than the default, while f should be specified as:
#        NONE – do not expand the widget = default
#        X – expand it in the horizontal direction
#        Y – expand it in the vertical direction
#        BOTH – expand it in both directions

import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")
button_1.pack()
button_2.pack()
button_3.pack()
window.mainloop()

# use of side
button_1.pack(side=tk.RIGHT)
button_2.pack()
button_3.pack()

