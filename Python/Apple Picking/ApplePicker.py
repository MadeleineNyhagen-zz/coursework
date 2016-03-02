import time
    
def start():
    print "Hello!"
    name = raw_input("What's your name? ")
    print "Welcome, {}!".format(name)
    print "The objective of this game is to collect apples."
    print "After collecting the apples you sell them."
    choice = raw_input("Do you want to play? (y/n) ")
    if choice == "y":
        print "Let's get started!"
        begin(0,0)
    if choice == "n":
        print "Okay, bye!"

def begin(apples, gold):

    if gold > 49:
        print "You've won the game!"
        play = raw_input("Do you want to play again? (y/n) ")
        if play == "y":
            print "Ok!"
            begin(0,0)
        if play == "n":
            print "Goodbye."
        
            
    pick = raw_input("Do you want to pick an apple? (y/n) ")
    if pick == "y":
        time.sleep(1)
        print "You pick an apple."
        apples = apples + 1
        if apples == 1:
            print "You have 1 apple."
            begin(apples, gold)
        if apples != 1:
            print "You have {} apples!".format(apples)
            begin(apples, gold)
    if pick == "n":
        sell = raw_input("Do you want to sell your apples? ")
        if sell == "y":
            if apples == 0:
                print "You have no apples to sell!"
            if apples == 1:
                print "You currently have {} apple.".format(apples)
                print "You have sold your apple."
                gold = gold + (apples*10)
                apples = 0
                print "you now have {} gold!".format(gold)
                begin(apples, gold)
            if apples > 1:
                print "You currently have {} apples.".format(apples)
                print "You have sold your apples."
                gold = gold + (apples*10)
                apples = 0
                print "You now have {} gold!".format(gold)
                begin(apples, gold)
        if sell == "n":
            leave = raw_input("Would you like to quit the game? (y/n) ")
            if leave == "y":
                print("Goodbye.")
            if leave == "n":
                begin(apples, gold)
                

start()




    
