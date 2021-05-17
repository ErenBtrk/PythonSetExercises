'''
5. Write a Python program to remove an item from a set if it is present in the set.
'''

set1 = set([1,2,3,4,5])

set1.discard(2)

print(set1)

set1.discard(6)

print(set1)