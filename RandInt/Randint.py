import turtle
import os
import random
##### Config #####
groupname="Randint"
turtle.speed(0) # 0-10, 0 fastest, 10 slowest. Save precious time only running slow if you need to.
turtle.colormode(255) # allows you to use (r, g, b) tuples as colors, with values 0-255

#### Code ####
trevor = turtle.Turtle()
turtle.bgcolor("#CCFFFF")
def stem(x, y, t):
    t.penup()
    t.color("#006400")
    t.setx(x)
    t.sety(y)
    t.pendown()
    t.setheading(270)
    t.width(25)
    t.forward(250)

def petals(x, y, t):
    t.setheading(0)
    t.width(2)
    colours = ["#32CD32", "#FFC0CB", "#F0FF00", "#AC28F6", "#FF0000"]
    t.color(random.choice(colours))
    t.penup()
    t.setx(x)
    t.sety(y)
    t.pendown()
    size = 10
    while size < 60:
        trevor.circle(size)
        trevor.right(60)
        size += 1
for _ in range(25):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    stem(x, y, trevor)
    petals(x, y, trevor)

trevor.penup()
while True:
    trevor.circle(10)




########### export #########
outputpath=os.path.dirname(os.path.abspath(__file__))+os.path.sep+groupname+'.ps'
turtle.getscreen().getcanvas().postscript(file=outputpath)
turtle.done()