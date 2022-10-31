# 45 degree

# list of coordinates for the roads

# goto each coordinate


from turtle import *


class d2(object):

    def __init__(self, X, Y) -> None:
        self.x = X

        self.y = Y


def set_theme(canvas_width=1000, canvas_height=1000, canvas_colour=(232 / 255, 210 / 255, 210 / 255),
              pen_colour=(94 / 255, 71 / 255, 69 / 255), thickness=1, speed_value=0, tracer_value=0, hide_turtle=True,
              window_title="Demo"):
    setup(canvas_width, canvas_height)

    bgcolor(canvas_colour)

    color(pen_colour)

    pensize(thickness)

    speed(speed_value)

    tracer(tracer_value)

    if hide_turtle:
        hideturtle()

    title(titlestring=window_title)


set_theme(canvas_colour="white", thickness=5)

# Here we will hard code the coordinates into the coordinates array
coordinates = [d2(100, 100), d2(0, 0)]

for i in range(len(coordinates)):
    goto(coordinates[i].x, coordinates[i].y)

tracer(True)

exitonclick()