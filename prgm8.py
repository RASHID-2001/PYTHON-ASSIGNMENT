#POWER OF A GIVEN NUMBER:
n=int(input("ENTER BASE VALUE:"))
e=int(input("ENTER POWER VALUE:"))
res=1
if e==0:
    print(f"{n}^0 = 1")
else:
    res=1
    for j in range(1,e+1):
        res=res*n
    print(f"{n}^{e} = {res}")