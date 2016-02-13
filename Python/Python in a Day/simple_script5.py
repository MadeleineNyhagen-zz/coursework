# create the list of epic programmers
epic_programmer_list = ["Ada Lovelace",
                        "Margaret Hamilton",
                        "Grace Hopper",
                        "Jean Jennings Bartik",
                        "Adele Goldstine"]

# print to console
print "An epic programmer: " + epic_programmer_list[0]

print "An epic programmer: " + epic_programmer_list[0]
print "An epic programmer: " + epic_programmer_list[1]
print "An epic programmer: " + epic_programmer_list[2]
print "An epic programmer: " + epic_programmer_list[3]
print "An epic programmer: " + epic_programmer_list[4]

# add myself to the end of the list
epic_programmer_list.append("Me")

# add this line to show myself in the console
print "An epic programmer: " + epic_programmer_list[5]

# looping through each item in epic_programmer_list
for programmer in epic_programmer_list:
    # print the programmers' name to console
    print "An epic programmer: " + programmer

# create list of numbers
number_list = [1,2,3,4,5]
empty_number_list = []

# loop each number in number_list
for x in number_list:
    # print each number to the power of 2
    # print x**2

    # append each number to the power of 2 to the empty_number_list
    empty_number_list.append(x**2)

print empty_number_list
