# Program to print lower triangle matrix

rows = int(input("Enter the Number of rows : " ))
column = int(input("Enter the Number of Columns: "))

print("Enter the elements of First Matrix:")
matrix= [[int(input()) for i in range(column)] for i in range(rows)]
print("First Matrix is: ")
for n in matrix:
    print(n)

for i in range(rows):
    for j in range(column):
        if(i>=j):
            print(matrix[i][j],end="\t")
        else:
            print(' ',end="\t")
    print()