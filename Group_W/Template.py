import turtle
import os
from random import randint

##### Config #####
groupname="Group W"
turtle.speed(0) # 0-10, 0 fastest, 10 slowest. Save precious time only running slow if you need to.
turtle.colormode(255) # allows you to use (r, g, b) tuples as colors, with values 0-255

s = turtle.getscreen()
t = turtle.Turtle()
names = ['Jeremy', 'Maxime', 'Simon', 'Joachim', 'Kechen', 'Ziad']

def randomize_color():
  return t._colorstr((randint(0,255),randint(0,255),randint(0,255)))

def write_names():
  for _ in range(5000):
    for i in names:
      s._write(txt = i, align = 'right',pos = (randint(-800,800),randint(-800,800)),font = ('Verdana', randint(10,30), 'normal'), pencolor = randomize_color())



write_names()




  
  

  



########### export #########
outputpath=os.path.dirname(os.path.abspath(__file__))+os.path.sep+groupname+'.ps'
turtle.getscreen().getcanvas().postscript(file=outputpath)
turtle.done()