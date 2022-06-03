import random
import linecache

word = ""
#while (len(word) <= 4):
#     turns = random.randint(1,10000)
#     word = linecache.getline('wordlist', turns).strip()
# print(word)

word_as_list = []
for x in word:
    word_as_list.append(x)

lives = 10

solution = []
for x in word:
    solution.append('_')

incorrect_chars = []

solved = False

def list_to_string(arr):
    res = ""
    for x in arr:
        res += x + ' '
    return res
print(list_to_string(word_as_list))


def guess_letter(a):
    if (not a.isalpha()) or (len(a) != 1):
        print("Please enter a letter")
        return
    changed = False
    for x in range(len(word_as_list)):
        print(word_as_list)
        if word_as_list[x] == a:
            print('here')
            solution[x] = a
            changed = True
    if (list_to_string(solution) == list_to_string(word_as_list)):
        global solved
        solved = True
    if not changed:
        global incorrect_chars
        if a not in incorrect_chars:
            global lives
            lives -= 1
            print("uh oh, you lost a life! Current lives remaining: " + str(lives))
            incorrect_chars.append(a)

def check_word(a):
    if (not a.isalpha()):
        print("Please enter a letter")
        return
    if (a == word):
        global solved
        solved = True
    else:
        global incorrect_chars
        if a not in incorrect_chars:
            global lives
            lives -= 1
            print("uh oh, you lost a life! Current lives remaining:" + str(lives))
            incorrect_chars.append(a)


def game():
    while (lives > 0):
        print("Lives left: " + str(lives))
        if (len(incorrect_chars) != 0):
            print("Incorrect guesses: " + list_to_string(incorrect_chars))
            print()
        print(list_to_string(solution))
        k = input("Please enter a guess")
        k = k.strip().lower()
        if (len(k) != 1):
            check_word(k)
        else:
            guess_letter(k)
        if solved:
            break
    if solved:
        print("Congratulations! You guessed the word with " + str(lives) + "remaining")
    else:
        print("Sorry, you didn't get the word this time")



def main():
    while True:
        global word
        global word_as_list
        global lives
        global solution
        global incorrect_chars
        global solved
        word = ""
        word_as_list = []
        lives = 10
        while (len(word) <= 4):
            turns = random.randint(1,10000)
            word = linecache.getline('wordlist', turns).strip()
        for x in word:
            word_as_list.append(x)
        solution = []
        for x in word:
            solution.append('_')
        incorrect_chars = []
        solved = False
        game()
        k = input("Enter 1 to play again or any other key to exit.")
        if (k.strip() != '1'):
            break
    print("Thanks for playing!")