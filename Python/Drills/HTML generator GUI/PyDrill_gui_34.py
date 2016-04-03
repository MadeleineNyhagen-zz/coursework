#!/usr/bin/python3

# adapting my html generator script to be editable via a gui

from tkinter import *

f = open("summersale.html","w")

htmltext = '''<html>
<body>
Stay tuned for our amazing summer sale!
</body>
</html>
'''

f.write(htmltext)
f.close()
