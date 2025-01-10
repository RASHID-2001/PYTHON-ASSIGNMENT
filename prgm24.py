"""
 WRITE A PROGRAM THAT GET A NUMBER FROM THE USER EXTRACT THE DIGIT OF THE OBTAINED NUMBER AND PRINT THE DIGITS IN WORDS IN REVERS ORDER
EX:-
	n=541
   OUTPUT:-
	 FIVE FOUR ONE	
"""

x = input("ENTER A NUMBER: ")

Len=len(x)
n = int(x[::-1])  
steps=0
while steps<Len :
    digit = n % 10 
    match digit:
        case 0:
            print("ZERO", end=" ")
        case 1:
            print("ONE", end=" ")
        case 2:
            print("TWO", end=" ")
        case 3:
            print("THREE", end=" ")
        case 4:
            print("FOUR", end=" ")
        case 5:
            print("FIVE", end=" ")
        case 6:
            print("SIX", end=" ")
        case 7:
            print("SEVEN", end=" ")
        case 8:
            print("EIGHT", end=" ")
        case 9:
            print("NINE", end=" ")
    n = n // 10 
    steps+=1 
