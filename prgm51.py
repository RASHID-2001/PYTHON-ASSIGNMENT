"""
UNIVERSITY QUESTION :MAY 2022

Write a Python program to implement Caesar cipher encryption and decryption
on a string of lowercase letters. Take distance value and the string as input. (Hint:
Caesar cipher encryption strategy replaces each character in the plaintext with the
character that occurs a given distance away in the sequence.

"""
text = input("Enter a string (lowercase letters only): ")
shift = int(input("Enter shift distance: "))
mode = input("Enter mode (encrypt/decrypt): ")

if mode == 'decrypt':
    shift = -shift  

result = ""
for char in text:
    if char.islower():  
        new_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        result += new_char
    else:
        result += char  

print("Result:", result)

