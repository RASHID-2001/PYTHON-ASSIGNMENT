"""
UNIVERSITY QUESTION:MAY 2023 (7 marks)
e^x=1+x+(x^2)/2!+(x^3)/3!.....................
Given the value of x, write a Python program to evaluate the following series upto
n terms:
"""
print("e^x=1+x+(x^2)/2!+(x^3)/3!.....................")
x=int(input("ENTER THE VALUES FOR x:"))
n=int(input("ENTER THE NUMBER OF TERMS:"))
sum=1+x
for i in range(2,n):
	fact=1
	for j in range(1,i+1):
		fact*=j
	sum+=(x**i)/fact
print(f"RESULT = {sum}")
