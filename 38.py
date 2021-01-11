# program to input two tuples and interchange the tuple values in python

t1 = tuple( )  
n = input("Total number of values m first tuple") 
for i in range (n):  
    a = input("Enter elements")  
t2 = t2 + (a, ) 
print ("First tuple")  
print (t1) 
print("Second tuple")  
print( t2 ) 
t1, t2 = t2, t1
print("After swapping" )
print("First tuple")  
print(t1)  
print("Second tuple")  
print(t2)