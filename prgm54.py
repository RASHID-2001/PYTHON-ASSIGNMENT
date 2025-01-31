"""
UNIVERSITY QUESTION:JANUARY 2024

Write a Python program to convert a decimal number to its binary equivalent.

"""
dec=int(input("ENTER A NUMBER:"))
if dec==0:
	print(f"BINARY REPRESNTATION OF {dec} IS 0")
else:
	bin=""
	n=dec
	while n>0:
		b=n%2
		bin+=str(b)
		n=n//2
	bin=bin[::-1]
	print(f"BINARY REPRESNTATION OF {dec} IS ",bin)
		