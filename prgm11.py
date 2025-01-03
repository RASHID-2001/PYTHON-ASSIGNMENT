#PALINDROME CHECKER:
word=input("ENTER A WORD:")
leng=len(word)
flag=True
n=leng-1
for i in range(leng//2):
    if word[i]!=word[n]:
        flag=False
        break
    n=n-1
if flag:
    print(word," IS A PALINDROME!!!")
else:
    print(word," IS NOT PALINDROME!!!")