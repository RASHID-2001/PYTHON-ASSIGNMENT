#SUM OF n NATURAL NUMBERS AND THER AVERAGE
n=int(input("ENTER A NUMBER:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(f"SUM={sum}")
print(f"AVERAGE={sum/n}")