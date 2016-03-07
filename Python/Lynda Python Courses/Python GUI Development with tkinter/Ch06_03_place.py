#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

root.geometry('640x480+200+200')

ttk.Label(root, text = 'Yellow', background = 'yellow').place( x = 100, y = 50, width = 100, height = 50)
# absolute coordinates (x, y) and absolute sizing (width, height)
ttk.Label(root, text = 'Blue',
          background = 'blue').place(relx = 0.5, rely = 0.5, anchor = 'center', relwidth = 0.5, relheight = 0.5)
# ^ relx and rely place the widget in relative locations depending on the size of the window, while anchor
# affects which part of the widget is anchored to the given coordinates (by default it's the top left corner)
# relwidth and relheight allow you to set a widgets size relative to the window
ttk.Label(root, text = 'Green', background = 'green').place(relx = 0.5, x = 100, rely = 0.5, y = 50)
# ^ can use absolute and relative coordinates with each other to place a widget
ttk.Label(root, text = 'Orange', background = 'orange').place(relx = 1.0, x = -5, y = 5, anchor = 'ne')
# ^ negative coordinates move the widget to the left, which can be useful when using relative coordinates and
# absolutes together.


# other grid methods:
# place_slaves()
# place_configure()
# place_info()
# place_forget()


root.mainloop()
