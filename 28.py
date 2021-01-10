# Program to print the fibonacci Series up to an input limit

limit = int(input("enter limit "))
sum = 0
a=0
b=1
count = 0
while count < limit:
    sum = a+b

    print(sum)
    a = b
    b = sum 
    count +=1
    
