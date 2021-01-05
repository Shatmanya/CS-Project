# Program to print factorial of given number

number=int(input("enter number "))
factorial=1

for i in range(1,number + 1):
    factorial = factorial*i
print("The factorial of",number,"is",factorial)