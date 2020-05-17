# Module 5
#   Programming Assignment 6
#       Prob-3.py

# <Grant Parkinson>

from graphics import *


def main():
    win = GraphWin("Target", 300, 300)
    win.setCoords(0, 0, 20, 20)

    circle_white = Circle(Point(10, 10), 10)
    circle_white.setOutline("white")
    circle_white.setFill("white")
    circle_white.draw(win)

    circle_black = Circle(Point(10, 10), 8)
    circle_black.setOutline("black")
    circle_black.setFill("black")
    circle_black.draw(win)

    circle_blue = Circle(Point(10, 10), 6)
    circle_blue.setOutline("blue")
    circle_blue.setFill("blue")
    circle_blue.draw(win)

    circle_red = Circle(Point(10, 10), 4)
    circle_red.setOutline("red")
    circle_red.setFill("red")
    circle_red.draw(win)

    circle_yellow = Circle(Point(10, 10), 2)
    circle_yellow.setOutline("yellow")
    circle_yellow.setFill("yellow")
    circle_yellow.draw(win)

    win.getMouse()
    win.close()


main()
