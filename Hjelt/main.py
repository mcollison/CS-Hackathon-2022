import turtle
import os
from PIL import Image
##### Config #####
groupname="Hjelt"
turtle.speed(0) # 0-10, 0 fastest, 10 slowest. Save precious time only running slow if you need to.
turtle.colormode(255) # allows you to use (r, g, b) tuples as colors, with values 0-255
turtle.hideturtle()

#### Code ####
filepath = "./napoleon.jpeg"
img = Image.open(filepath)
resolution = (img.size[0],img.size[1])
out_resolution = (118,161)
turtle.screensize(out_resolution[0], out_resolution[1])
turtle.penup()
turtle.goto(out_resolution[0]//2,out_resolution[1]//2)
turtle.pendown()

pixels = img.load()

yy = resolution[1]//out_resolution[1]
xx = (resolution[0]-1)//out_resolution[0]
# cue horrible variable names
for y in range(out_resolution[1]):
    for x in range(out_resolution[0]):
        (r,g,b) = ([],[],[])
        for y_ in range(yy):
            for x_ in range(xx):
                (r_, g_, b_) = pixels.__getitem__((xx*x+x_,yy*y+y_))
                r.append(r_)
                g.append(g_)
                b.append(b_)
        colour = (round(sum(r)/len(r)),round(sum(g)/len(g)),round(sum(b)/len(b)))
        turtle.color(colour)
        turtle.forward(1) # draw pixel
    # typewriter
    turtle.penup()
    turtle.backward(out_resolution[0])
    turtle.right(90)
    turtle.forward(1)
    turtle.left(90)
    turtle.pendown()



########### export #########
outputpath=os.path.dirname(os.path.abspath(__file__))+os.path.sep+groupname+'.ps'
turtle.getscreen().getcanvas().postscript(file=outputpath)
turtle.done()