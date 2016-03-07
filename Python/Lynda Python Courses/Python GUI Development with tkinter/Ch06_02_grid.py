#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()


### a very simple grid layout:
##ttk.Label(root, text = "Yellow", background = "yellow").grid(row = 1, column = 1)
##ttk.Label(root, text = "Blue", background = "blue").grid(row = 1, column = 0)
##ttk.Label(root, text = "Green", background = "green").grid(row = 0, column = 0)
##ttk.Label(root, text = "Orange", background = "orange").grid(row = 0, column = 1)


### a slightly more complex grid layout:
##ttk.Label(root, text = "Yellow", background = "yellow").grid(row = 0, column = 2, rowspan = 2)
##ttk.Label(root, text = "Blue", background = "blue").grid(row = 1, column = 0, columnspan = 2)
##ttk.Label(root, text = "Green", background = "green").grid(row = 0, column = 0)
##ttk.Label(root, text = "Orange", background = "orange").grid(row = 0, column = 1)


### sticking a widget in a particular part of the grid section allocated to it, using the sticky property
### nsew stands for the cardinal directions, using all of them forces the label to expand to fill its cell
### but using just one sticks the label to that side of the cell
##ttk.Label(root, text = "Yellow", background = "yellow").grid(row = 0, column = 2, rowspan = 2, stick = 'nsew')
##ttk.Label(root, text = "Blue", background = "blue").grid(row = 1, column = 0, columnspan = 2, stick = 'e')
##ttk.Label(root, text = "Green", background = "green").grid(row = 0, column = 0)
##ttk.Label(root, text = "Orange", background = "orange").grid(row = 0, column = 1)


### using the weight property to increase the size of the grid cells as the window expands
##root.rowconfigure(0, weight = 1) # to configure weight of row 1 (first parameter is the index of the row)
##root.rowconfigure(1, weight = 3) # to configure weight of row 2
### row 1 will expand 1 pixel for every 3 that row 2 expands as the size of the window increases
##
##root.columnconfigure(2, weight = 1) # to configure weight of column
##
##ttk.Label(root, text = "Yellow", background = "yellow").grid(row = 0, column = 2, rowspan = 2, stick = 'nsew')
##ttk.Label(root, text = "Blue", background = "blue").grid(row = 1, column = 0, columnspan = 2, stick = 'nsew')
##ttk.Label(root, text = "Green", background = "green").grid(row = 0, column = 0, stick = 'nsew')
##ttk.Label(root, text = "Orange", background = "orange").grid(row = 0, column = 1, stick = 'nsew')


# using padding in grid
root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 3)
root.columnconfigure(2, weight = 1)

ttk.Label(root, text = "Yellow", background = "yellow").grid(row = 0, column = 2, rowspan = 2, stick = 'nsew')
ttk.Label(root, text = "Blue", background = "blue").grid(row = 1, column = 0, columnspan = 2, stick = 'nsew')
ttk.Label(root, text = "Green", background = "green").grid(row = 0, column = 0, stick = 'nsew', padx = 10, pady = 10)
ttk.Label(root, text = "Orange", background = "orange").grid(row = 0, column = 1, stick = 'nsew', ipadx = 25, ipady = 25)


# some other available grid methods are:
# grid_slaves()
# grid_configure()
# grid_info()
# grid_forget()


root.mainloop()
