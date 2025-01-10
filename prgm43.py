"""
UNIVERSITY QUESTION:MAY 2023 (7 marks)
Write a Python program to find the roots of a quadratic equation, ax^2+ bx + c =0 . Consider the cases of both real and imaginary roots.
"""
print("ax^2+bx+c")
a=float(input("ENTER VLUE FOR a:"))
b=float(input("ENTER VLUE FOR b:"))
c=float(input("ENTER VLUE FOR c:"))
desc=(b**2)-(4*a*c)
if desc<0:
	print(f"root1={(-1*b)/(2*a)}+{(-desc)/(2*a)}i")
	print(f"root2={(-1*b)/(2*a)}-{(-desc)/(2*a)}i")
else:
	desc=(desc)**0.5
	print(f"root1={((-1*b)+desc)/(2*a)}")
	print(f"root2={((-1*b)-desc)/(2*a)}")
	
