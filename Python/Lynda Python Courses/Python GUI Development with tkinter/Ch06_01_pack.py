#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

### Using fill and expand properties:
##ttk.Label(root, text = 'Hello, Tkinter!',
##          background = 'yellow').pack(fill = BOTH, expand = True) # fill can be X for horizontal, Y for vertical, or BOTH for both
##          # expand tells the pack manager to expand it to fill the entire space
##ttk.Label(root, text = 'Hello, Tkinter!',
##          background = 'blue').pack(fill = BOTH)
##ttk.Label(root, text = 'Hello, Tkinter!',
##          background = 'green').pack(fill = BOTH, expand = True)

# Using side, anchor, pad, and ipad properties: widgets should usually be packed against the same side when using the pack manager
# (If packing against multiple sides, the grid manager is more appropriate)
# anchor uses cardinal directions to anchor a widget
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'yellow').pack(side = LEFT, anchor = 'nw')
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'blue').pack(side = LEFT, padx = 10, pady = 10) # padx & pady add external padding
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'green').pack(side = LEFT, ipadx = 10, ipady = 10) # ipadx & ipady add internal padding

# to create a label that is saved in a variable, it's necessary to create and pack it separately, like this:
label = ttk.Label(root, text = 'Hello, Tkinter!', background = 'red')
label.pack()
print(label) # testing that the label variable actually refers to something

label.pack_forget() # to forget the label, but not destroy it

for widget in root.pack_slaves(): # a loop to apply a style to all widgets that are children of the parent window
    widget.pack_configure(fill = BOTH, expand = True)
    print(widget.pack_info())

root.mainloop()
