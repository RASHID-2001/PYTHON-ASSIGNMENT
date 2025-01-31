"""
UNIVERSITY QUESTION:MAY 2023

Write a Python program to check whether a list contains a sublist.
Eg. Input 1: my_list = [3,4,5,2,7,8] , sub_list = [2,7]
output 1: True
input 2: my_list = [3,4,5,2,7,8] , sub_list = [5,7]
output 2: False

"""
n=int(input("ENTER THE NUMBER OF LIST CONTENT:"))
my_list = []
print("ENTER THE LIST CONTENTs:")
for i in range(n):
	l_e=input()
	my_list.append(l_e)
m=int(input("ENTER THE NUMBER OF SUB_LIST CONTENT:"))
print("ENTER THE LIST CONTENTs:")
sub_list = []

for i in range(m):
	k=input()
	sub_list.append(k)
found = False
for i in range((n-m)+1):
	temp=my_list[i:m]
	m+=1
	if temp==sub_list:
		found=True
print(found)  