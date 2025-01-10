"""
UNIVERSITY QUESTION:JUNE 2023 ( 7 marks )
Write a python program to find the sum of the cosine series 1 - x^2/2! + x^4/4!-.......

"""
x=float(input("ENTER THE VALUE OF X:"))
n=int(input("ENTER THE NUMBER OF TERMS:"))
sum=1
power=2
sign=-1
for i in range(2,n+1):
	fact=1
	for j in range(1,power+1):
		fact*=j
	res=(x**power)/fact
	sum=sum+(res*sign)
	power=power+2
	sign*=-1	
print(f"SUM={sum}")