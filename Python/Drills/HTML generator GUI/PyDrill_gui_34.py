#!/usr/bin/python3

# adapting my html generator script to be editable via a gui

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class HTMLEditor:

    def __init__(self, master):

        master.title('Edit the sale page! What should it say?')



        self.f = open("summersale.html","w")

        self.htmltext = '''<html>
        <body>
        Stay tuned for our amazing summer sale!
        </body>
        </html>
        '''

    def savebodytext(self):
        f.write(self.htmltext)
        f.close()


def main():
    root = Tk()
    htmleditor = HTMLEditor(root)
    root.mainloop()

if __name__ == "__main__": main()
