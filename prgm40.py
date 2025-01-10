"""
UNIVERSITY QUESTION:JUNE 2022 (7 marks)
Write the python program to print all prime numbers less than 1000.
"""
print("PRIME NUMBERS BELOW 1000:")
for i in range(2,1000):
	flag=0
	for j in range(2,((i+1)//2)):
		if i%j==0:
			flag=1
	if flag==0:
		print(i)
	