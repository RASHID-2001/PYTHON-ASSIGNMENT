"""
UNIVERSITY QUESTION :: MAY 2023

Write a Python code segment that opens a file for input and prints the number of
four-letter words in the file.

"""
f_name=input("ENTER THE FILE NAME:")
f=open(f_name,"r")
print("FOUR LETTER WORD IN THE FILE" +f_name+":")
for line in f:
	words=line.split()
	for i in range(len(words)):
		if len(words[i])==4:
			print(words[i])
	
	