#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

def callback(number):
    print(number)

# The lambda function is necessary here to prevent the callback function from
# being executed immediately when the code is run. If that happens, the command
# is set to the return value of the function, rather than the function itself.
# In this case, because callback has no return value, that means that command is
# set to none and the buttons will not work. Using an anonymous lambda function
# to point to the callback function fixes this:
ttk.Button(root, text = "Click Me 1", command = lambda: callback(1)).pack()
ttk.Button(root, text = "Click Me 2", command = lambda: callback(2)).pack()
ttk.Button(root, text = "Click Me 3", command = lambda: callback(3)).pack()

# More widgets with command callbacks:
# Button
# Checkbutton
# Radiobutton
# Spinbox
# Scale
# Scrollbar


root.mainloop()
