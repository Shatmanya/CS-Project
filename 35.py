# Program to create phonebook and delete particular phone number using name
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
print("Remove Name and Number")
name_del = input("Name: ")
if name_del in numbers:
    del numbers[name]