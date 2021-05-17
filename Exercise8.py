'''
8. Write a Python program to create set difference.
'''

setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setz = setx & sety
print(setz)
#Set difference
setb = setx - setz
print(setb)
setc = sety - setz
print(setc)