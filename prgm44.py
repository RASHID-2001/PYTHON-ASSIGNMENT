"""
UNIVERSITY QUESTION:MAY 2023 (7 marks)
Write a Python program to display the sum of odd numbers between a
programmer specified upper and lower limit.
"""
lower=int(input("ENTER THE LOWER LIMIT:"))
upper=int(input("ENTER THE UPPPER LIMIT:"))
print(f"SUMOFODD NUMBERS BETWEEN {lower} AND {upper}",end=":")
sum=0
if lower%2==0:
	lower=lower+1
for i in range(lower,upper+1,2):
	sum+=i
print(sum)

