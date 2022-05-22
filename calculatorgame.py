import random
import time
#original = input('input a number: ')
#original = int(original)
#n = original
#strn = str(n)

highscore = 0
num_turns = 0
starting_number = random.randint(0,700)
num_to_get = random.randint(0,700)
while (starting_number == num_to_get):
    starting_number = random.randint(0, 700)

#turns number into a list of its digits
def num_listing(number):
    exponentiate = 10**(len(str(number)) - 1)
    digits = []
    while exponentiate >= 1:
        digits.append(int(number//exponentiate))
        number -= (number//exponentiate)*exponentiate
        exponentiate = exponentiate / 10
    return digits

#turns list of digits back into the number
def list_to_num(digits_list):
    exponent = 10 ** (len(digits_list) - 1)
    num = 0
    for x in digits_list:
        num += (x * exponent)
        exponent = exponent / 10
    return int(num)

#print(list_to_num([1,2,3,4]))

#sorts a number's digits from biggest to smallest then returns that number
def sort_big_to_small(number):
    listing = num_listing(number)
    ordered_list = []
    max_len = len(listing)
    #max_i = 0
    cmax = 0
    #c_i = 0
    cmax_occurrences = []
    while len(ordered_list) < max_len:
        for x in listing:
            if x > cmax:
                cmax = x
        for m in listing:
            if m == cmax:
                cmax_occurrences.append(1)
        n = len(cmax_occurrences)
        for x in range(n):
            listing.remove(cmax)
            ordered_list.append(cmax)
            cmax_occurrences.remove(1)
        cmax = 0
    return ordered_list
##print(sort_big_to_small(347581842))
##print('should be 887544321')


#addition
def additions(number, adding):
    number += adding
    return number
##print(additions(13, 5))
##print('should be 18')

#subtraction
def subtraction(number, subbing):
    number -= subbing
    return number
##print(subtraction(13,5))
##print('should be 8')

#division
def division(number, divisor):
    number = int(number / divisor)
    return number
##print(division(12,4))
##print('should be 3')

#multiplication
def multiply(number, multiple):
    number *= multiple
    return number
##print(multiply(12,3))
##print('should be 36')

#deletes the last digit in a number
def backspace(number):
    digits_list = num_listing(number)
    return list_to_num(digits_list[:len(digits_list) - 1])
#    m = len(digits_list)
#    for x in range(m):
#        digits_list[x] = str(digits_list[x])
#    digits_list = digits_list[:m - 1]
#    for y in range(m - 1):
#        digits_list[y] = int(digits_list[y])
#    n = list_to_num(digits_list)
#    return n
##print(backspace(1234))
##print('should be 123')

#deletes the first digit in a number
def frontspace(number):
    digits_list = num_listing(number)
    return list_to_num(digits_list[1:])
##print (frontspace(1234))
##print ("should be 234")

#adds a digit onto the end of the number
def backadd(number, digit):
    digits_list = num_listing(number)
    digits_list.append(digit)
    n = list_to_num(digits_list)
    return n
##print(frontadd(1234, 3))
##print('should be 12343')

def frontadd(number, digit):
    digits_list = num_listing(number)
    result = [digit]
    for k in digits_list:
        result.append(k)
    return list_to_num(result)
# print(frontadd(1234,3))

#converts all of the digits(converting) that are a certain number to another number(replacing)
def convert(number, converting, replacing):
    digits_list = num_listing(number)
    for x in range(len(digits_list)):
        if digits_list[x] == converting:
            digits_list[x] = replacing
    n = list_to_num(digits_list)
    return n

#returns the digits in largest to smallest order
def big_to_small(number):
    n = list_to_num(sort_big_to_small(number))
    return n
#print(big_to_small(564739))
#print('should be 976543')

#returns the digits in smallest to largest order
def small_to_big(number):
    n = list_to_num(sort_big_to_small(number)[::-1])
    return n
#print(small_to_big(476849))
#print('should be 446789')


#replaces all occurrences of a digit or string of digits with another
def replace(number, converting, replacement):
    num_string = str(number)
    convert = str(converting)
    replace = str(replacement)
    new_num = num_string.replace(convert, replace)
    num = int(new_num)
    return num
#print(replace(1234, 1, 4))
#print('should be 4234')
#print(replace(1234, 12, 23))
#print('should be 2334')
#print(replace(1234, 12, 6))
#print('should be 634')

def options():
    print("Here are the moves you can take:")
    print("Rearrange the digits smallest to largest - 1")
    print("Rearrange the digits largest to smallest - 2")
    print("Add a number between 1 and 9 inclusive - 3")
    print("Subtract a number between 1 and 9 inclusive - 4")
    print("Divide by any positive integer. Returns the quotient - 5")
    print("Multiply by any positive integer - 6")
    print("Deletes the last digit of the number - 7")
    print("Deletes the first digit of the number - 8")
    print("Add a digit onto the end of the number - 9")
    print("Add a digit onto the front of the number - 10")
    print("Convert all occurrances of a digit to another digit - 11")
    print("Stop the current game - \"stop\"")


def turn(num, n):
    if (n==1):
        return small_to_big(num)
    if (n == 2):
        return big_to_small(num)
    if (n == 3):
        k = input("Enter a number between 1 and 9: ")
        try:
            k = int(k.strip())
        except:
            print("Please enter an integer")
        if (k <= 0 or k > 9):
            print("Please enter a valid number")
            return num
        return (num + k)
    if (n == 4):
        k = input("Enter a number between 1 and 9: ")
        try:
            k = int(k.strip())
        except:
            print("Please enter an integer")
        if (k <= 0 or k > 9):
            print("Please enter a valid number")
            return num
        return (num - k)
    if (n == 5):
        k = input("Enter a positive integer: ")
        try:
            k = int(k.strip())
        except:
            print("Please enter an integer")
        if (k <= 0):
            print("Please enter a valid integer")
            return num
        return (num/k)
    if (n == 6):
        k = input("Enter a positive integer: ")
        try:
            k = int(k.strip())
        except:
            print("Please enter an integer")
        if (k <= 0):
            print("Please enter a valid integer")
            return num
        return (num*k)
    if (n == 7):
        return backspace(num)
    if (n == 8):
        return frontspace(num)
    if (n == 9):
        k = input("Enter a positive integer: ")
        try:
            k = int(k.strip())
        except:
            print("Please enter an integer")
        if (k <= 0 or k > 9):
            print("Please enter a valid digit")
            return num
        return backadd(num, k)
    if (n == 10):
        k = input("Enter a positive integer: ")
        try:
            k = int(k.strip())
        except:
            print("Please enter an integer")
        if (k <= 0 or k > 9):
            print("Please enter a valid digit")
            return num
        return frontadd(num, k)
    if (n == 11):
        k = input("Enter the digit to replace: ")
        j = input("Enter the replacement digit: ")
        try:
            k = int(k.strip())
            j = int(j.strip())
        except:
            print("Please enter an integer")
        if (k <= 0 or k > 9 or j <= 0 or j > 9):
            print("Please enter a valid digit")
            return num
        return convert(num, k, j)
    else:
        print("Invalid input, please try again")
        return num
        


def game():
    print('goal: ' + str(num_to_get))
    print('starting number: ' + str(starting_number) + '\n')
    current_number_state = starting_number
    global num_turns
    num_turns = 0
    while (current_number_state != num_to_get):
        options()
        step_to_take = input("Enter a value: ")
        if (step_to_take.strip() == 'stop'):
            return
        try:
            step_to_take = int(step_to_take.strip())
        except:
            print('please enter a valid number')
        print()
        current_number_state = turn(current_number_state, step_to_take)
        print("your current number: " + str(current_number_state) + ", your goal: " + str(num_to_get))
        print()
        num_turns += 1
        time.sleep(1.5)
        print('number of turns: ' + str(num_turns))
    print("Congratulations!")
    global highscore
    if (highscore == 0 or num_turns < highscore):
        print("You got a new high score of " + str(num_turns) + "!!")
        highscore = num_turns
    

def main():
    print("Welcome to the Calculator Game! You are given two numbers: your goal and your starting number.")
    print("The objective of the game is to arrive from the starting number to the goal in the fewest turns.")
    print("Good luck!")
    game()
    # print('here')
    # print(starting_number)
    # print(num_to_get)
    # print(num_turns)
    while (True):
        print("restart - 1 \nTo quit, enter any other number \n")
        retry = input("Enter a number")
        if (retry == "1"):
            print('\n')
            game()
            # print(starting_number)
            # print(num_to_get)
            # print(num_turns)
            # print(highscore)
        else:
            break
    # print('finished')
        

