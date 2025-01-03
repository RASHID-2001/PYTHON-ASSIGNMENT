#CHECKING CHARACTER IS UPPERCASE OR LOWERCASE
char=input("ENTER A CHARACTER:")
if char.isalpha():
    if char.isupper():
        print(char," IS IN UPPERCASE!")
    else:
        print(char," IS IN LOWERCASE!")
else:
    print(char," IS NOT A ALPHABET!")