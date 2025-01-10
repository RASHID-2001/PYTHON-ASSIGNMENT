"""
UNIVERSITY QUESTION: JANUARY 2024
Write a program that accepts the lengths of three sides of a triangle as inputs and
outputs whether or not the triangle is a right triangle.(3 marks)

"""
s1=float(input("BASE:"))
s2=float(input("HEIGHT:"))
s3=float(input("HYPOTENUSE:"))
if s3**2==(s1**2)+(s2**2):
	print("RIGHT ANGLED TRIANGLE!")
else:
	print("NOT A RIGHT ANGLED TRIANGLE!")