"""
STAR PYRAMID
n=5
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
"""
n=int(input("ENTER THE NUMBER OF ROWS:"))
for i in range(n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1))
