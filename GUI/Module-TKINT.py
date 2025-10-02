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



