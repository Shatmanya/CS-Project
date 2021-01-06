# Program to check whether the entered year is leap year or not

year = int(input("enter year to check "))

if year%4==0:
    print("leap year")
else:
    print("Not a leap year")