from datetime import datetime

now = datetime.now()

currentHour = now.hour
currentMin = now.minute

PortlandTime = str(currentHour) + ":" + str(currentMin)
PortlandMath = currentHour

NewYorkTime = str(currentHour + 3) + ":" + str(currentMin)
NewYorkMath = currentHour + 3

LondonTime = str(currentHour + 8) + ":" + str(currentMin)
LondonMath = currentHour + 8


if PortlandMath >= 9 and PortlandMath < 21:
   print "It is " + PortlandTime + " and the Portland branch is open."
else:
    print "It is " + PortlandTime + " and the Portland branch is closed."

if NewYorkMath >= 9 and NewYorkMath < 21:
   print "It is " + NewYorkTime + " and the New York branch is open."
else:
    print "It is " + NewYorkTime + " and the New York branch is closed."

if LondonMath >= 9 and LondonMath < 21:
   print "It is " + LondonTime + " and the London branch is open."
else:
    print "It is " + LondonTime + " and the London branch is closed."


