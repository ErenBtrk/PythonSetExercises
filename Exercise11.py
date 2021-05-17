'''
11. Write a Python program to create a shallow copy of sets. 
Note : Shallow copy is a bit-wise copy of an object.
A new object is created that has an exact copy of the values in the original object.
'''

set1 = set(["red","green"])
set2 = set(["green","red"])

set3 = set1.copy()

print(set1)
print(set2)
print(set3)