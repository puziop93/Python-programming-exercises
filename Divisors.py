'''
4) Divisors
Question
Create a program that asks the user for the natural number and then prints out a list of all the divisors of that number.
Solution
'''
def isare(x):
    if len(div) >1:
        x = 'are'
    else:
        x = 'is'
    return x

def divi(y):
    if len(div) >1:
        y = 'Divisors'
    else:
        y = 'Divisor'
    return y

def naturalNumber(help_text = "Enter the natural number "):
    n = 0
    while n<1:
        print("It is not the natural number. Try again.")
        n = int(input(help_text))
    return n

number = naturalNumber()
div=[]
x = range(1,number+1)
for elem in x:
    if number%elem ==0:
        div.append(elem)
    else:
        pass
