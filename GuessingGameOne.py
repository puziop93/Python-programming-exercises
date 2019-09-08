'''
9) Guessing Game One
Question
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
Solution
'''
import random
x = True
y = False
count = 1
while x:
    user = int(input("Enter the number from 1 to 9 "))
    rand = random.randint(1,10)
    if user == rand:
        count =+ count
        print('exactly right')
    elif user> rand:
        print('Too hight, correct number is {}'.format(rand))
    else:
        print('too low, correct number is {}'.format(rand))
    user = input("Do you want continue game? Y/N ")
    if user.lower() == 'y':
        pass
    else:
        print('You won {} times'.format(count))
        break
