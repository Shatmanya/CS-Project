# Program to input 'n' names and phone numbers to store it in a dictionary and print the phone number if a particular name

n = int( input('enter number of contacts '))
numbers = {}
for i in range(1,n+1):
    print("Add Name and Number")
    name = input("Name: ")
    phone = input("Number: ")
    numbers[name] = phone

a = input("enter name for details ")

for i in numbers:
    if i == a:
        print(numbers[name])
