#REVERSING A GIVEN STRING:
word=input("ENTER A WORD:")
leng=len(word)
j=0
rev=[""]*leng
for i in range(leng-1,-1,-1):
    rev[i]=word[j]
    j=j+1
print("REVERSED STRING:",end="")
for i in range(leng):
    print(rev[i],end="")

