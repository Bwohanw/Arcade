from functools import partial
import random
import linecache
import string

word = ""
wrong_letters = set()
turns = 6
known_letters = ["_","_","_","_","_"]
partial_letters = {}
unknown_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def main():
    while True:
        global word
        global wrong_letters
        global turns
        global known_letters
        global partial_letters
        word = ""
        wrong_letters = set()
        turns = 6
        known_letters = ["_","_","_","_","_"]
        partial_letters = {}
        word = linecache.getline('wordleword.txt', random.randint(1, 2315)).strip()
        print("Tip: Enter a question mark to review what each symbol means")
        while turns > 0:
            guess = input().strip().lower()
            if guess == word:
                break
            move(guess)
            print("you have " + str(turns) + " turns left")
        if turns == 0:
            print("Sorry, that's all your moves")
            print("The word was " + word)
        else:
            turns -= 1
            print("congratulations! You got it in " + str(6 - turns) + " tries")
        k = input("Press 1 to play again, or anything else to quit: ").strip()
        if (k != '1'):
            break

def move(guess):
    global wrong_letters
    global turns
    global known_letters
    global partial_letters
    if (guess == '?'):
        print("O means the position and letter are correct. Y means the letter is right but the position is wrong. X means the letter is not in the word.")
        return
    if (len(guess) != 5 or not guess.isalpha()):
        print("Enter a valid guess")
        return
    indices = {}
    correctness = ['','','','','']
    for x in guess:
        indices[x] = []
    for x in range(5):
        global unknown_letters
        if guess[x] in unknown_letters:
            unknown_letters.remove(guess[x])
        if isGreen(guess, x):
            indices[guess[x]].append(x)
            correctness[x] = 'O'
            known_letters[x] = guess[x]
        else:
            correctness[x] = 'X'
            if isGray(guess, x):
                wrong_letters.add(guess[x])
    for x in range(5):
        if isYellow(guess, x, indices):
            correctness[x] = 'Y'
            if guess[x] not in partial_letters:
                partial_letters[guess[x]] = set()
            partial_letters[guess[x]].add(x)
    turns -= 1
    for x in word:
        if allFound(x):
            if x in partial_letters:
                partial_letters.pop(x)
    c = ""
    for x in correctness:
        c += x
    k = ""
    for x in known_letters:
        k += x
    print(c)
    u = ""
    for x in unknown_letters:
        u += x
    print("known letters: " + k)
    print("wrong letters: " + setToString(sorted(wrong_letters)))
    print("partial letters: " + dictToString(partial_letters))
    print("unknown letters: " + setToString(unknown_letters))
    

def isGreen(guess, index):
    return guess[index] == word[index]
def isGray(guess, index):
    return guess[index] not in word

def isYellow(guess, index, indices):
    letter = guess[index]
    if isGray(guess, index):
        return False
    occurrance = numOccurrances(letter, word)
    if not inList(index, indices[letter]):
        if len(indices[letter]) < occurrance:
            indices[letter].append(index)
            return True
    return False

def numOccurrances(letter, thing):
    counter = 0
    for x in thing:
        if x == letter:
            counter += 1
    return counter

def inList(element, list):
    for x in list:
        if x == element:
            return True
    return False

def allFound(letter):
    return numOccurrances(letter, word) == numOccurrances(letter, known_letters)
def setToString(s):
    str = ""
    for x in s:
        str += x + ", "
    return str[:len(str)-2]

def dictToString(d):
    str2 = ""
    for x in sorted(d):
        str2 += x + ": "
        for y in sorted(d[x]):
            str2 += str(y) + ", "
    return str2[:len(str2) - 2]