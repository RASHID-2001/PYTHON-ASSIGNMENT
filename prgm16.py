#COUNT OF DIGITS,VOWELS,CONSONATS AND SPEPCIAL CHARACTERS IN ASTRING
word=input("ENTER A WORD:")
n=len(word)
c_dig=0
c_vowel=0
c_con=0
c_sp=0
for i in range(n):
    if word[i].isalpha():
        if word[i] in "AEIOUaeiou":
            c_vowel=c_vowel+1
        else:
            c_con=c_con+1
    elif word[i].isdigit():
        c_dig=c_dig+1
    else:
        c_sp=c_sp+1
print(f"DIGIT COUNT ={c_dig}")
print(f"COUNT OF VOWELS={c_vowel}")
print(f"COUNT OF CONSONANTS={c_con}")
print(f"COUNT OF SPECIAL CHARACTER={c_sp}")