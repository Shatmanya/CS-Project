# Program to take temperature for seven days and print it's average

temperature = []

print("enter temperatur of seven days")
for i in range(1,8):
    print("Day ",i)
    Day = int(input())
    temperature.append(Day)
sum=0
for j in temperature:
    sum += j
print("sum",sum)
average = sum/7
print("Average Temperature", average)