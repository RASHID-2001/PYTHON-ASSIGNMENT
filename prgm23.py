"""
ENTER A PROGRAM THAT CONVERTION
	1: CELSIUS to FAHRENHEIT
	2: KILOMETERS to MILES
	3: KILOGRAMS to POUNDS
	USER HAVE TO CHOOSE THE CONVERSION,THUS GET THE VALUE AND DO THE REQUIRED CONVERSION
"""

print("MENU:-\n1-CELSIUS to FAHRENHEIT\n2-KILOMETERS to MILES\n3-KILOGRAMS to POUNDS")
n=int(input("ENTER THE YOUR CHOICE:"))
match n:
	case 1:
		c=float(input("ENTER THE VALUE IN CELSIUS:"))
		print(f" {c} CELSIUS = {c*(9/5)+32} FAHRENHEIT")
	case 2:
		c=float(input("ENTER THE VALUE IN KILOMETERS:"))
		print(f" {c} KILOMETERS = {c*0.621371} MILES")
	case 3:
		c=float(input("ENTER THE VALUE IN KILOGRAMS:"))
		print(f" {c} KILOGRAMS = {c*2.20462} POUNDS")
	case _:print("ENTER A VALID CHOICE!")

