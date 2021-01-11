# Program to input "n" numbers and store it in a tuple and find maximum and minimum values in the tuple
t = tuple()
n = int(input('enter number of values '))

for i in range(n):
    values = int(input("enter values "))
    t = t + (values,)

print("maximum value in the tuple ",max(t))
print("minimum value in the tuple ",min(t))