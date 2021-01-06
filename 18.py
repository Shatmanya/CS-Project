# Program to print sum of odd and even numbers
limit=int(input("enter a number as limit "))
even=0
odd=0
for i in range(1,limit+1):
    if i%2==0:
        even+=i
    else:
        odd+=i

print("sum of even numbers are ",even)
print("sum of odd number are ",odd)