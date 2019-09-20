"""
16)Password Generator
Question
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
Solution
"""
import random
import string


while 1:
    choose = input("Choose a way of generation your \
password \nPress a (weak password) if you want to have a specific word in your password \nPress b (strong password) if you want to have the password generated in full \n")

    def user():
        us = 0
        us = input("Enter a password containing at least five characters: ")

        while len(us)<5:
            print('Password is too short. Try again')
            us = input("Enter a password containing at least five characters: ")
        return us

    tab2=[]
    def mixstring_norepeat(x, length = 10):
        for i in range(length):
            tab2.append(random.choice(x))
            mix3 = ''.join(tab2)
        return mix3
    def mixstring(x, length = 10):
        return ''.join(random.sample(x,length))

    tab1 = []
    if choose.lower() == "a":
        spec = string.punctuation
        upper = string.ascii_uppercase
        number = string.digits
        gen1 = spec+upper+number
        gen2 = mixstring(gen1,3)
        gen3 = user()+gen2
        print("Password was created for you. It is: ",gen3)
    if choose.lower() == "b":
        spec = string.punctuation
        upper = string.ascii_uppercase
        number = string.digits
        swap = string.capwords
        gen2 = spec+upper+number
        print("Password was created for you. It is: ",mixstring_repeat(gen2))

    again = input("If you want to generate new password, press 'Y/N'\n")
    if again.lower() == "y": pass
    else:
        break
