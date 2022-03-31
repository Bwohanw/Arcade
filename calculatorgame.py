import random
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

#adds a digit onto the beginning of the number
def frontadd(number, digit):
    digits_list = num_listing(number)
    digits_list.append(digit)
    n = list_to_num(digits_list)
    return n
##print(frontadd(1234, 3))
##print('should be 12343')

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

def main():
    print('goal: ' + str(num_to_get))
    print('starting number: ' + str(starting_number))
    current_number_state = starting_number
    global num_turns
    num_turns = 0
    while (current_number_state != num_to_get):
        step_to_take = input("enter a value: ")
        try:
            step_to_take = int(step_to_take)
        except:
            print('please enter a valid number')
        if (step_to_take== 1):
            current_number_state = small_to_big(current_number_state)
        elif (step_to_take == 2):
            current_number_state = num_to_get
        print(current_number_state)
        print(starting_number)
        num_turns += 1
        print('number of turns:' + str(num_turns))
    print('finished')
    global highscore
    if (highscore == 0 or num_turns < highscore):
        print("New high score!")
        highscore = num_turns
    

if __name__ == "__main__":
    main()
    print('here')
    print(starting_number)
    print(num_to_get)
    print(num_turns)
    while (True):
        retry = input("restart - 1 \n quit - q")
        if (retry == "1"):
            main()
            print(starting_number)
            print(num_to_get)
            print(num_turns)
            print(highscore)
        else:
            break
    print('finished')
        

