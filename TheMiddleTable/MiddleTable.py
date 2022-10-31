import turtle
import random

def TutInit(orig=None):
    if orig == None:
        tut = turtle.Turtle()
    else:
        tut = orig.clone()
    tut.speed(0)
    tut.ht()
    tut.color("green")
    return tut

turtles = [TutInit()]
turtles[0].lt(90)

def Stick(tut):
    tut.fd(30)
    new = TutInit(tut)
    new.rt(15)
    tut.lt(15)
    return [new]

def LeftBranchingStick(tut):
    Return = []
    for i in range(2):
        tut.fd(10)
        Return.append(TutInit(tut))
        Return[-1].lt(15)
    tut.fd(10)
    return Return

def RightBranchingStick(tut):
    Return = []
    for i in range(2):
        tut.fd(10)
        Return.append(TutInit(tut))
        Return[-1].rt(15)
    tut.fd(10)
    return Return


for i in range(5):
    newTurtles = []
    for tut in turtles:
        shapeFunk = random.choice([Stick, RightBranchingStick, LeftBranchingStick])
        newTurtles += shapeFunk(tut)
    turtles += newTurtles
input()
