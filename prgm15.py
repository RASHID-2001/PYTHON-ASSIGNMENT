#FIBINOCCI SERIES
n=int(input("ENTER THE NUMBER :"))
a=0
b=1
for i in range(1,n+1):
    if i==1:
        print(0,end=" ")
    elif i==2:
        print(1,end=" ")
    else:
        c=a+b
        print(c,end=" ")
        a=b
        b=c