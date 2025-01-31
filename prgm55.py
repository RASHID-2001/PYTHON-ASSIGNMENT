"""
UNIVERSITY QUESTION:JANUARY 2024

Write a Python program to compute the sum of the series (1- x2/2! + x4/4! –
x6/6!+..........n terms).

"""
n=int(input("ENTER THE NUMBER OF TERMS:"))
x=int(input("ENTER THE ANGLE VALUE:"))
value=0
for k in range(n):
	fact=1
	for i in range(1,(2*k)+1):
		fact*=i
	term = ((-1) ** k) * (x ** (2 * k)) /fact
	value += term
print(f"COS({x})={value}")
	