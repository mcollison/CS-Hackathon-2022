import turtle
import os

import numpy as np
import cv2
##### Config #####
groupname="TeamBackRow"
turtle.speed(0) # 0-10, 0 fastest, 10 slowest. Save precious time only running slow if you need to.
turtle.colormode(255) # allows you to use (r, g, b) tuples as colors, with values 0-255

PICTURE_DIRECTORY = str(input("Enter the Directory for an image: "))

#### Code ####

img = cv2.imread(PICTURE_DIRECTORY, 2)

t = turtle.Turtle()

START_COORDS = (-1/2 * img.shape[0], 1/2 * img.shape[1])
t.penup()
t.goto(START_COORDS)

print(img.shape[0], img.shape[1])
print(img[0][0], img[0][1], img[0][2])

delay=input()
for i in range(img.shape[0]):
    t.penup()
    t.goto(START_COORDS[0],START_COORDS[1] - i)
    t.pendown()
    rgb_s = "#"
    for j in range(img.shape[1]):
        val = img[i][j]
        rgb_s += hex(val)[2:]

        if len(rgb_s) == 7:
            print(rgb_s, "X =", j, "Y =", i)
            t.color(rgb_s)
            t.forward(1.5)
            rgb_s = "#"

########### export #########
outputpath=os.path.dirname(os.path.abspath(__file__))+os.path.sep+groupname+'.ps'
turtle.getscreen().getcanvas().postscript(file=outputpath)
turtle.done() 