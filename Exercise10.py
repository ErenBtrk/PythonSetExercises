'''
10. Write a Python program to check if a set is a subset of another set.
'''

print("Check if a set is a subset of another set, using comparison operators and issubset():\n")
setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setz = set(["mango"])
print("x: ",setx)
print("y: ",sety)
print("z: ",setz,"\n")
print("If x is subset of y")
print(setx <= sety)
print(setx.issubset(sety))
print("If y is subset of x")
print(sety <= setx)
print(sety.issubset(setx))
print("\nIf y is subset of z")
print(sety <= setz)
print(sety.issubset(setz))
print("If z is subset of y")
print(setz <= sety)
print(setz.issubset(sety))