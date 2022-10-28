import cv2
import turtle
import os
##### Config #####
groupname="erhjje"
turtle.speed(0) # 0-10, 0 fastest, 10 slowest. Save precious time only running slow if you need to.
turtle.colormode(255) # allows you to use (r, g, b) tuples as colors, with values 0-255

#### Code ####
# Binary Image

img = cv2.imread('bonus_image.png', 2)
ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
width = int(img.shape[1])
height = int(img.shape[0])


# Turtle Setup

my_screen = turtle.Screen()
my_screen.screensize(width, height)
my_pen = turtle.Turtle()
my_screen.tracer(0)


# Printing Loop

for i in range(int(height/2), int(height/-2),  -1):
    my_pen.penup()
    my_pen.goto(-(width / 2), i)

    for l in range(-int(width/2), int(width/2), 1):
        pix_width = int(l + (width/2))
        pix_height = int(height/2 - i)
        if bw_img[pix_height, pix_width] == 0:
            my_pen.pendown()
            my_pen.forward(1)
        else:
            my_pen.penup()
            my_pen.forward(1)
    my_screen.update()

my_pen.hideturtle()

turtle.done()




########### export #########
outputpath=os.path.dirname(os.path.abspath(__file__))+os.path.sep+groupname+'.ps'
turtle.getscreen().getcanvas().postscript(file=outputpath)
turtle.done()