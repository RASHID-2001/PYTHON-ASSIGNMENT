"""
UNIVERSITY QUESTION:MAY 2024(6 marks)
Write a python program to print factorial of a given number
"""
n=int(input("ENTER A NUMBER:"))
if n==0 or n==1:
	print(f"{n}! = 1")
else:
	fact=1
	for j in range(1,n+1):
		fact*=j
	print(f"{n}! = {fact}")