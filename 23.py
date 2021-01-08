# Program to input an list and arrange all numbers in descending order

list = []
number = int(input("enter total number of items "))
for i in range(0,number):
    element = int(input())
    list.append(element)
print(list)

list.sort(reverse=True)
print( list )