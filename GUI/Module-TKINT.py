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

PROPERTY NAME    	PROPERTY ROLE
widget	            The widget’s object (not the widget’s name!) to which the event is addressed

<x>
<y>	                The mouse cursor’s coordinates at the moment of the event’s occurrence (both coordinates are counted relative to the target widget)

<x_root>
<y_root>	        As above, but relative to the screen

<char>	            The pressed key character code (only for keyboard events)
<keysym>	        The pressed key symbol (only for keyboard events)
                    ==> full list of all recognized key symbols: https://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm
 
<keycode>	        The pressed key numerical code (only for keyboard events)
                    Don’t confuse this with char, which is the ASCII/UNICODE code of the character bound to the key
                    
<num>	            The number of the clicked mouse button (only for mouse events)
<type>	            The event’s type
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

import tkinter as tk
from tkinter import messagebox

def click(event=None):
    tk.messagebox.showinfo("Click!", "I love clicks!")

window = tk.Tk()
label = tk.Label(window, text="Label")
label.bind("<Button-1>", click)   # if we click on the "label", click function will execute
label.pack()

button = tk.Button(window, text="Button", command=click)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame.bind("<Button-1>", click)   # if we click on the "frame", click function will execute
frame.pack()

window.mainloop()


# using events code to see what's occuring
# if we click on label or frame, it will send a message with cursor coordinates x and y + event num and type
# ex: x=31, y=15, num=1, type=4

def click(event=None):
    if event is None:
        tk.messagebox.showinfo("Click!", "I love clicks!")
    else:
        string = "x=" + str(event.x) + ",y=" + str(event.y) + \
                 ",num=" + str(event.num) + ",type=" + event.type
        tk.messagebox.showinfo("Click!", string)        

window = tk.Tk()
label = tk.Label(window, text="Label")
label.bind("<Button-1>", click)
label.pack()

button = tk.Button(window, text="Button", command=click)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame.bind("<Button-1>", click)
frame.pack()

window.mainloop()



### widget.config()

# If we want to modify a property named prop, existing within a widget named "wid", and we’re going set its value to "val"
#   we can use the config() method: wid.config(prop=val)

# if we want to unbind our current callback from a Button named b1
#   we would use an invocation like this one: b1.config(command=lambda:None)
# This binds an empty function to the widget’s callback

import tkinter as tk
from tkinter import messagebox


def on_off():
    global switch
    if switch:
        button_2.config(command=lambda: None) # if we press button_2, nothings occurs (None)
        button_2.config(text="Gee!") # button_2 name changes to "Gee!""
    else:
        button_2.config(command=peekaboo)
        button_2.config(text="Peekaboo!")
    switch = not switch # reverse the swhitch variable value( True to False or False to True)

def peekaboo():
    messagebox.showinfo("", "PEEKABOO!")

def do_nothing():
    pass

switch = True
window = tk.Tk()
buton_1 = tk.Button(window, text="On/Off", command=on_off)
buton_1.pack()
button_2 = tk.Button(window, text="Peekaboo!", command=peekaboo)
button_2.pack()
window.mainloop()



### widget.unbind()

# To unbind a callback previously bound with the bind() method invocation we need to use 
#   the unbind() method ==> widget.unbind(event)
# The method requires one argument identifying the event being unbound
# Any the information about a previously used callback is lost
# We cannot retrieve it automatically and we must repeat the bind() invocation

import tkinter as tk

def on_off():
    global switch
    if switch:
        label.unbind("<Button-1>") # 
    else:
        label.bind("<Button-1>", rhyme)
    switch = not switch

def rhyme(dummy):
    global word_no, words
    word_no += 1
    label.config(text=words[word_no % len(words)])

switch = True
words = ["Old", "McDonald", "Had", "A", "Farm"]
word_no = 0
window = tk.Tk()
button = tk.Button(window, text="On/Off", command=on_off)
button.pack()
label = tk.Label(window, text=words[0])
label.bind("<Button-1>", rhyme) # Button-1 is the mouse left click event
label.pack()
window.mainloop()



### bind_all()/unbind_all()

# bind_all() == binds a callback to all currently existing widgets
# window.bind_all(event, callback)

# unbind_all() == unbinds all currently existing binds
# window.unbind_all(event)

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



### Interact with widgets properties

## using the widget dictionnary

import tkinter as tk

def on_off():                # 2- 1st click
    global button
    state = button["text"]   # 2.1 state = OFF
    if state == "ON":   
        state = "OFF"
    else:                    # 2.2 state switches to ON
        state = "ON"
    button["text"] = state   # 2.3 button "text" property changes to ON

window = tk.Tk()
button = tk.Button(window, text="OFF", command=on_off) # 1- starts in state = OFF
button.place(x=50, y=100, width=100)
window.mainloop()


## .cget() / .config()

import tkinter as tk

def on_off():
    global button
    state = button.cget("text")
    if state == "ON":
        state = "OFF"
    else:
        state = "ON"
    button.config(text=state)

window = tk.Tk()
button = tk.Button(window, text="OFF", command=on_off)
button.place(x=50, y=100, width=100)
window.mainloop()


## font

# ("font_family_name", "font_size")
# ("font_family_name", "font_size", "font_style")

# font_family_name ==> str
# font_size ==> in points but str
# font_style
#   "bold" "italic" "underline" "overstrike"

# default font ==
#   family     = "Segoe_UI"
#   size       = "9"
#   weight     = "normal"
#   slant      = "roman"
#   underline  = False
#   overstrike = False

import tkinter as tk

window = tk.Tk()
label_1 = tk.Label(window, text="Quick brown fox jumps over the lazy dog")
label_1.grid(column=0, row=0)
label_2 = tk.Label(window, text="Quick brown fox jumps over the lazy dog", font=("Times", "12"))
label_2.grid(column=0, row=1)
label_3 = tk.Label(window, text="Quick brown fox jumps over the lazy dog", font=("Arial", "16", "bold"))
label_3.grid(column=0, row=2)
window.mainloop()


## widget sizes

'''
WIDGET PROPERTY NAME	  PROPERTY ROLE
borderwidth               The width of the 3D-frame surrounding some widgets (e.g., Button)
highlightthickness	      The width of the additional frame drawn around the widget when it gains the focus

padx
pady	                  The width/height of an additional empty space/margin around the widget

wraplength	              If the text filling the widget becomes longer than this property’s value, it will be wrapped (possibly more than once)
height	                  The height of the widget
underline                 The index of the character inside the widget’s text, which should be presented as underlined or -1 otherwise (the underlined letter/digit can be used as a shortcut key, but it needs a specialized callback to work – no automation here, sorry)
width	                  The width of the widget
'''

import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Ordinary button");
button_1.pack()
button_2 = tk.Button(window, text="Exceptional button")
button_2.pack()
button_2["borderwidth"] = 10
button_2["highlightthickness"] = 10
button_2["padx"] = 10
button_2["pady"] = 5
button_2["underline"] = 1
window.mainloop()


## widget colours

'''
WIDGET PROPERTY NAME	  PROPERTY ROLE
background
bg	                      The color of the widget’s background (you can freely use either of these two forms)

foreground
fg	                      The color of the widget’s foreground (note: it can mean different things in different widgets; in general, it’s used to specify text color)

activeforeground
activebackground	      Like bg and fg but used when the widget becomes active

disabledforeground	      The width of the widget
'''

import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Ordinary button");
button_1.pack()
button_2 = tk.Button(window, text="Colorful button")
button_2.pack()
button_2.config(bg ="#000000")
button_2.config(fg ="yellow")
button_2.config(activeforeground ="#FF0000")
button_2.config(activebackground ="green")
window.mainloop()


## anchor

# Imaginary (invisible) point inside the widget to which the text (if any) is anchored
# Widgets tend to put their text in the middle of themselves (both in horizontal and vertical directions)
# Location of the anchor can easily be changed, as there is a property of the same name

# 9*possible locations : 
#  NW   N    NE
#   W Center E
#  SW   N    SE

import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Regular button");
button_1["anchor"] = tk.E
button_1["width"] = 20  # pixels!
button_1.pack()
button_2 = tk.Button(window, text="Another button")
button_2["anchor"] = tk.SW
button_2["width"] = 20
button_2["height"] = 3  # rows
button_2.pack()
window.mainloop()


## cursor

# to change cursor appearance when going over a label/button/frame
'''
arrow
based_arrow_down
based_arrow_up
boat
bogosity
bottom_left_corner
bottom_right_corner
bottom_side
bottom_tee
box_spiral
center_ptr
circle
clock
coffee_mug
cross
cross_reverse
crosshair
diamond_cross
dot
dotbox
double_arrow
draft_large
draft_small
draped_box
exchange
fleur
gobbler
gumby
hand1
hand2
heart
icon
iron_cross
left_ptr
left_side
left_tee
leftbutton
ll_angle
lr_angle
man
middlebutton
mouse
pencil
pirate
plus
question_arrow
right_ptr
right_side
right_tee
rightbutton
rtl_logo
sailboat
sb_down_arrow
sb_h_double_arrow
sb_left_arrow
sb_right_arrow
sb_up_arrow
sb_v_double_arrow
shuttle
sizing
spider
spraycan
star
target
tcross
top_left_arrow
top_left_corner
top_right_corner
top_side
top_tee
trek
ul_angle
umbrella
ur_angle
watch
xterm
'''

import tkinter as tk

window = tk.Tk()
label_1 = tk.Label(window, height=3, text="arrow", cursor="arrow")
label_1.pack()
label_2 = tk.Label(window, height=3, text="clock", cursor="clock")
label_2.pack()
label_3 = tk.Label(window, height=3, text="heart", cursor="heart")
label_3.pack()
window.mainloop()



### widget methods


## after()/after_cancel()

# Widget.after(time_ms, function)
# Widget.after_cancel(id)

# ==> after() 
# expects 2*arguments: 
#   1st is time interval specification, expressed in milliseconds: 1 s = 1000 ms
#   2nd points to an existing function; successful invocation of the method causes the event manager to change its plans
#       when the number of milliseconds elapses, the manager will invoke the function (only once)
#       this the only possible way of controlling the passage of time when using an event-driven environment

# ==> after_cancel(id) 
# cancels the planned invocation identified by the id argument


# infinite loop
import tkinter as tk

def blink():     # will loop for ever
    global is_white
    if is_white:
        color = 'black'
    else:
        color = 'white'
    is_white = not is_white
    frame.config(bg=color)
    frame.after(500, blink)  # due to this at the end

is_white = True
window = tk.Tk()
frame = tk.Frame(window, width=200, height=100, bg='white')
frame.after(500, blink)  # invokes "blink" function
frame.pack()
window.mainloop()


# terminating with after_cancel

import tkinter as tk

def blink():
    global is_white, id, count
    if count >= 20:
        window.after_cancel(id)
        return
    
    if is_white:
        color = 'black'
    else:
        color = 'white'
        
    is_white = not is_white
    
    frame.config(bg=color)
    count += 1
    id = window.after(500, blink)

is_white = True
count = 0

window = tk.Tk()
frame = tk.Frame(window, width=200, height=100)

frame.pack()

id = window.after(500, blink)  # invokes "blink" function

window.mainloop()


## .destroy()

# very destructive
# removes the widget completely from the event manager’s memory
# the widget’s object is deleted and becomes inaccessible

# if the widget we want to destroy has children (other widgets embedded inside it, ex: frames) 
# the children will be destroyed, too (this rule works recursively)

import tkinter as tk

def suicide():
    frame.destroy()

window = tk.Tk()
frame = tk.Frame(window, width=200, height=100, bg='green')
button = tk.Button(frame, text="I'm a frame's child")
# ==> button is child of frame wich is child of window
button.place(x=10, y=10)
frame.after(5000, suicide) # ==> will kill frame + its child button BUT window remains (empty)
frame.pack()
window.mainloop()


## focus

# wi.focus_get()
# wi.focus_set()

import tkinter as tk


def flip_focus():
    if window.focus_get() is button_1:
        button_2.focus_set()
    else:
        button_1.focus_set()
    window.after(1000, flip_focus)


window = tk.Tk()
button_1 = tk.Button(window, text="First")
button_1.pack()
button_2 = tk.Button(window, text="Second")
button_2.pack()
window.after(1000, flip_focus)
window.mainloop()



### observable variables

# works like a regular variable + something more => any change of the variable’s state can be observed by a number of external agents
# ex: Entry widget can use its own observable variable to inform other objects that the contents of the input field have been changed

# Technically such a variable is an object of the container class
# This means that a variable of that kind has to be explicitly created and initialized

# Another important difference => these variables are typed
# We have to be aware of what type of value we want to store in them, and don’t change our mind during the variable’s life

# We can only create an observable variable after the main window initialization


## tkinter observable variables

# BooleanVar    
# DoubleVar
# IntVar
# StringVar

# names are also the constructors’ names
# If we want to use any of the variables, you must invoke the proper constructor and save the returned object

# newly created variables are set to:
#   integer o for IntVar
#   float 0.0 for DoubleVar
#   Boolean False for BooleanVar
#   string "" for StringVar


## observers
 
# observable variable can be enriched with a number of "observers"
# An observer is a function (a kind of callback) which will be invoked automatically each time a specified event occurs in the variable’s life
# Number of observers is not limited
# Adding an observer to a variable is done by a method named trace():

# ==> obsid = variable.trace(trace_mode, observer)

# method takes 2*arguments:

# 1st = string describing which events should trigger an observer 
# possible values are:
#   "read" – if you want to be aware of the variable reads (accessing its value through get())
#   "write" – if you want to be aware of the variable writes (changing its value through set())
#   "unset" – if you want to be aware of the variable’s annihilation (removing the object through del)

# A reference to a function which will be invoked when the specified event occurs
# The function returns a string which is a unique observer identifier

import tkinter as tk

def r_observer(*args):  # "reading" observer function
    print("Reading")

def w_observer(*args):  # "writing" observer function
    print("Writing")

dummy = tk.Tk()    
# Create a window, mandatory to use variables like StringVar, even if print nothing, no dummy.mainloop() here
# Without this Tkinter does not work

variable = tk.StringVar()
# Create a StringVar variable 
# special Tkinter variable which is able to notify changes, useful for GUIs
# ex: update a label when a value changes

variable.set("abc") # defines variable value, here "abc"
r_obsid = variable.trace_add("read", r_observer)
w_obsid = variable.trace_add("write", w_observer)
variable.set(variable.get() + 'd')      # get=read followed by set=write, adds "d" to variable string
# Reading
# Writing
variable.trace_remove("read", r_obsid)  # removes the "read" observer
variable.set(variable.get() + 'e')      # adds "e" to variable string
# Writing
variable.trace_remove("write", w_obsid) # removes the "write" observer
variable.set(variable.get() + 'f')      # adds "f" to variable string
print(variable.get())
# abcdef



### WIDGETS lexicon

# Each tkinter widget is created by a constructor of its class
# The very 1st argument of the constructor invocation is always the master widget
# == the widget that owns the newly created object
# master widget is just the main window in most cases, but can be also a Frame or a LabelFrame 
# constructor accepts a set of arguments that configure the widget
# all widgets fall into two categories: clickable and non-clickable

# widget = Widget(master, option, ... )


## ==> CLICKABLE widgets

'''
BUTTON PROPERTY   	PROPERTY MEANING
command	            callback being invoked when the button is clicked
justify	            the way in which the inner text is justified: possible (self-describing) values are: LEFT, CENTER, and RIGHT
state	            if we set the property to DISABLED, the button becomes deaf and doesn’t react to clicks, while its title is shown in gray
                    setting it to NORMAL restores normal button functioning, when the mouse is located above the button, the property changes its value to ACTIVE

BUTTON METHOD	    METHOD ROLE
flash()	            the button flashes a few times but doesn’t change its state
invoke()	        activates the callback assigned to the widget and returns the same value the callback returned; note: this is the only way to invoke your own callback explicitly, as the event manager must be aware of the fact
'''


# Checkbutton 

'''
CHECKBUTTON PROPERTY 	PROPERTY MEANING
bd	                    checkbutton frame width (default is two pixels)
command	                callback being invoked when the checkbutton changes its state
justify	                same as for Button
state	                same as for Button
variable	            an observable IntVar variable reflecting the widget’s state; defaultly it’s set to 1 when the checkbutton is checked, and to 0 otherwise
offvalue	            non-default value being assigned to a variable when the checkbutton is not checked
onvalue	                non-default value being assigned to a variable when the checkbutton is checked


CHECKBUTTON METHOD      METHOD ROLE
deselect()	            unticks the widget
flash()	                same as for Button
invoke()	            same as for Button
select()	            ticks the widget
toggle()	            changes its state to the opposite one
'''


# Radiobutton

'''
RADIOBUTTON PROPERTY     	PROPERTY MEANING
command	                    callback being invoked when the Radiobutton (not the group it belongs to!) changes its state
justify	                    same as for Button
state	                    same as for Button
variable	                observable IntVar or StringVar variable reflecting the current selection within the Radiobutton’s group; changing the variable’s value automatically changes the selection
value	                    unique (inside the group) value identifying the Radiobutton; can be an integer value or a string, and should be compatible with the variable’s type

RADIOBUTTON METHOD      	METHOD ROLE
deselect()	                unchecks the widget
flash()	                    same as for Button
invoke()	                same as for Button
select()	                checks the widget
'''


import tkinter as tk

def switch():
    if button_1.cget('state') == tk.DISABLED: # DISABLED means no clickable but colour changes will continue to occur
        button_1.config(state=tk.NORMAL)
        button_1.flash()
    else:
        button_1.flash()
        button_1.config(state=tk.DISABLED)

def mouseover(ev):
    button_1['bg'] = 'green'

def mouseout(ev):
    button_1['bg'] = 'blue' # the button will remain blue if mouseout, not red anymore

window = tk.Tk()
button_1 = tk.Button(window, text="Enabled", bg="red")
button_1.bind("<Enter>", mouseover)
button_1.bind("<Leave>", mouseout)
button_1.pack()
button_2 = tk.Button(window, text="Enable/Disable", command=switch)
button_2.pack()
window.mainloop()


import tkinter as tk
from tkinter import messagebox

def count():
    global counter
    counter += 1

def show():
    messagebox.showinfo("","counter=" + str(counter) + ",state=" + str(switch.get()))

window = tk.Tk()
switch = tk.IntVar() # linked to checkbutton[variable], == 0(unticked) or 1(ticked)
counter = 0 # will be implemented by 1 at each tick/untick of checkbutton
button = tk.Button(window, text="Show", command=show)
button.pack()
checkbutton = tk.Checkbutton(window, text="Tick", variable=switch, command=count)
checkbutton.pack()
window.mainloop()


import tkinter as tk
from tkinter import messagebox

def show():
    messagebox.showinfo("", "radio_1=" + str(radio_1_var.get()) +
                        ",radio_2=" + str(radio_2_var.get()))

def command_1():
    radio_2_var.set(radio_1_var.get())

def command_2():
    radio_1_var.set(radio_2_var.get())

window = tk.Tk()
button = tk.Button(window, text="Show", command=show)
button.pack()
radio_1_var = tk.IntVar()
radio_1_1 = tk.Radiobutton(window, text="pizza", variable=radio_1_var, value=1, command=command_1)
radio_1_1.select()
radio_1_1.pack()
radio_1_2 = tk.Radiobutton(window, text="clams", variable=radio_1_var, value=2, command=command_1)
radio_1_2.pack()
radio_2_var = tk.IntVar()
radio_2_1 = tk.Radiobutton(window, text="FR", variable=radio_2_var, value=2, command=command_2)
radio_2_1.pack()
radio_2_2 = tk.Radiobutton(window, text="IT", variable=radio_2_var, value=1, command=command_2)
radio_2_2.select()
radio_2_2.pack()
window.mainloop()


# Entry()

# presents a line of text
# able to edit the text according to the user’s actions
# using an Entry is necessary when we ask the user for any textual information: name, password, email
# the widget implements all standard edit operations like inserting, removing, scrolling, selecting, copying and pasting

'''
ENTRY PROPERTY    	PROPERTY MEANING
command	            although Entry is obviously a clickable widget, it doesn’t allow us to bind a callback through the command property
                    We can observe and control all occurring changes instead by setting the tracer function for the observable variable which cooperates with Entry 

show	            a string assigned to this property will be displayed instead of the actual characters entered into the input field
                    EX: if we set show='*', this will enable the widget to safely edit the user’s password

state	            same as for Button
textvariable	    observable StringVar reflecting the current state of the input field
width	            input field’s width (in characters)


ENTRY METHOD     	       METHOD ROLE
get()	                   returns the current input field’s contents as a string
set(s)	                   sets the whole input field’s contents with the s string
delete(first, last=None)   deletes a part of the input field’s contents; first and last can be integers with values indexing the string
                           if the last argument is omitted, a single character is deleted
                           if last is specified as END, it points to the place after the last field’s character

insert(index, s)	       inserts the s string at the field position pointed to by index
'''


import tkinter as tk

def digits_only(*args):
    global last_string        
    string = text.get()
    if string == '' or string.isalnum() and len(string) <= 5 : # string vide ou alphanum ET 5 characteres MAX
        last_string = string
    else:
        text.set(last_string)

last_string = ''
window = tk.Tk()
text = tk.StringVar()                        # to hold the entry's value
entry = tk.Entry(window, textvariable=text)  # Creates the entry widget, bound to the StringVar
text.set(last_string)                        # we start with an empty string
text.trace_add('write', digits_only)         # we'll add any string through the digits_only function
entry.pack()
entry.focus_set()                            # focus to the entry so you can start typing immediately
window.mainloop()



## NON-CLICKABLE widgets

# designed to present textual information and don’t have a command property, although we can use bind() to simulate similar behavior

# Label()
'''
Label()
label = Label(master, option, ...)

LABEL PROPERTY       PROPERTY MEANING
text	             a string which will be shown within the Label; (\n) are interpreted in the usual way
textvariable	     same as for text, but makes use of an observable StringVar variable, so if we change the variable’s alteration, it will be immediately visible on the screen
'''

import tkinter as tk

def to_string(x):
    return "Current counter\nvalue is:\n" + str(x)

def plus():
    global counter
    counter += 1
    text.set(to_string(counter))

counter = 0
window = tk.Tk()
button = tk.Button(window, text="Go on!", command=plus)
button.pack()
text = tk.StringVar()
label = tk.Label(window, textvariable=text, height=4)
text.set(to_string(counter))
label.pack()
window.mainloop()


# Message()

'''
message = Message(master, option, ...)
'''

import tkinter as tk

def do_it_again():
    text.set(text.get() + "and again...")

window = tk.Tk()
button = tk.Button(window, text="Go ahead!", command=do_it_again)
button.pack()
text = tk.StringVar()
message = tk.Message(window, textvariable=text, width=400)
text.set("You did it again... ")
message.pack()
window.mainloop()


# Frame()

# a container designed to store other widgets
# can be used to separate a rectangular part of the window and to treat it as a kind of local window
# Such a window works as a master widget for all the widgets embedded within it

# Frame() has its own coordinate system, so when we place a widget inside, we measure its location relative to the Frame’s upper-left corner, not the window’s one
# Also, if we move the Frame to a new position, all its inner widgets will go with it

# Frame() can grasp virtually any widget – including another Frame

'''
FRAME PROPERTY   	PROPERTY MEANING
takefocus	        normally, the Frame doesn’t take the focus but if we really want it to behave in this way, we can set the property to 1
'''

import tkinter as tk

window = tk.Tk()

frame_1 = tk.Frame(window, width=200, height=100, bg='white')
frame_2 = tk.Frame(window, width=200, height=100, bg='yellow')

button_1_1 = tk.Button(frame_1, text="Button #1 inside Frame #1")
button_1_2 = tk.Button(frame_1, text="Button #2 inside Frame #1")
button_2_1 = tk.Button(frame_2, text="Button #1 inside Frame #2")
button_2_2 = tk.Button(frame_2, text="Button #2 inside Frame #2")

button_1_1.place(x=10, y=10)
button_1_2.place(x=10, y=50)
button_2_1.grid(column=0, row=0)
button_2_2.grid(column=1, row=1)

frame_1.pack()
frame_2.pack()

window.mainloop()


# LabelFrame()

# Frame enriched with a visible border and a title, also visible
# The title may be located at one of 12 possible places on the border line

'''
lfrm = LabelFrame(master, option, ...)

LABELFRAME PROPERTY   	PROPERTY MEANING
takefocus	            same as for the Frame
text	                LabelFrame’s title
labelanchor	            title’s location, defined as a string containing a quasi-compass coordinate (NW N NE etc)
'''

import tkinter as tk

window = tk.Tk()
label_frame_1 = tk.LabelFrame(window, text="Frame #1",
                              width=200, height=100, bg='white')
label_frame_2 = tk.LabelFrame(window, text="Frame #2",
                              labelanchor='se', width=200, height=100, bg='yellow')

button_1_1 = tk.Button(label_frame_1, text="Button #1 inside Frame #1")
button_1_2 = tk.Button(label_frame_1, text="Button #2 inside Frame #1")
button_2_1 = tk.Button(label_frame_2, text="Button #1 inside Frame #2")
button_2_2 = tk.Button(label_frame_2, text="Button #2 inside Frame #2")

button_1_1.place(x=10, y=10)
button_1_2.place(x=10, y=50)
button_2_1.grid(column=0, row=0)
button_2_2.grid(column=1, row=1)

label_frame_1.pack()
label_frame_2.pack()
window.mainloop()



## MENUs


import tkinter as tk
from tkinter import messagebox

def about_app():
    messagebox.showinfo("App", "The application\nthat does nothing")

def are_you_sure(event=None):
    if messagebox.askyesno("", "Are you sure you want to quit the App?"):
        window.destroy()

def open_file():
    messagebox.showinfo("Open doc", "We'll open a file here...")
          
window = tk.Tk()

main_menu = tk.Menu(window)
window.config(menu=main_menu) # creates the main Menu bar
sub_menu_file = tk.Menu(main_menu)
# we don't want the tear-off here  = ----- below File
sub_menu_file = tk.Menu(main_menu, tearoff=0)
# setting the hotkey to "Alt-F"
main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
# a new submenu item is here!
sub_menu_file.add_command(label="Open...", underline=0, command=open_file)
# adding a submenu
sub_sub_menu_file = tk.Menu(sub_menu_file, tearoff=0)
sub_menu_file.add_cascade(label="Open recent file...", underline=5, menu=sub_sub_menu_file)
# adding (simulate) the presence of eight recently opened files
for i in range(8):
    number = str(i + 1)
    sub_sub_menu_file.add_command(label=number + ". file.txt", underline=0)
# separator is here == line between submenu titles
sub_menu_file.add_separator()
# add the QUIT action to the submenu
sub_menu_file.add_command(label="Quit", accelerator="Ctrl-Q", underline=0, command=are_you_sure)
sub_menu_help = tk.Menu(main_menu)
# setting the hotkey to "Alt-B"
main_menu.add_command(label="About...", command=about_app, underline=1)
# shortcut (accelerator) to close the window with hotkey from any menu
window.bind_all("<Control-q>", are_you_sure)
window.mainloop()


# .entryconfigure()

import tkinter as tk

def on_off():
    global accessible
    if accessible == tk.DISABLED:
        accessible = tk.ACTIVE
    else:
        accessible = tk.DISABLED
    sub_menu.entryconfigure(1, state=accessible) # sub_menu index 1 == the 2nd menu option ==> sub_menu.add_command(label="Switch", state=tk.DISABLED)

accessible = tk.DISABLED
window = tk.Tk()
menu = tk.Menu(window)
window.config(menu=menu)
sub_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Menu", menu=sub_menu)
sub_menu.add_command(label="On/Off", command=on_off)
sub_menu.add_command(label="Switch", state=tk.DISABLED)
window.mainloop()


'''
PROPERTY         	PROPERTY ROLE
postcommand	        callback invoked every time a menu’s item is activated
tearoff	            set to zero removes the tear-off decoration from the top of the cascade
state	            when set to DISABLED, the menu item is grayed and inaccessible; setting it to ACTIVE restores its normal functionality
accelerator	        a string describing a hot-key bound to the menu’s item

METHOD           	             METHOD ROLE
add_cascade(prop=val, ...)	     adds a cascade to the menu’s item
add_command(prop=val, ...)	     assigns an action to the menu’s item
add_separator()	                 adds an separator line to the menu
entryconfigure(i, prop=val,...)	 modifies the i-th menu item’s property named prop
'''



### MAIN WINDOW


## title()

# to change the main window title

import tkinter as tk

def click(*args):
    global counter
    if counter > 0:
        counter -= 1
    window.title(str(counter)) # re-apply the title with the new counter value

counter = 10
window = tk.Tk()
window.title(str(counter)) # counter value will start being the counter value ("10")
window.bind("<Button-1>", click) # ac click will launch the function "click"
window.mainloop()


## icon

import tkinter as tk
from tkinter import PhotoImage

window = tk.Tk()
window.title('Icon?')
window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='logo.png'))
'''
Use tk.call() to invoke a Tk command
'wm', 'iconphoto' : define icon  
window._w : internal window identifier
PhotoImage(file='logo.png') : loads logo.png as the icon image
'''
window.bind("<Button-1>", lambda e: window.destroy()) # a left click will close the window
window.mainloop()


## geometry()

# not any any default value, the window size is defined by the widgets it contains
# we can set the window size explicitly by using the geometry() method, width and height

import tkinter as tk

def click(*args):
# the window grow till 500x500 then shrink to 100x100 and repeat
    global size, grows
    if grows:
        size += 50
        if size >= 500:
            grows = False
    else:
        size -= 50
        if size <= 100:
            grows = True
    window.geometry(str(size) + "x" + str(size))

size = 100
grows = True
window = tk.Tk()
window.geometry("100x100")
window.bind("<Button-1>", click) # left click launches "click" function
window.mainloop()


# minsize()/maxsize()
import tkinter as tk

window = tk.Tk()
window.minsize(width=250, height=200) # Set minimum size of the window
window.maxsize(width=450, height=400) # Set maximum size of the window
window.geometry("300x300") # Set initial size of the window
window.mainloop()


# resizable()

import tkinter as tk

window = tk.Tk()
window.resizable(width=False, height=False) # disable window resizing width and height
window.geometry("400x200")
window.mainloop()


# protocol()

import tkinter as tk
from tkinter import messagebox

def really():
    if messagebox.askyesno("?", "Are you sure you want to abort ?"):
        window.destroy()

window = tk.Tk()
window.protocol("WM_DELETE_WINDOW", really) # intercepts the window close event and calls the really() function instead of immediately closing
window.mainloop()



## MESSAGEBOX dialogs

# display a modal dialog window and wait for a user response

'''
dialog’s behavior is determined by three parameters:
    title   ==> a string displayed in the dialog’s title bar
    message ==> a string displayed inside the dialog
    options ==> a set of options shaping the dialog in a non-default way
        default => sets the default (pre-focused) answer; usually, it’s focused on the button located first from the left; this can be changed by setting the keyword argument with identifiers like CANCEL, IGNORE, OK, NO, RETRY, and YES;
        icon    => sets the non-default icon for the dialog: possible values are: ERROR, INFO, QUESTION, and WARNING
'''

# askyesno( )

import tkinter as tk
from tkinter import messagebox

def question():
    answer = messagebox.askyesno("?", "To be or not to be?") # Asks a Yes/No question, window title is "?" and question is "To be or not to be?"
    print(answer) # will print True for Yes and False for No

window = tk.Tk()
button = tk.Button(window, text="Ask the question!", command=question)
button.pack()
window.mainloop()
# True  ==> if Yes clicked
# False ==> if No clicked   


# askokcancel(  )

import tkinter as tk
from tkinter import messagebox

def question():
    answer = messagebox.askokcancel("?", "I'm going to format your hard drive")
    print(answer) # will print True for Ok and False for Cancel

window = tk.Tk()
button = tk.Button(window, text="What are your plans?", command=question)
button.pack()
window.mainloop()
# True  ==> if Ok clicked
# False ==> if Cancel clicked 


# askretrycancel()

import tkinter as tk
from tkinter import messagebox

def question():
    answer = messagebox.askretrycancel("?", "I'm going to format your hard drive")
    print(answer) # print True if Retry is clicked, False if Cancel is clicked

window = tk.Tk()
button = tk.Button(window, text="What are your plans?", command=question)
button.pack()
window.mainloop()
# True
# False


# askquestion()

import tkinter as tk
from tkinter import messagebox

def question():
    answer = messagebox.askquestion("?", "I'm going to format your hard drive")
    print(answer) # Prints 'yes' or 'no' based on user response

window = tk.Tk()
button = tk.Button(window, text="What are your plans?", command=question)
button.pack()
window.mainloop()
# yes
# no


# showerror()

import tkinter as tk
from tkinter import messagebox

def question():
    answer = messagebox.showerror("!", "Your code does nothing!")
    print(answer) # print 'ok' since showerror only has an 'OK' button, even if we close the window

window = tk.Tk()
button = tk.Button(window, text="Alarming message", command=question)
button.pack()
window.mainloop()
# ok
# ok


# showwarning()

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
