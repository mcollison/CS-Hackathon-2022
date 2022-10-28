import turtle
import os
import random
##### Config #####
groupname="YourGroupName"
turtle.speed(0) # 0-10, 0 fastest, 10 slowest. Save precious time only running slow if you need to.
turtle.colormode(255) # allows you to use (r, g, b) tuples as colors, with values 0-255





#### Code ####
turtle.speed(2000)
def polygon(n):
    for i in range(n):
        turtle.forward((1000/n)+3)
        turtle.left(360/n)


def DrawTube():
    n=50
    for x in range(1,18,2):
        turtle.penup()
        turtle.goto(x*10,(x*10)-100)
        turtle.pendown()
        turtle.color("green", "green")
        turtle.begin_fill()
        polygon(n)
        turtle.end_fill()

        x+=1
        turtle.penup()
        turtle.goto(x * 10, (x * 10) - 100)
        turtle.pendown()
        turtle.color("white", "white")
        turtle.begin_fill()
        polygon(n)
        turtle.end_fill()
        n-=5

DrawTube()



########### export #########
outputpath=os.path.dirname(os.path.abspath(__file__))+os.path.sep+groupname+'.ps'
turtle.getscreen().getcanvas().postscript(file=outputpath)
turtle.done()