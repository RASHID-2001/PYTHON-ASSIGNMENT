"""
QN:Write a python program to create a 3x3 matrix named A with random integer
values between 1 and 10.(MAY 2024)
"""
import numpy as np
A = np.random.randint(1, 11, (3, 3))
print("Matrix A:\n", A)
