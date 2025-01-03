"""
PROGRAM TO PRINT PATTRN OF * IN A GRID WITH n NUMBER OF COLUMNS AND ROWS
EX:
    N=3
    * * *
    * * *
    * * *
"""
n=int(input("ENTER THE NUMBER:"))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
        
