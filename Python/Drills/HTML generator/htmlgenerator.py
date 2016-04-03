# writing a script to generate a very simple html page

f = open("summersale.html","w")

htmltext = '''<html>
<body>
Stay tuned for our amazing summer sale!
</body>
</html>
'''

f.write(htmltext)
f.close()
