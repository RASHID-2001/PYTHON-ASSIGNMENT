"""
UNIVERSITY QUESTION :: JUNE 2022

Write Python code for the following statements
i)write the text "PROGRAMMING IN PYTHON"in to a file of name code.txt
ii) then reads the text again and prints it to the screen.

"""
f=open("code.txt","w")
f.write("PROGRAMMING IN PYTHON")
f=open("code.txt","r")
content=f.read()
print("CONTENT OF THE FILE:",content)
