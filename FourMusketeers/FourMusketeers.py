import turtle
import os
##### Config #####
groupname="YourGroupName"
turtle.speed(0) # 0-10, 0 fastest, 10 slowest. Save precious time only running slow if you need to.
turtle.colormode(255) # allows you to use (r, g, b) tuples as colors, with values 0-255
turtle.bgcolor("black")




#### Code ####
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

turtle.penup()
turtle.goto(-350, 0)
turtle.right(180)
turtle.pendown()
i = 0
for item in range (179):
    turtle.color(colors[i])
    turtle.forward(100)
    turtle.left(179)

turtle.penup()
turtle.right(180)
turtle.pendown()
i += 1
for item in range (179):
    turtle.color(colors[i])
    turtle.forward(100)
    turtle.left(179)

turtle.penup()
turtle.right(180)
turtle.pendown()
i += 1
for item in range (179):
    turtle.color(colors[i])
    turtle.forward(100)
    turtle.left(179)

turtle.penup()
turtle.right(180)
turtle.pendown()
i += 1
for item in range (179):
    turtle.color(colors[i])
    turtle.forward(100)
    turtle.left(179)

turtle.penup()
turtle.left(180)
turtle.pendown()
i += 1
for item in range (179):
    turtle.color(colors[i])
    turtle.forward(100)
    turtle.left(179)

turtle.penup()
turtle.right(180)
turtle.pendown()
i += 1
for item in range (179):
    turtle.color(colors[i])
    turtle.forward(100)
    turtle.left(179)

turtle.penup()
turtle.left(180)
turtle.pendown()
i += 1
for item in range (179):
    turtle.color(colors[i])
    turtle.forward(100)
    turtle.left(179)
########### export #########
outputpath=os.path.dirname(os.path.abspath(__file__))+os.path.sep+groupname+'.ps'
turtle.getscreen().getcanvas().postscript(file=outputpath)
turtle.done()
