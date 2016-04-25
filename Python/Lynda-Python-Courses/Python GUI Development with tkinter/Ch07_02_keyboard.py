#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com


from tkinter import *
from tkinter import ttk        
    
root = Tk()


##def key_press(event):
##    print('type: {}'.format(event.type))
##    print('widget: {}'.format(event.widget))
##    print('char: {}'.format(event.char))
##    print('keysym: {}'.format(event.keysym))
##    print('keycode: {}'.format(event.keycode))
##
##root.bind('<KeyPress>',key_press) # first parameter is a string containing specially formatted description
### of the event to listen for, second parameter is the name of the callback function or method to execute


def shortcut(action):
    print(action)

root.bind('<Control-c>', lambda e: shortcut('Copy')) # e parameter added to lambda to catch the event being passed into it
root.bind('<Control-v>', lambda e: shortcut('Paste'))


# Tk Event types:
# ButtonPress
# ButtonRelease
# Enter
# Leave
# Motion
# KeyPress
# KeyRelease
# FocusIn
# FocusOut
# for more documentation: http://www.tkdocs.com/tutorial/canvas.html#bindings

# some keyboard event examples:
# Event Format: <Key>, <KeyPress>  -----  Event Description: User pressed any key.
# Event Format: <KeyPress-Delete>  -----  Event Description: User pressed Delete key.
# Event Format: <KeyRelease-Right>  -----  Event Description: User released Right Arrow key.

root.mainloop()
