import turtle

t = turtle.Turtle()
t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

colours = ['red','orange','yellow','green','blue','violet']

t.up()
t.setpos(-200, 50)
t.down()
t.forward(100)
t.left(90)
t.forward(30)
t.left(90)
t.forward(60)
t.right(90)
t.forward(60)
t.right(90)
t.forward(60)
t.left(90)
t.forward(30)
t.left(90)
t.forward(60)
t.right(90)
t.forward(60)
t.right(90)
t.forward(60)
t.left(90)
t.forward(30)
t.left(90)
t.forward(100)
t.left(90)
t.forward(210)
t.up()

t.setpos(150,50)
t.left(90)
t.pensize(6)
t.color("green", "green")

# initiate the masterpiece

t.up()
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.down()
t.right(130)
t.forward(50)
t.right(40)
t.forward(50)
t.right(40)
t.forward(70)
t.right(30)
t.forward(220)
t.left(20)
t.forward(100)
t.left(20)
t.forward(60)
t.left(40)
t.forward(60)
t.left(40)
t.forward(30)

# pen up; move to draw the left of letter

t.up()
t.left(120)
t.forward(380)

#

t.down()
t.right(180)
t.forward(60)
t.right(180)
t.forward(30)
t.right(140)
t.forward(270)
t.right(40)
t.forward(30)
t.right(180)
t.forward(60)

# the masterpiece is finished

t.up()
