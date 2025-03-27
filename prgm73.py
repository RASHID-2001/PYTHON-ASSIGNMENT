"""
Write a python program to create two numpy arrays of random integers between 0 and 20 of shape (3, 3) and perform matrix addition, multiplication and transpose of the product matrix.
MAY 2023
"""
import numpy as np


np.random.seed(42)  # For reproducibility
A = np.random.randint(0, 21, (3, 3))
B = np.random.randint(0, 21, (3, 3))

addition = A + B

multiplication = np.dot(A, B)

transpose_product = multiplication.T    #TRANSPOSE 


print("Matrix A:\n", A)
print("\nMatrix B:\n", B)
print("\nMatrix Addition (A + B):\n", addition)
print("\nMatrix Multiplication (A * B):\n", multiplication)
print("\nTranspose of the Product Matrix:\n", transpose_product)
