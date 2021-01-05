# Program to ask user for the beginning number and ask for ending number and print the sum from beginning to ending series
beginning =int(input("enter beginning number "))
ending = int(input("enter the ending number "))

sum = 0

for i in range(beginning , ending+1):
    sum+=i

print(sum)