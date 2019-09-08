'''1) Input
Question
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
Solution'''
import datetime
person = input('Enter your name: ')
person = person.capitalize()
age = input('Enter your age: ')
now = datetime.datetime.now()
now.year
year_bth = int(now.year) - int(age)
to_the_years_100 = int(year_bth) + 100
print('{},'.format(person),"you will be 100 years ago in",int(to_the_years_100),'.')
