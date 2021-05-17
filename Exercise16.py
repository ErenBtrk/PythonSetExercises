'''
16. Write a Python program to check if a given value is present in a set or not.
'''

set1 = set([1,2,3,4,5,6,7,8,9,10])

n = 11

if n in set1:
    print(f"{n} is in the list.")
else:
    print(f"{n} is not in the list.")