#FACTORIAL OF A NUMBER
n=int(input("ENTER THE NUMBER:"))
if n==0:
    print("0! = 1")
else:
    res=1
    for i in range(1,n+1):
        res=res*i
    print(f"{n} ! ={res}")