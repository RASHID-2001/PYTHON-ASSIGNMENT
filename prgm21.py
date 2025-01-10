"""
PYTHON PROGRAM TO  PRINT THEN GIVEN PATTERN:-    
  n=5
              0
            1 0 1
          2 1 0 1 2 
 	3 2 1 0 1 2 3   
      4 3 2 1 0 1 2 3 4  
    5 4 3 2 1 0 1 2 3 4 5
"""

n = int(input("ENTER THE NUMBER OF ROWS: "))
print()
print()
for i in range(n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for j in range(i, -1, -1):
        print(j, end=" ")
    for j in range(1, i+1):
        print(j, end=" ")
    print()
