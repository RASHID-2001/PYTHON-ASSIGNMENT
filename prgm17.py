"""
PYTHON PROGRAM TO PRINT THE PATTERN:-
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
6 5 4 3 2 1 
7 6 5 4 3 2 1
8 7 6 5 4 3 2 1 
9 8 7 6 5 4 3 2 1
"""
for i in range(1,10):
	for j in range(1,i+1):
		print(j,end=" ")
	print()