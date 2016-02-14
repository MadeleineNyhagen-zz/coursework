dictionary_name = {'item_1':1,'item_2':2, 'item_3':3 }
print dictionary_name['item_1']

epic_programmer_dict = {'Ada Lovelace' : 'lordbyronsdaughter@gmail.com',
                        'Margaret Hamilton' : 'asynchronous.apollo@mit.edu',
                        'Grace Hopper' : 'Commodore.debug@vassar.edu',
                        'Jean Jennings Bartik' : 'bartik@eniac.mil',
                        'Adele Goldstine' : 'goldstine@eniac.mil'}

print epic_programmer_dict
print 'Email for Ada: ' + epic_programmer_dict['Ada Lovelace']

# adds a different email address
epic_programmer_dict['Ada Lovelace'] = 'analyticalengine@gmail.com'

print 'New email for Ada: ' + epic_programmer_dict['Ada Lovelace']

# add Betty Holberton and her email to the dictionary
epic_programmer_dict['Betty Holberton'] = 'holberton@eniac.mil'
print "Email for Betty Holberton: " + epic_programmer_dict['Betty Holberton']

# add myself to the dictionary
epic_programmer_dict['Madeleine Nyhagen'] = 'nyhagen@gmail.com'
print 'My email: ' + epic_programmer_dict['Madeleine Nyhagen']

# add some guy to the dictionary
epic_programmer_dict['Guido van Rossum'] = 'gvr@gmail.com'
print 'Email for Guido: ' + epic_programmer_dict['Guido van Rossum']
print epic_programmer_dict

# delete guido from the dictionary
del epic_programmer_dict['Guido van Rossum']

del epic_programmer_dict['Madeleine Nyhagen']

for programmer in epic_programmer_dict:
    print programmer
