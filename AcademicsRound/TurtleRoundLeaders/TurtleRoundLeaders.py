import turtle
from random import randint
import os
##### Config #####
groupname="AcademicLeaders"
turtle.speed(0) # 0-10, 0 fastest, 10 slowest. Save precious time only running slow if you need to.
# turtle.tracer(0,0) # only updates canvas when calling turtle.update(). Makes generation MUCH faster. Won't see turtle move though in between update calls though.
turtle.colormode(255) # allows you to use (r, g, b) tuples as colors, with values 0-255





#### Code ####

# sample creates a chess board, with black and white tiles
outputpath=os.path.dirname(os.path.abspath(__file__))+os.path.sep+groupname+'.ps'
GridSize=8
TileLength=15
TileColors=["white", (0,0,0)]

def drawline():
    for i in range(0,GridSize): # line loop
        turtle.begin_fill()
        turtle.color(TileColors[i % 2 == 0], TileColors[i % 2 != 0]) # i is even => tile color index
        for j in range(0, 4): # draw a box
            turtle.down()
            turtle.forward(TileLength)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(TileLength)
        turtle.up()
def drawgrid():
    for a in range(0,int(GridSize/2)):
        drawline()
        turtle.left(90)
        turtle.forward(2*TileLength) #position one TileLength above previous line, and turn around
        turtle.left(90)
        drawline()
        turtle.left(180) # turn around
   
drawgrid()


turtle.getscreen().getcanvas().postscript(file=outputpath)
turtle.done()