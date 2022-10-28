from PIL import Image
from numpy import asarray
import turtle as jeff

image = Image.open("blue30.png")
data = asarray(image)
print(list(data[0][0]))

SIZE = 0.2


jeff.shape("square")
jeff.turtlesize(SIZE)
jeff.speed(0)
jeff.delay(0)
jeff.colormode(255)
line = 0

INITIAL = (-500, 300)

for x in data:
    column = 0
    line +=1
    for y in x:
        column += 1
        jeff.penup()
        jeff.goto((INITIAL[0]+column, INITIAL[1]))
        jeff.pendown()
        jeff.color(tuple(data[line][column]))
        jeff.stamp()
        
