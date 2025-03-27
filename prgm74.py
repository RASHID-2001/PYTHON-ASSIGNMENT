"""
Write a Python program to input two matrices and perform the following
operations using numpy and display the results:
1. Add the matrices
2. Subtract the matrices
3. Multiply the matrices
4. Find transpose of the matrices(MAY2024)

"""
import numpy as np
def input_matrix(rows, cols, name):
    print(f"Enter elements of Matrix {name} (row-wise):")
    l = []
    for i in range(rows):
        l1=[]
        for j in range(cols):
           l1.append(int(input()))
        l.append(l1)
    return np.array(l)  


rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))


A = input_matrix(rows, cols, "A")
B = input_matrix(rows, cols, "B")

# 1- Matrix Addition
addition = A + B

# 2- Matrix Subtraction
subtraction = A - B

# 3- Matrix Multiplication (Dot Product)
if A.shape[1] == B.shape[0]:  # Ensure valid multiplication dimensions
    multiplication = np.dot(A, B)
else:
    multiplication = "Matrix multiplication not possible (column count of A must match row count of B)"

# 4- Transpose of Matrices
transpose_A = A.T
transpose_B = B.T

print("\nMatrix A:\n", A)
print("\nMatrix B:\n", B)
print("\nMatrix Addition (A + B):\n", addition)
print("\nMatrix Subtraction (A - B):\n", subtraction)
print("\nMatrix Multiplication (A * B):\n", multiplication)
print("\nTranspose of Matrix A:\n", transpose_A)
print("\nTranspose of Matrix B:\n", transpose_B)
