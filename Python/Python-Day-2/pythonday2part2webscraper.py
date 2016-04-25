import urllib2
from bs4 import BeautifulSoup

# open webpage
webpage = urllib2.urlopen ("http://inadaybooks.com/justiceleague")

# convert to BeautifulSoup
soup = BeautifulSoup(webpage, "html.parser")
# print soup.title
# print soup.body

# get the contents container div
divContainer = soup.find("div", {"id":"container"})

# get the div class "block"
divBlock = divContainer.findAll("div", {"class":"block"})

# get the div class "separator"
divSep = divBlock[3].findAll("div",{"class":"separator"})

# extract member names
members = divSep[3].findAll("a")

# extraction function

def extractMData(webpage):
    soup = BeautifulSoup(webpage, "html.parser")
    print soup.title.get_text()

    # find all the divs with class block
    divBlock = soup.findAll("div", {"class":"block"})

    # get 'info_left' and 'info_right'
    info = divBlock[3]
    # extract info_left and info_right divs
    getLeft = info.findAll("div", {"class":"info_left"})
    getRight = info.findAll("div", {"class":"info_right"})
    for i in range(0,len(getLeft)):
        textLeft = getLeft[i].get_text()
        textRight = getRight[i].get_text()
        print textLeft + ": " + textRight
    print ""

# loop through members

##for member in members:
##    # Strip <a> tags
##    print member.get_text()
##
##for member in members:
##    print member.get("title")
##    print member.get("href")

for member in members:
    # strip <a> tags
    href = member.get("href")
    # create url to open
    url = "http://inadaybooks.com/justiceleague/" + href
    # open url
    mPage = urllib2.urlopen(url)
    # extract data from url
    extractMData(mPage)


