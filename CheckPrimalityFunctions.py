'''
11) Check Primality Functions
Question
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.
Solution
'''
def num():
    n = int(input("Give me a number "))
    if n <2:
        print(f"Number {n} is neither prime nor composite")
        n = int(input("Give me a number "))
    else:
        n = n
    return n

number = num()

x = list(range(1,number+1))
sum=[]
for elem in x:
    if number%elem == 0:
        sum.append(elem)
        print("Divisor of number {} is: {}".format(number,elem))
    else:
        continue
print(sum)
    
if len(sum)>0 and len(sum)<3:
    print("Number {} is primary key".format(number))
else:
    print("Number {} is not primary key".format(number))
