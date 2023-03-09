import os
import turtle

class Pattern:
    def __init__(self, angleNo, timesNo):
        self.__angle = angleNo
        self.__times = timesNo

    def drawPattern(self):
        colours = ['red', 'yellow', 'green', 'blue', 'purple', 'pink']
        turtle.setup(800, 600)
        turtle.bgcolor('black')
        for x in range(self.__times):
            turtle.pencolor(colours[x % 6])
            y = (x/100) + 1
            turtle.width(y)
            turtle.forward(x)
            turtle.left(self.__angle)
        turtle.done()


patternList = []

try:
    f = open("angle.txt", "r")
    while True:
        angle = f.readline().strip()
        if angle == "":
            break
        NoTimes = f.readline().strip()
        patternList.append(Pattern(int(angle), int(NoTimes)))
    f.close()
except OSError:
    print("Sorry file not found. Current directory is",os.getcwdb())

patternList[3].drawPattern()
