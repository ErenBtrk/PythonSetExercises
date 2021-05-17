'''
6. Write a Python program to create an intersection of sets.
'''

set1 = set([1,2,3,4,5])
set2 = set([3,4,5])

newset = set()
for item in set1:
    if(item in set2):
        newset.update([item])

print(newset)

################################################################################################

#Intersection
setx = set(["green", "blue"])
sety = set(["blue", "yellow"])
setz = setx & sety
print(setz)
