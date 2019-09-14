"""
12)List Ends
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
Solution
"""
def num():
    return input("Enter numbers: ")
lista=[]
numbers = num().split()
for i in numbers:
    lista.append(int(i))
def first(lista):
    return print("The first element is",lista[0])
def last(lista):
    return print("The last element is",lista[-1])
first(lista)
last(lista)
