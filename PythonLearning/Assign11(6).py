rows=int(input("Enter the number of rows:"))
cols=int(input("Enter the number of columns:"))

matrix=[]

for i in range(rows):
    row=[]
    for j in range(cols):
        x=input(f"Enter the row value {i+1}: ")
        row.append(x)
    matrix.append(row)
print(matrix)


