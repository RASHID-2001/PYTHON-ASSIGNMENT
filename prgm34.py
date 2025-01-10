"""
UNIVERSITY QUESTION:JANUARY 2024(8 marks)
->Write a Python program to print all prime factors of a given number.

"""
n=int(input("ENTER A NUMBER:"))
print(f"PRIME FACTORS OF {n}",end=":")
for i in range(2,(n//2)+1):
	flag=0
	if n%i==0:
		for j in range(2,(i//2)+1):
			if i%j==0:
				flag=1
		if flag==0:
			print(i,end=" ")