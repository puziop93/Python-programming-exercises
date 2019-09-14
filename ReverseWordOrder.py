"""
15)Reverse Word Order
Question
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.
Solution
"""
def string():
    string = input("Enter a string: ")
    string = string.split()
    x =string[::-1]
    b =" ".join(x)
    return print(b.capitalize())
string()
