a = int(input("Enter 1 For Multiplication And 2 For Addition, 3 For Subtraction And 4 For Division: "))
b = int(input("Enter The First Number: "))
c = int(input("Enter The Second Number: "))
if(a == 1):
    multiplication = b * c
    print (multiplication)
if(a == 2):
    addition = b + c
    print(addition)
if(a == 3):
    subtraction = b - c
    print(subtraction)
if(a == 4):
    division = b/c
    print(division)
