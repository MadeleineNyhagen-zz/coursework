#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

entry = ttk.Entry(root)
entry.pack()

entry.bind('<<Copy>>', lambda e: print('Copy'))
entry.bind('<<Paste>>', lambda e: print('Paste'))

entry.event_add('<<OddNumber>>', '1', '3', '5', '7', '9') # creating a virtual event
entry.bind('<<OddNumber>>', lambda e: print('Odd Number!'))

print(entry.event_info('<<OddNumber>>')) # to print the information about the event

entry.event_generate('<<OddNumber>>') # to trigger the OddNumber event
entry.event_generate('<<Paste>>') # to trigger the paste event

entry.event_delete('<<OddNumber>>') # deletes the OddNumber event

root.mainloop()
