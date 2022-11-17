from exturtle import *

t = Turtle()



pendown(t)
right(t,45)
forward(t, 50)
left(t, 145)
forward(t, 100)

for i in range (0,180):
    forward(t,1)
    right(t,1)

left(t, 85)
forward(t, 50)
left(t, 100)
for i in range (0,180):
    forward(t,1)
    right(t,1)

forward(t,100)
left(t, 145)
forward(t,50)

penup(t)
left(t, 135)
forward(t, 150)
pendown(t)
left(t, 45)
forward(t, 50)
right(t, 90)
forward(t, 50)
