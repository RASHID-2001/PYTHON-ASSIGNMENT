"""
UNIVERSITY QUESTION:JUNE 2022

Write a python program to generate the following type of pattern for the given N
rows .
1
1 2
1 2 3
1 2 3 4

"""
n=int(input("ENTER THE NUMBER OF ROWS:"))
for i in range(1,n+1):
	for j in range(1,i+1):
		print(j,end=" ")
	print()
	
		