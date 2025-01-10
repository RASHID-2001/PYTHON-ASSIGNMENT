"""
 WRITE A PROGRAM THAT GET A NUMBER FROM THE USER AND PRINT THE CORRESPONDING BCD REPRESENTATION
EX:-
	n=541
   OUTPUT:-
	 0101 0100 0001	
"""

x = input("ENTER A NUMBER: ")
n=int(x)
print(f"BCD REPRESENTATION OF {n}:::") 
Len=len(x)
n = int(x[::-1]) 
steps=0
while steps<Len :
    digit = n % 10 
    match digit:
        case 0:
            print("0000", end=" ")
        case 1:
            print("0001", end=" ")
        case 2:
            print("0010", end=" ")
        case 3:
            print("0011", end=" ")
        case 4:
            print("0100", end=" ")
        case 5:
            print("0101", end=" ")
        case 6:
            print("0110", end=" ")
        case 7:
            print("0111", end=" ")
        case 8:
            print("1000", end=" ")
        case 9:
            print("1001", end=" ")
    n = n // 10 
    steps+=1 
