########## GUI Programming ##########


# ==> Visual programming demands a completely different philosophy, it needs a different paradigm
# ==  event-driven programming



### What is EDP ?

# detecting, registering and classifying all of a user's actions is beyond the programmer's control 
# there is a dedicated component called the "event controller" which takes care of this
# It's automatic and completely opaque
# we don't need to do anything (or almost anything) to make the machinery run, but we are obliged to do something else

# We have to inform the event controller what we want to perform when a particular event 
# This is done by writing specialized functions called "event handlers"
# We write these handlers only for the events we want to serve 
# All other events will activate default behaviors

# We also have to make the event controller aware of events
# In the event-driven paradigm our duties look completely different:
# - the event controller detects the clicks on its own
# - it identifies the target of the click on its own
# - it invokes the desired function on its own
# - all these actions take place behind the scenes



### Events

# There are lots of events, here are some of them:
# - pressing the mouse button
# - releasing the mouse button
# - moving the mouse cursor
# - dragging something under the mouse cursor
# - pressing and releasing a key
# - tapping a screen
# - tracking the passage of time
# - monitoring a widget’s state change
# - etc



### TkInter

# Each operating system delivers its own set of services designed to operate with its native GUI
# Some of them (Linux) may define more than one standard for visual programming

# If we want to build portable GUI applications (= able to work the same under different operating environments) we need an adapter
# Such an adapter is called a widget toolkit, a GUI toolkit, or a UX library
# One of these toolkits, which is very attractive to us, is Tk

# Here are some of its features:
#   - it’s free and open source
#   - been developed since 1991 (== stable and mature)
#   - defines and serves more than thirty different universal widgets which is enough even for quite complex applications
#   - implementation available for many programming languages

# Python module is "TkInter" == Tk Interface
