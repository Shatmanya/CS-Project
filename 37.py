# Program to input 'n ' numbers and store it in tuples
t = tuple ( )  
n = input ("enter limit")  
print("enter all numbers one by one")  
for i in range (n) :  
    a = input ("enter Numbers")  
    t = t+(a, )  
print("Output is ")
print(t)