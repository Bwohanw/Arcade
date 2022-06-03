import random
number = 0
turns = 1

def main():
    while True:
        global number
        global turns
        turns = 1
        number = random.randint(1, 500)
        k = int(input("enter a number: ").strip())
        while (k != number):
            turns += 1
            if k > number:
                print("This number is too large")
            else:
                print("This number is too small")
            k = int(input("enter a number: ").strip())
        print("You got it in " + str(turns) + " turns!")
        k = input("Press 1 to play again, or anything else to quit ").strip()
        if (k != '1'):
            break