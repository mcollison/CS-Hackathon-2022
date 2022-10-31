import turtle
import os
import math
##### Config #####
groupname="M1 mac"

turtle.speed(0) # 0-10, 0 fastest, 10 slowest. Save precious time only running slow if you need to.
turtle.colormode(255) # allows you to use (r, g, b) tuples as colors, with values 0-255

#### Code ####
name = list("university of exeter ")
radius_name = 170

turtle.penup()
turtle.pencolor((0, 255, 20))
turtle.goto(x=0, y=-100)

turtle.pendown()
turtle.circle(200)
turtle.penup()

turtle.goto(x=0, y=-50)
turtle.pendown()
turtle.circle(150)

turtle.degrees()

turtle.pencolor("black")

for i in range(len(name)):
    turtle.penup()
    angle = 360//len(name) * i
    print(angle)
    turtle.settiltangle(angle)
    turtle.goto(x=radius_name * math.sin(math.radians(angle)), y=(radius_name*math.cos(math.radians(angle))+95))
    turtle.pendown()
    turtle.write(name[i])

turtle.penup()
turtle.goto(x=0, y=0)
# outside circle green



########### export #########
outputpath=os.path.dirname(os.path.abspath(__file__))+os.path.sep+groupname+'.ps'
turtle.getscreen().getcanvas().postscript(file=outputpath)
turtle.done()
