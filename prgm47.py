"""
UNIVERSITY QUESTION:-JUNE 2023 (7marks)
Write a python program to generate the following type of pattern for the given N rows where N <= 26.
A
A B
A B C 
A B C D 
"""
N=int(input("ENTER A NUMBER:"))
for i in range(0,N):
	for j in range(i+1):
		print("*",end=" ")
	print()