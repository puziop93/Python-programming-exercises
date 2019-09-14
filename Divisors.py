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

def naturalNumber():
    n = int(input("Enter the natural number "))
    if n <1:
        print(f"It is not the natural number. Try again.")
        n = int(input("Enter the natural number "))
    else:
        n = n
    return n

number = naturalNumber()
div=[]
x = range(1,number+1)
for elem in x:
    if number%elem ==0:
        div.append(elem)
    else:
        pass
print(divi(div),f"of the number {number}",isare(div),":",div)
