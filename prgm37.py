"""
UNIVERSITY QUESTION:MAY 2024(7 marks)
Consider the mathematical expression (a+b)2=a2+2ab+b2. Write a Python
program that takes user input for values of a and b, then evaluates both sides of
the expression. Finally, compare the results and print whether the equation holds
true or false.
"""
a=int(input("ENTER VALUE FOR \'a\':"))
b=int(input("ENTER VALUE FOR \'b\':"))
rhs=(a+b)**2
lhs=(a**2)+(2*a*b)+(b**2)
if rhs==lhs:
	print("TRUE")
else :
	print("FALSE")
