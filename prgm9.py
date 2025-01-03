#CHECKING A NUMBER IS PRIME OR NOT
n=int(input("ENTER A NUMBER:"))
flag=False
for i in range(2,(n//2)+1):
        if n%i==0:
            flag=True
            break
if flag:
    print(f"{n} IS NOT  A PRIME!")
else:
    print(f"{n} IS A PRIME!")