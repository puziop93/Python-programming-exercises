'''2) Odd Or Even
Question
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
Solution'''
number = float(input("Enter a number "))
remainder = float(number % 2)
if remainder == 0:
    print("The number is even, because the remainder is 0")
else:
    print("The number is odd")
