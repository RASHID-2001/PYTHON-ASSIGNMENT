"""
QN:MAY2023
WRITE A PANDAS PROGRAM TO READ THE CSV FILE NAMED"diamond.csv"WITH THE FOLLOWING FIELDS
carat, cut, color, clarity, depth, and price and to print the following:
1. Number of rows and columns
2. First five rows
"""
import pandas as pd

df = pd.read_csv("diamond.csv")

#1
print("\nNumber of rows and columns in the dataset:")
print(df.shape)  

#2
print("\nFirst five rows of the dataset:")
print(df.head())  