"""
UNIVERSITY QUESTION::JUNE 2022
Write a Python program to read n integers into a list and separate the positive
and negative numbers into two different lists.?

"""
n=int(input("ENTER THE NUMBER OF ELEMENTS IN LIST:"))
l=[]
for i in range(n):
	k=int(input(f"ENTER THE {i}th ELEMENT:"))
	l.append(k)
print(l)
l_n=[]
l_p=[]
for i in range(n):
	if l[i]<0:
		l_n.append(l[i])
	else:
		l_p.append(l[i])
print("NEGETIVE NUMBERS:"l_n)
print("POSITIVE NUMBERS:"l_p)