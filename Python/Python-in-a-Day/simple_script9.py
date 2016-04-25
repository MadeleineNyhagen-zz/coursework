epic_programmer_dict = {'ada lovelace' : ['lordbyronsdaughter@gmail.com', 111],
                        'margaret hamilton' : ['asynchronous.apollo@mit.edu', 222],
                        'grace hopper' : ['commodore.debug@vassar.edu', 333],
                        'jean jennings bartik' : ['bartik@eniac.mil', 444],
                        'adele goldstine' : ['goldstine@eniac.mil', 555]}
##print epic_programmer_dict['ada lovelace'][1]
##
### to make a variable that uses a dictionary key/value pair
##programmer = epic_programmer_dict['ada lovelace']
##print programmer[1]
##
### use raw input to have user input a name
##personsName = raw_input('Please enter a name: ').lower()
##
### to take name inputted and compare it to dictionary
##personsInfo = epic_programmer_dict[personsName]


def searchPeople(personsName):
    # looks up the name in the epic dictionary
    try:
        # tries the following lines of texts and if there are no errors then it runs
        personsInfo = epic_programmer_dict[personsName]
        print 'Name: ' + personsName.title()
        print 'Email: ' + personsInfo[0]
        print 'Number: ' + str(personsInfo[1])
    except:
        # if there are errors, then this code gets run
        print 'No information found for that name'

userWantsMore = True
while userWantsMore == True:
    # asks user to input persons name
    personsName = raw_input('Please enter a name: ').lower()
    # run our new function searchPeople with what was typed in searchPeople(personsName)
    searchPeople(personsName)
    # see if user wants to search again
    searchAgain = raw_input('Search again? (y/n) ')
    # look at what they reply and act accordingly
    if searchAgain == 'y':
        # userWantsMore stays as true so loop repeats
        userWantsMore = True
    elif searchAgain == 'n':
        # userWantsMore turns to false to stop loop
        userWantsMore = False
    else:
        # user inputs an invalid response so we quit anyway
        print "I don't understand what you mean, quitting"
        userWantsMore = False
