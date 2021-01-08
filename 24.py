# Menu driven program to convert temperature in fahrenheit and celcius

print("Enter temperature in ")
print("1.Celcius")
print("2.Farhenheit")
choice = int(input())
temperature = int(input("enter temperature "))

if choice ==1:
    farhenheit=(temperature *  9/5) + 32 
    print("Farhenheit ",farhenheit)
elif choice ==2:
    Celcius = (temperature - 32) * 5/9
    print("Celcius ",Celcius)
else:
    print("invlid choice")


