"""
QUESTION	WRITE A PROGRAM TO PERFORM A QUIZ WITH MULTIPLE CHOICE,PRINT THE RULES OF QUIZ AND PRINT THE TOTAL MARK OF THE USER
"""
print("--------------------------------------------------------------------------------------------------------------------------------------------")
print("\t\tWELCOME TO QUIZE TIME!\nRULES:-\n1>TOTAL 10 QUESTIONS EACH CARRIES 5 MARKS\n2>-2 MARKS FOR A WRONG ANSWER\n3>ANY CHOICE OTHER THAN <a,b,c,d> IS CONSIDERED AS WRONG ANSWER\n4>ENTER * TO LEAVE A QUESTION")
print("--------------------------------------------------------------------------------------------------------------------------------------------")
a=[0]*10
print("\nQUESTION:-")
print("\n\n1-Who is the founder of PYTHON ?\n(A) James Gosling\t(B) uido van Rossum\n(C) Dennis Ritchie\t(D) Yukihiro Matsumoto")
a[0]=input("\nANSWER:")
print("\n--------------------------------------------------------------------------------------------------------------------------------------------\n")
print('\n\n2-What is the output of the following code?\n\n>>>x = "Hello"\n>>>y = "World"\n>>>print(x + y)')
print("\n(A) Hello World\t(B) Hello\n(C) world\t(D) HelloWorld")
a[1]=input("\nANSWER:")
print("\n--------------------------------------------------------------------------------------------------------------------------------------------\n")
print("\n\n3-Which of the following is used to define a block of code in Python?\n(A) ()\t(B)  {}\n(C) []\t(D) Indentation")
a[2]=input("\nANSWER:")
print("\n--------------------------------------------------------------------------------------------------------------------------------------------\n")
print("\n\n4-What is the result of the following operation in Python?\n >>> 3**2\n(A) 5\t(B) 6\n(C) 9\t(D) 8")
a[3]=input("\nANSWER:")
print("\n--------------------------------------------------------------------------------------------------------------------------------------------\n")
print("\n\n5- What is the correct file extension for Python files?\n(A) .pyth\t(B) .pt\n(C) .py\t(D) .python")
a[4]=input("\nANSWER:")
print("\n--------------------------------------------------------------------------------------------------------------------------------------------\n")
print("\n\n6- How do you insert comments in Python?\n(A) //\t(B) /* */\n(C) #\t(D) --")
a[5]=input("\nANSWER:")
print("\n--------------------------------------------------------------------------------------------------------------------------------------------\n")
print('\n\n7-What will be the output of the following code?\n\n>>>x="PYTHON"\n>>>print(x[0])\nA) P\t(B) Python\n(C) n\t(D) IndexError')
a[6]=input("\nANSWER:")
print("\n--------------------------------------------------------------------------------------------------------------------------------------------\n")
print("\n\n8- Which operator is used for floor division in Python?\n(A) /\t(B) //\n(C) %\t(D) **")
a[7]=input("\nANSWER:")
print("\n--------------------------------------------------------------------------------------------------------------------------------------------\n")
print("\n\n9-What will the following code output?\n>>>for i in range(1,10,2)\n>>>\tprint(i)")
print("\n(A) 0 1 2 3 4 5 6 7 8 9 10\t(B)1 3 5 7 9\n(C) 1 2 4 6 8\t(D) 1 1 1 1 1 1 1")
a[8]=input("\nANSWER:")
print("\n--------------------------------------------------------------------------------------------------------------------------------------------\n")
print("\n\n10What is the output of the following code?>>>print(type(10))\n(A) <class 'int'>\t(B) <class 'float'>\n(C) <class 'number'>\t(D) Error")
a[9]=input("\nANSWER:")
print("\n--------------------------------------------------------------------------------------------------------------------------------------------\n")
right=0
wrong=0
attend=0
print(a)
for i in range(10):
	answer=a[i]
	match i:
		case 0:
			if answer=='B' or answer=='b':
				right+=1
			elif answer=='':
				attend=attend+1
			else:
				wrong+=1
		case 1:
			if answer=='D' or answer=='d':
				right+=1
			elif answer=='':
				attend=attend+1
			else:
				wrong+=1
		case 2:
			if answer=='D' or answer=='d':
				right+=1
			elif answer=='':
				attend=attend+1
			else:
				wrong+=1
		case 3:
			if answer=='C' or answer=='c':
				right+=1
			elif answer=='':
				attend=attend+1
			else:
				wrong+=1
		case 4:
			if answer=='C' or answer=='c':
				right+=1
			elif answer=='':
				attend=attend+1
			else:
				wrong+=1
		case 5:
			if answer=='C' or answer=='c':
				right+=1
			elif answer=='':
				attend=attend+1
			else:
				wrong+=1
		case 6:
			if answer=='A' or answer=='a':
				right+=1
			elif answer=='':
				attend=attend+1
			else:
				wrong+=1
		case 7:
			if answer=='B' or answer=='b':
				right+=1
			elif answer=='':
				attend=attend+1
			else:
				wrong+=1
		case 8:
			if answer=='B' or answer=='b':
				right+=1
			elif answer=='':
				attend=attend+1
			else:
				wrong+=1
		case 9:
			if answer=='A' or answer=='a':
				right=right+1
			elif answer=='':
				attend=attend+1
			else:
				wrong+=1
print(f"TOTAL NUMBER OF QUESTIONS ATTENDED:{10-attend}")
print(f"TOTAL NUMBER OF CORRECT ANSWERs: {right}")
print(f"TOATAL NUMBER OF WRONG ANSWERS: {wrong}")
print(f"YOUR SCORE    :{(5*right)-(2*wrong)}")
print("\n\t\t THANK YOU FOR ATTENDING😊❤️")
	