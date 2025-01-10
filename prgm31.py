"""
UNIVERSITY QUESTION:JUNE 2023(7 marks)
Write a python program to generate prime numbers within a certain range

"""
lower=int(input("ENTER THE LOWER LIMIT:"))
upper=int(input("ENTER THE UPPER LIMIT:"))
print(f"PRIME NUMBERS BETWEEN {lower} AND {upper}:",end=" ")
if lower==0 or lower==1:
	lower=2
for i in range(lower,upper+1):
	flag=0
	for j in range(2,(i//2)+1):
		if i%j==0:
			flag=1
	if flag==0:
		print(i,end=" ")
	