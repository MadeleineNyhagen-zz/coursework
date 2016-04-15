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

        # making a frame header
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        # making the frame body
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        # adding content to the header
        self.picture = PhotoImage(file = 'maru3.gif')
        ttk.Label(self.frame_header, image = self.picture).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.frame_header, text = 'Sale Page Editor', style = 'Header.TLabel').grid(row = 0, column = 1)
        ttk.Label(self.frame_header, wraplength = 300, text = ("Type out the text you'd like to see in the body of our summer sale announcement page. "
                                            "When you're done, hit submit to create it!")).grid(row = 1, column = 1)


        # adding content to the body

        # adding the name entry box
        self.name_entry = Text(self.frame_content, width = 30, height = 1, font = ('Helvetica',10))
        self.name_entry.grid(row = 0, column = 0, padx = 1, pady = 5, stick = 'n')

        # adding the body text entry box        
        self.body_text = Text(self.frame_content, width = 50, height = 10, font = ('Helvetica',10))
        self.body_text.grid(row = 0, column = 2, columnspan = 2, padx = 1, pady = 5)

        ttk.Button(self.frame_content, text = 'Submit', command = self.savebodytext).grid(row = 1, column = 0, padx = 5, stick = 'e')
        ttk.Button(self.frame_content, text = 'Cancel', command = self.exitgui).grid(row = 1, column = 1, padx = 5, stick = 'w')



    def savebodytext(self):
        textinput = self.body_text.get(1.0, 'end')
        f = open("summersale.html","w")

        htmltext = '''<html>
    <body>
    {}
    </body>
</html>
        '''.format(textinput)
        f.write(htmltext)
        f.close()

        print(htmltext)

    def exitgui(self):
        root.destroy()


##def main():
##    root = Tk()
##    htmleditor = HTMLEditor(root)
##    root.mainloop()

root = Tk()
htmleditor = HTMLEditor(root)
root.mainloop()

# if __name__ == "__main__": main()
