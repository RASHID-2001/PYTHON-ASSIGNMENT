"""
QN:How to draw a square and hexagon using turtle module in Python.(MAY 2024)

"""
# TO DRAW A SQUARE
import turtle

t = turtle.Turtle()


for _ in range(4):
    t.forward(100)  
    t.left(90)      

 #TO DRAW HEXAGON
t.up()
t.left(180)
t.forward(150)
t.down()
for _ in range(6):
    t.forward(100)  
    t.left(60)      
turtle.done()
