# Program to input 5 subject names and put it in tuple and display the tuple information on the output screen
t = tuple()

for i in range(0,5):
    subject = input("enter subject ")
    t = t + (subject,)

print(t)
