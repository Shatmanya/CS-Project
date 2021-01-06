# Program to identify whether the entered string is upper case,lower case,digit or special character

string=input("enter a string ")

if string[0].isupper():
    print('\n',"it is a upper case string")
elif string[0].islower():
    print('\n',"it is a lower case string")
elif string[0].isdigit():
    print('\n',"digit")
else :
    print('\n',"it is a special character")