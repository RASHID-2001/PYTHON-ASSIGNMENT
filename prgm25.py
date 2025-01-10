"""
WRITE A PROGRAM THAT CALCULATE THE AREA AND THE PERIMETER OF  THE SHAPE CHOSEN BY THE USER
	1-RECTANGLE
	2-TRIANGLE
	3-CIRCLE
	NB:PROMT THE USER TO GIVE THE REQUIERD PARAMETERS
	
"""
print("MENU:-\n1-RECTANGLE\n2-TRIANGLE\n3-CIRCLE")
n=int(input("ENTER YOUR CHOICE:"))
match n:
	case 1:
		l=float(input("LENGTH :"))
		b=float(input("BREADTH :"))
		print(f"PERIMETER:{2*(l+b)}")
		print(f"AREA :{l*b}")
		
	case 2:
		s1=float(input("SIDE1 :"))
		s2=float(input("SIDE2 :"))
		s3=float(input("SIDE2 :"))
		s=(s1+s2+s3)
		print(f"PERIMETER:{s}")
		s=s/2
		print(f"AREA :{(s*(s-s1)*(s-s2)*(s-s3))**0.5}")
	case 3:
		r=float(input("RADIUS:"))
		pi=22/7
		print(f"CIRCUMFERENCE:{2*pi*r}")
		print(f"AREA:{pi*r*r}")
	case _:print("ENTER A VALID CHOICE!")
		
