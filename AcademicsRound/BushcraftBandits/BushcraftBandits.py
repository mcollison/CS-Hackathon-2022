import turtle as t
import os
import time
##### Config #####
groupname="BushcraftBandits"

def drawE(x,y):
    t.penup()
    t.setpos(x,y) #centering in the screen
    t.pendown()
    t.forward(100)
    t.backward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.backward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.setheading(0)
    
def drawX(x,y):
    t.penup()
    t.goto(x,y) #centering in the screen
    t.pendown()
    t.right(50)
    t.forward(155)
    t.penup()
    
    t.goto(x+80,y)
    t.right(70)
    t.pendown()
    t.forward(150)
    t.setheading(0)
    
def drawT(x,y):
    t.penup()
    t.goto(x,y) #centering in the screen
    t.pendown()
    t.forward(100)
    t.goto(20,50)
    t.right(90)
    t.forward(100)
    t.setheading(0)
    
def drawR(x,y):
    t.penup()
    t.goto(-30,50) #centering in the screen
    t.pendown(x,y)
    t.right(90)
    t.forward(150)
    t.goto(-30,50)
    t.right(-90)
    t.circle(-50,180,100)
    t.penup()
    t.goto(0,-40)
    t.left(135)
    t.pendown()
    t.forward(70)
    t.setheading(0)

def coolSpiral():
    for n in range(50):
        t.circle(20)
        t.lt(20)

def stampCircle(x,y,rad):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(rad)
    

if __name__ == "__main__":
    t.bgcolor("springgreen") #00C896
    t.speed(100)
    t.pensize(10)
    t.pencolor("blue")
    drawE(-200,100)
    drawX(-100,50)
    drawE(0,100)
    #drawT(100,100)
    #drawE(200,100)
    #drawR(300,100)
    
    t.fillcolor("blue")
    
    #stampCircle(-200,-100, 50)
    
    ########### export #########
    outputpath=os.path.dirname(os.path.abspath(__file__))+os.path.sep+groupname+'.ps'
    t.getscreen().getcanvas().postscript(file=outputpath)
    t.done()