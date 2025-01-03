#FREQUENCY  OF A CHARACTOR IN GIVEN STRING
s=input("ENTER THE STRING:")
c=input("ENTER THE CHARACTOR:")
if c in s:
	n=len(s)
	count=0
	for i in range(n):
		if s[i]==c:
			count=count+1
	print(f"{c} OCCURES {count} TIMES IN THE GIVEN STRING {s}")
else:
	print(f"{c} IS NOT FOUND IN {s}")
