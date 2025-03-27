"""
QN:Write a python program to create two numpy arrays of random integers between
0 and 20 of shape (3, 3) and perform the following operations.
1. Perform element-wise addition of two NumPy arrays.
2. Calculate the mean and standard deviation of first NumPy array.
3. Multiply each element of first NumPy array by a scalar value.
4.Compute the dot product of two matrices using NumPy.(MAY 2024)

"""
import numpy as np


np.random.seed(42)  # For reproducibility
A = np.random.randint(0, 21, (3, 3))
B = np.random.randint(0, 21, (3, 3))

C = A + B


mean_A = np.mean(A)
std_A = np.std(A)


A_scaled = A * 2


dot_product = np.dot(A, B)

print("Array A:\n", A)
print("\nArray B:\n", B)
print("\nElement-wise Addition (A + B):\n", C)
print("\nMean of A:", mean_A)
print("Standard Deviation of A:", std_A)
print("\nA multiplied by 2:\n", A_scaled)
print("\nDot Product of A and B:\n", dot_product)
