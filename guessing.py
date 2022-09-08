import math
import random

def main():
    print("Welcome to the guessing game!")
    print("In this game, we will be hiding a prize under one of the numbers.")
    print("Try to guess where the prize is.")
    while True:
        numcups = setcups()
        numballs = setballs(numcups)
        cups = list(range(numcups))
        balls = set()
        while (len(balls) < numballs):
            balls.add(random.randint(0, numcups - 1))
        print(makeoutput(cups))
        print("Take your pick!")
        while True:
            try:
                guess = int(input())
                break
            except:
                print("Try again")
        guess -= 1
        if guess in balls:
            print("You got it! I would give you a prize but look at the economy, I'd have to mortgage my house!")
        else:
            print("Aw, you didn't get it. I'm sure you're due a win next time though, so you should try again!")
        q = input("Try again? Y/N ")
        if (q.strip().upper() != "Y"):
            break
    print("Thanks for playing!")


def makeoutput(cups):
    output = ""
    for x in cups:
        output += str((x+1)) + " "
    return output[:len(output) - 1]

def setcups():
    cups = 0
    while cups < 3:
        try:
            cups = int(input("How many cups would you like to choose from? "))
            if cups <= 0:
                print("I'd love to see that, but I can't do it myself")
            elif cups <= 2:
                print("Let's make it more interesting shall we?")
            elif cups == 3:
                print("Standard. A bit boring, but I like it")
        except:
            print("Can't do that buddy, sorry")
    return cups

def setballs(cups):
    balls = 0
    if (cups <= 5):
        return 1
    print("Alright. One more step before we begin.")
    while balls <= 0 or balls > math.floor(cups / 3):
        try:
            balls = int(input("How many balls would you like to hide? "))
            if balls <= 0:
                print("Really setting yourself up for failure huh...")
            if balls == cups:
                print("A for effort. You must think I haven't been doing this long.")
            elif balls > cups:
                print("Where am I gonna put all this?!")
            elif balls > math.floor(cups / 3):
                print("Hey, I don't want you to win that badly. I gotta make a living somehow.")
        except:
            print("Can't do that buddy, sorry")
    return balls