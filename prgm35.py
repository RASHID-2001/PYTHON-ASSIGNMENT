"""
UNIVERSITRY QUESTION:JANUARY 2024(6 marks)
Write a Python program to print all numbers between 100 and 1000 whose sum
of digits is divisible by 9.

"""
for i in range(100,1001):
	n=i
	sum=0
	while n>0:
		digit=n%10
		sum+=digit
		n=n//10
	if sum%9==0:
		print(i)