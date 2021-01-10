# Program to find sum of rows and columns of the matrix

rows = int(input("Enter the Number of rows : " ))
column = int(input("Enter the Number of Columns: "))

print("Enter the elements of First Matrix:")
matrix= [[int(input()) for i in range(column)] for i in range(rows)]
print("First Matrix is: ")
for n in matrix:
    print(n)

sum_rows=0
sum_column = 0
for i in range(rows) : 
    for j in range(column) :   
        sum_rows += matrix[i][j] 
   
    print("Sum of the row",i,"=",sum_rows) 
  
for i in range(column) : 
    for j in range(rows) :   
        sum_column += matrix[i][j] 
   
    print("Sum of the column",i,"=",sum_column) 