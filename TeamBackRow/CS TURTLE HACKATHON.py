import turtle
import os

import numpy as np
import cv2
##### Config #####
groupname="TeamBackRow"
turtle.speed(0) # 0-10, 0 fastest, 10 slowest. Save precious time only running slow if you need to.
turtle.colormode(255) # allows you to use (r, g, b) tuples as colors, with values 0-255

# DIRECTORY = "/".join(__FILE__.split("/")[:-1])
# PICTURE_DIRECTORY=DIRECTORY + "/FORUM_SMALL.JPEG"

#### Code ####

img = cv2.imread("TeamBackRow\FORUM_SMALL.JPEG", 2)
img = img.tolist()

t = turtle.Turtle()
for i in range(img):
    t.goto(0,i)
    for j in range(img[i]):
        rgb = img[i][j]
        rgb_s = "#" + str(hex(rgb[0])[2:]) + str(hex(rgb[1])[2:]) + str(hex(rgb[2])[2:])
        
        t.pencolor(rgb_s)
        t.forward(1)



########### export #########
outputpath=os.path.dirname(os.path.abspath(__file__))+os.path.sep+groupname+'.ps'
turtle.getscreen().getcanvas().postscript(file=outputpath)
turtle.done()


##### OUR CONFESSION (AMBITIONS) ##############
"""
Unfinished Code, do not run

We wanted to recreate a picture of our lovely university with the turtle.
Alas, we failed, but had a good time trying.

Method for this, was to rip the pixel data form an existing image, and recreate with turtle pixel by pixel.

################################################
"""