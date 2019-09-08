'''
6) String Lists
Question
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
Solution
'''
string = input("Enter a string \n")
if string.lower() == string[::-1].lower():
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")
