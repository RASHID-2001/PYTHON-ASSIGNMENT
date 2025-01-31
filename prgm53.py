"""
UNIVERSITY QUESTION:JUNE 2023
Assume that there is a text file named “numbers.txt”. Write a python program to find the median of list of numbers in the file without using standard function for median.

"""
f = open("numbers.txt", "r")  
lis = []
for line in f:
    	lis.extend(map(int, line.split()))  

f.close() 

lis.sort()  

n = len(lis)
if n % 2 == 1:
	md_ind = n // 2  
    	print("Median:", lis[md_ind])
else:
    	md_ind = n // 2
    	print("Median:", (lis[md_ind] + lis[md_ind - 1]) / 2)

