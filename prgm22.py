"""
ENTER A PROGRAM TO GET A NUMBER FROM THE USER AND GIVE THE NAME OF THE CORRESPONDING MONTH NUMBER OF DAYS IN THAT MONTH
EX: 
	INPUT:-
		n=5
	OUTPUT:-
		MAY 31 DAYS
	
"""
n=int(input("ENTER A  NUMBER:"))
match n:
	case 1:print("JANUARY 31 DAYS")
	case 2:print("FEBRUARY 28/29 DAYS") 
	case 3:print("MARCH 31 DAYS")
	case 4:print("APRIL 30 DAYS")
	case 5:print("MAY 31 DAYS")
	case 6:print("JUNE 30 DAYS")
	case 7:print("JULY 31 DAYS")
	case 8:print("AUGUST 31 DAYS")
	case 9:print("SEPTEMBER 30 DAYS")
	case 10:print("OCTOBER 31 DAYS")
	case 11:print("NOVEMBER 30 DAYS")
	case 12:print("DECEMBER 31 DAYS")
	case invalid:print("ENTER A NUMBER IN BETWEEN 1-12")