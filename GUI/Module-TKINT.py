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



### colours


## bg “background-color” and fg “foreground-color”

import tkinter as tk

window = tk.Tk()
button = tk.Button(window, text="Button #1", bg="red", fg="yellow") # bg= messabox colour, fg= policy colour
button.pack()
window.mainloop()


## activeforeground and activebackground
# the same but when we point or click on the button

import tkinter as tk


window = tk.Tk()
button = tk.Button(window, text="Button #1",
                   bg="MediumPurple",
                   fg="LightSalmon",
                   activeforeground="yellow",
                   activebackground="red")
button.pack()
window.mainloop()


## RGB, notions

# primary colours RGB ==|  RED   GREEN  BLUE
#                         0-255  0-255  0-255
#                           0      0      0    = black
#                          255    255    255   = white
#                          255     0      0    = red
#                           0     255     0    = green
#                           0      0     255   = blue

# intermediate colours for RGB with more than 1 non-zero component

# to represent RGBs value we do use hexadecimal 
# 0-->F * 2 for each
# RR GG BB
# FF FF FF = white
# 00 00 00 = black
# each color has:
# - a name
# - an hexadecimal value

import tkinter as tk

window = tk.Tk()
button = tk.Button(window, text="Button #1",
                   bg="#9370DB",
                   fg="#FFA07A",
                   activeforeground="#FFF0F5",
                   activebackground="#FF69B4")
button.pack()
window.mainloop()



### .Label()

# non-clickable widget able to present short textual information passed to the widget's constructor using a text argument

import tkinter as tk

window = tk.Tk()

label = tk.Label(window, text = "Little label:")
label.pack()

window.mainloop()



### .Frame()

# non-clickable component used to group widgets and to separate them (visually) from other window components

import tkinter as tk

window = tk.Tk()

label = tk.Label(window, text="Little label:")
label.pack()

frame = tk.Frame(window, height=30, width=100, bg="#000099")
frame.pack()

window.mainloop()



### fill=tk.X/Y/BOTH/NONE

# tk.X = fills horizontally
# tk.Y = fills vertically
# tk.BOTH = fills both ways
# tk.NONE = no extension => widget keeps its default size

import tkinter as tk

window = tk.Tk()

label = tk.Label(window, text="Little label:")
label.pack()

frame = tk.Frame(window, height=30, width=100, bg="#000099")
frame.pack()

button = tk.Button(window, text="Button")
button.pack(fill=tk.X)

window.mainloop()



### .IntVar()

# designed to store integer values
# Objects of the IntVar class are used by tkinter to organize internal communication between different widgets
# to store an integer value the class offers a dedicated method set()

window = tk.Tk()

label = tk.Label(window, text="Little label:")
label.pack()

frame = tk.Frame(window, height=5, width=100, bg="#000099")
frame.pack()

button = tk.Button(window, text="Button")
button.pack(fill=tk.X)

switch = tk.IntVar()
switch.set(1)

window.mainloop()



### Checkbutton()

# small square which can be filled with a tick mark, or which can be empty
# primarily used to represent two-state selections


import tkinter as tk

win = tk.Tk()

label = tk.Label(win, text="Little label:")
label.pack()

frame = tk.Frame(win, height=5, width=100, bg="#000099")
frame.pack()

button = tk.Button(win, text="Button")
button.pack(fill=tk.X)

switch = tk.IntVar()
switch.set(1) # the box will be ticked by default

checkbutton = tk.Checkbutton(win, text="Check Button", variable=switch)
checkbutton.pack()

win.mainloop()



### Entry()

# designed to let the user enter simple, one-line data, like single numbers, names, addresses, etc
# 

import tkinter as tk

window = tk.Tk()

label = tk.Label(window, text="Little label:")
label.pack()

frame = tk.Frame(window, height=30, width=100, bg="#000099")
frame.pack()

button = tk.Button(window, text="Button")
button.pack(fill=tk.X)

switch = tk.IntVar()
switch.set(1)

checkbutton = tk.Checkbutton(window, text="Check Button", variable=switch)
checkbutton.pack()

entry = tk.Entry(window, width=30)
entry.pack()

window.mainloop()



### Radiobutton()

# small circles filled with a dot or not
# The most important difference between Checkbutton and Radiobuttons lies in the fact that Checkbuttons work individually
#   while Radiobuttons always work in groups and only one of the widgets inside the group can be checked
# Clicking an unchecked member of the group will cause the currently checked Radiobutton to change its state

# we can bind a variable to Radiobutton, to change this variable state

import tkinter as tk

window = tk.Tk()

label = tk.Label(window, text="Little label:")
label.pack()

frame = tk.Frame(window, height=30, width=100, bg="#000099")
frame.pack()

button = tk.Button(window, text ="Button")
button.pack(fill=tk.X)

switch = tk.IntVar()
switch.set(1)

checkbutton = tk.Checkbutton(window, text="Check Button", variable=switch)
checkbutton.pack()

entry = tk.Entry(window, width=30)
entry.pack()

radiobutton_1 = tk.Radiobutton(window, text="Steak", variable=switch, value=0)  # radiobutton block, only 1 can be selected
radiobutton_1.pack()             
radiobutton_2 = tk.Radiobutton(window, text="Salad", variable=switch, value=1)  # set "switch" variable to 1 (= ticked)
radiobutton_2.pack()

window.mainloop()



### Event handling

# All events come to the event manager which is responsible for dispatching them to all the application components
# This also means that some of the events may launch some of our callbacks, which makes us responsible for preparing the proper reactions to the user’s actions

## Events

'''
EVENT NAME	           EVENT ROLE

<Button-1>	           Single left-click (if our mouse is configured for a right-handed user)
<Button-2>	           Single middle-click
<Button-3>	           Single right-click
<ButtonRelease-1>	   Left mouse button release
<ButtonRelease-2>      Middle mouse button release
<ButtonRelease-3>      Right mouse button release
<DoubleButton-1>	   Double left-click
<DoubleButton-2>	   Double middle-click
<DoubleButton-3>	   Double right-click
<Enter>	               Mouse cursor appears over the widget
<Leave>	               Mouse cursor leaves the widget area
<Focus-In>	           The widget gains the focus
<Focus-Out>	           The widget loses the focus
<Return>	           The user presses the Enter/Return key
<Key>	               The user presses any key
x	                   The user presses x key (x can be neither a space nor the < key)
<space>	               The user presses the spacebar
<less>	               The user presses the < key
<Cancel>	           The user presses the key/keys used by the current OS to stop the program ==> Ctrl-C or Ctrl-Break
<BackSpace>	           The user presses the Backspace key
<Tab>	               The user presses Tab key
<Prior>	               The Page Up key
<Next>	               The Page Down key
<End>	               The End key
<Home>	               The Home key

<Left>
<Right>
<Up>
<Down>	Cursor (arrows) keys

<Num_Lock>

<Scroll_Lock>	The two Lock keys

<Shift-x>

<Alt-x>

<Control-x>	The x key has been pressed 
'''


## messagebox.showinfo(title, info)

# title = title of the message box which will appear on the screen, can be empty
# info  = message to display inside the box, can be of any length, we can use the \n digraph to visually break the info into separate lines

import tkinter
from tkinter import messagebox

def clicked():
    messagebox.showinfo("info", "some\ninfo")

window = tkinter.Tk()
button_1 = tkinter.Button(window, text="Show info", command=clicked) # "clicked" function defined above is invoked here
button_1.pack()
button_2 = tkinter.Button(window, text="Quit", command=window.destroy)
button_2.pack()
window.mainloop()


## with label/button/frame

import tkinter as tk
from tkinter import messagebox

def click():
    tk.messagebox.showinfo("Click!","I love clicks!")

window = tk.Tk()
label = tk.Label(window, text="Label")
label.pack()

button = tk.Button(window, text="Button", command=click)
button.pack(fill=tk.X) # means it will fill horizontally

frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame.pack()

window.mainloop()


## widget.bind(event, callback)

# event    = event we want to launch our callback with
# callback = the callback itself

# From the event controller’s point of view, an event is an object carrying some useful info about what actually happens when the event has been induced by a user or another factor
# Events are identified by unique names, each event has its own name and the name is just a unified string

# a callback designed for usage with the command property/parameter == parameterless function
# a callback intended to cooperate with the bind() method           == one-parameter function 
#   (the callback’s argument carries some info about the captured event)
