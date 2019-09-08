'''5) List Overlap
Question
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.
Solution
'''
x = [1, 1, 2, 2, 3, 5, 8, 13, 1, 21, 34, 55, 89]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
z = []
for el in x:
    if el not in z:
        z.append(el)
for el in y:
    if el not in z:
        z.append(el)
print("This is ",z)
