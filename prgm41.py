"""
UNIVERSITY QUESTION:JUNE 2022 (7 marks)
Write a Python program to find distance between two points (x1,y1) and (x2,y2).
"""
x1=int(input("x CO-ORDINATE OF FIRST POINT:"))
y1=int(input("y CO-ORDINATE OF FIRST POINT:"))
x2=int(input("x CO-ORDINATE OF SECOND POINT:"))
y2=int(input("y CO-ORDINATE OF SECOND POINT:"))
X=x2-x1
Y=y2-y1
print(abs((X+Y)/2))