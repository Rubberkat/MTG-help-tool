__author__ = 'Roy'
import random
import csv

csvfile = 'life.csv'
with open('life.csv', 'r') as f:
    reader = csv.reader(f)
    lifetotalfromfile = list(reader)
    lifetotal = int(lifetotalfromfile[0][0])

#basic menu input where you can choose between 1-3
def menu():
    print ('1. Life counter\n2. Dice\n3. Flip coin\n')
    try:
        menuinput = int(input('\nWhat do you want to do?\n'))
        if menuinput == 1:
            lifecounter()
        elif menuinput == 2:
            dice()
        elif menuinput == 3:
            flipcoin()
        else:
            print ('\nEnter a number between 1 - 4\n')
            return menu()
    except ValueError:
        print ('\nEnter a number\n')
        return menu()

#rolls a dice between 1 to 20 (magic uses dice that go to 20)
def dice():

        print ('Rolling the dice..')
        rng = random.randrange(1, 20)
        print (rng)
        again()

#asks to roll the dice again y/n
def again():

    try:
        rollagain = input('Do you want to roll again? y/n')
        if rollagain == 'y':
            return dice()
        if rollagain == 'n':
            return menu()
        else:
            print ('Error')
            return again()
    except:
        print ('Error')
        return again()


def lifecounter():

    print ('\n1. Gain life\n2. Lose life\n3. Life total\n4. Reset life total\n5. Go back to menu\n')
    lifeinput = int(input('\nWhat do you want to do?\n'))
    try:
        if lifeinput == 1:
            lifegain()
        if lifeinput == 2:
            lifelost()
        if lifeinput == 3:
            print ('\nYour life total is', lifetotal)
            return lifecounter()
        if lifeinput == 4:
            resetlifetotal()
        if lifeinput == 5:
            menu()
    except:
        print ('\nError write a number between 1-5\n')
        return lifecounter()

def lifegain():
    global lifetotal
    f = open(csvfile, 'w', newline='')
    writer = csv.writer(f)
    gainlife = int(input('\nType in the number you gained in life:\n'))
    lifetotal = (lifetotal + gainlife)
    writer.writerow([lifetotal])
    f.flush()
    print ('\nYour total life is', lifetotal)
    return lifecounter()

def lifelost():
    global lifetotal
    f = open(csvfile, 'w', newline='')
    writer = csv.writer(f)
    gainlife = int(input('\nType in the number you lost in life:\n'))
    lifetotal = (lifetotal - gainlife)
    writer.writerow([lifetotal])
    f.flush()
    f.close()
    print ('\nYour total life is', lifetotal)
    return lifecounter()

def resetlifetotal():
    global lifetotal
    f = open(csvfile, 'w', newline='')
    writer = csv.writer(f)
    lifetotal = 20
    writer.writerow([lifetotal])
    f.flush()
    f.close()
    print ('\nLife has been reset to', lifetotal)
    menu()

def flipcoin():

    coin = ['Heads', 'Tails']
    coinflip = random.choice(coin)
    print (coinflip)
    flipagain()


def flipagain():

    try:
        fagain = input('\nDo you wish to flip again? y\n')
        if fagain == 'y':
            return flipcoin()
        if fagain == 'n':
            return menu()
        else:
            print ('\nType in \'y\' for yes and \'n\' for no\n')
            return flipagain()
    except TypeError:
        print('\nError, invalid input\n')
        return flipagain()

menu()
