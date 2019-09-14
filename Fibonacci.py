'''
13)Fibonacci
Question
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
Solution
'''
all_num = []
def gen():
    num = int(input("How many Fibonacci numbers to generate? "))
    if num<0:
        print("The number should be more than 0. Try again. ")
        gen()
    else:
        numbers = range(0,num)
        for i in numbers:
            all_num.append(i)
    return all_num
gen()
liste = []
for x in all_num:
    if x==0:
        print(f"For {x} this is 0")
        liste.append(x)
    elif x==1:
        print(f"For {x} this is 1")
        liste.append(x)
    elif x>1:
        sum = (x-1)+(x-2)
        print(f"For {x} this is {sum}")
        liste.append(sum)

y = len(all_num)
print(f"Fibonacci sequence for {y} numbers: {liste}")
