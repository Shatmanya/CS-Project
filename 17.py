# Program to show if the user entered even number then the message will show "Congractulations! you entered an even number"
#else it will ask to try again
even = int()
while even!=1:
    number=int(input("enter a number to check "))

    if number%2==0:
        print("Congractulations! you entered an even number")
        even=1
    else:
        print("please try again")