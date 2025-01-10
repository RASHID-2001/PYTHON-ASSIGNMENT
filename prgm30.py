"""
UNIVERSITY QUESTION :JUNE 2023(7 marks)
Write a python program to find X^Y or pow(X,Y) without using standard function 

"""
x=int(input("ENTER VALUE FOR X:"))
y=int(input("ENTER VALUE FOR Y:"))
res=1
for i in range(1,y+1):
	res=res*x
print(f" {x} ^{y} = {res}")