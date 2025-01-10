"""
UNIVERSITY QUESTION:-JUNE 2023 (7marks)
Write a python program to generate the following type of pattern for the given N rows where N <= 26.
A
A B
A B C 
A B C D 
"""
N=int(input("ENTER A NUMBER:"))
if N<=0 or N>26:
	print("PLEASE ENTERA NUMBER IN BETWEEN 1-26")
else:
	for i in range(0,N):
		for j in range(i+1):
			print(chr(65+j),end=" ")
		print()