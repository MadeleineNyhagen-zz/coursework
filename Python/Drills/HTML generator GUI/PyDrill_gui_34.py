#!/usr/bin/python3

# adapting my html generator script to be editable via a gui

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class HTMLEditor:

    def __init__(self, master):

        master.title('Edit the sale page! What should it say?')
        master.configure(background = '#99ccff')

        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#99ccff')
        self.style.configure('TButton', background = '#99ccff')
        self.style.configure('TLabel', background = '#99ccff', font = ('Helvetica', 11))
        self.style.configure('Header.TLabel', font = ('Helvetica', 18, 'bold'))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        self.picture = PhotoImage(file = 'maru3.gif')
        ttk.Label(self.frame_header, image = self.picture).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.frame_header, text = 'Summer Sale Page!', style = 'Header.TLabel').grid(row = 0, column = 1)
        ttk.Label(self.frame_header, wraplength = 300, text = ("Type out the text you'd like to see in the body of our summer sale announcement page. "
                                            "When you're done, hit submit to create it!")).grid(row = 1, column = 1)



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
