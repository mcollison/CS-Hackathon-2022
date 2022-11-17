import turtle
from db import fonts 
import os
from random import randint, choice

##### Config #####
groupname = "Group W"
turtle.speed(
  0
)  # 0-10, 0 fastest, 10 slowest. Save precious time only running slow if you need to.
turtle.colormode(
  255)  # allows you to use (r, g, b) tuples as colors, with values 0-255

s = turtle.getscreen()
t = turtle.Turtle()
names = []
with open('Group_W/polish_male_firstnames.txt') as f:
    for line in f:
        names.append(line.strip())
#names = ['Jeremy', 'Maxime', 'Simon', 'Joachim', 'Kechen', 'Ziad']

s.screensize(600,400)

def randomize_color():
  return t._colorstr((randint(0, 255), randint(0, 255), randint(0, 255)))


def write_names():
  for _ in range(1000):
    for i in names:
      s._write(txt=i,
               align='right',
               pos=(randint(-300, 300), randint(-200, 200)),
               font=(choice(fonts), randint(10, 25), 'normal'),
               pencolor=randomize_color())

write_names()

########### export #########
outputpath = os.path.dirname(
  os.path.abspath(__file__)) + os.path.sep + groupname + '.ps'
turtle.getscreen().getcanvas().postscript(file=outputpath)
turtle.done()