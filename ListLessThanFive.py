'''3) List Less Than five
Question
Take a list, say for example this one:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5
Solution'''
import string
a= [1,1,2,3,5,8,13,21,34,55,89]
b=[]
print(a)
for element in a:
    if element < 5:
        b.append(str(element))
        newb = ','.join(b)
    else:
     pass
print(f'Elements of the list that are less than 5: {newb}')
