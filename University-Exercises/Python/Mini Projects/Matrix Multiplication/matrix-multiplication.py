#The aim of this program is to matrix multiplication without using the NumPy library

#To take rows and columns of the matrix A from the user
rows_A = int(input("Type the rows of the desired Matrix 'A': "))
cols_A = int(input("Type the columns of the desired Matrix 'A': "))

#To take rows and columns of the matrix B from the user
rows_B = int(input("Type the rows of the desired Matrix 'B': "))
cols_B = int(input("Type the columns of the desired Matrix 'B': "))

#To check if the multiplication is allowed
if cols_A != rows_B:
  print("It's Impossible to multiply due to the fact that the columns"
" of the matrix 'A' must be equivalent to the rows of the matrix 'B' or vice versa")
  exit()
print("\n")

#To create Matrix A
matrix_A = []
for i in range(1,rows_A+1):
  new_matrix_A = []
  for j in range(1,cols_A+1):
    value = int(input(f"Type the scalars [{i}],[{j}] : "))
    new_matrix_A.append(value)
  matrix_A.append(new_matrix_A)
print(f"\nMatrix 'A'")
for row in matrix_A:
  print(f"{row}")
print("\n")

#To create Matrix B
matrix_B = []
for i in range(1,rows_B+1):
  new_matrix_B = []
  for j in range(1,cols_B+1):
    value = int(input(f"Type the scalars [{i}],[{j}] : "))
    new_matrix_B.append(value)
  matrix_B.append(new_matrix_B)
print(f"\nMatrix 'B'")
for column in matrix_B:
  print(f"{column}")

#To create an empty matrix to save the result of the multiplication
C = []
for i in range(rows_A):
  col = []
  for j in range(cols_B):
    col.append(0)
  C.append(col)

#Matrix A multiplied by Matrix B and then save the result in the Matrix C
for i in range(rows_A):
  for j in range(cols_B):
    for k in range(rows_B):#The rows in matrix B are equal to the columns in matrix A
      C[i][j] = C[i][j] + matrix_A[i][k] * matrix_B[k][j]

#To show the result of the multiplication
print("\nMatrix A multiply by Matrix B")
for row in C:
  print(f"{row}") 
