#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

label1 = ttk.Label(root, text = 'Label 1')
label2 = ttk.Label(root, text = 'Label 2')
label1.pack()
label2.pack()

label1.bind('<ButtonPress>', lambda e: print('<ButtonPress> Label')) # binding a general mouse event to this label
label1.bind('<1>', lambda e: print('<1> Label')) # binding a left click mouse event to this label

root.bind('<1>', lambda e: print('<1> Root')) # binding this event to the root

label1.unbind('<1>')
label1.unbind('<ButtonPress>')

root.bind_all('<Escape>', lambda e: print("Escape!")) # binds this function to all top-level windows in the program

root.mainloop()
