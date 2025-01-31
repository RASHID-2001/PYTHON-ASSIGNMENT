"""
UNIVERSITY QUESTION:JANUARY 2024

Write a Python program to print all palindromes in a line of text.

"""
text=input("ENTER A LINE OF TEXT:")
words=text.split()
for i in range(len(words)):
	temp=words[i]
	rev=temp[::-1]
	if temp==rev:
		print(temp)