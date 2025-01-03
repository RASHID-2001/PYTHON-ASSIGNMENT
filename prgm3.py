#GREATEST OF THREE NUMBERS:
x=float(input('ENTER THE NUMBER1: '))
y=float(input('ENTER THE NUMBER2: '))
z=float(input("ENTER THE NUMBER3:"))
if x>y	and y>z:
	print(x,' IS GREATER ')	
elif y>x and x>z:
	print(y,"IS GREATER " )
else:
	print(z,"IS GREATER " )
