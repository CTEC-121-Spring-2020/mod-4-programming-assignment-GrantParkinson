# Module 5
#   Programming Assignment 6
#       Prob-5.py

# <Grant Parkinson>

from graphics import *


def main():
    win = GraphWin("Car", 300, 300)
    wheel1 = Circle(Point(50, 250), 20)
    wheel2 = Circle(Point(200, 250), 20)
    line1 = Line(Point(30, 230), Point(220, 230))
    line2 = Line(Point(30, 230), Point(30, 210))
    line3 = Line(Point(30, 210), Point(50, 210))
    line4 = Line(Point(50, 210), Point(50, 170))
    line5 = Line(Point(50, 170), Point(220, 170))
    line6 = Line(Point(220, 170), Point(220, 230))
    line7 = Line(Point(220, 230), Point(230, 230))
    line8 = Line(Point(230, 230), Point(230, 220))
    line9 = Line(Point(230, 220), Point(220, 220))
    window1 = Rectangle(Point(60, 200), Point(80, 180))
    window2 = Rectangle(Point(100, 200), Point(120, 180))
    window3 = Rectangle(Point(140, 200), Point(160, 180))
    window4 = Rectangle(Point(180, 200), Point(200, 180))
    stopSign = Polygon(Point(70, 220), Point(80, 220), Point(
        83, 215), Point(80, 210), Point(70, 210), Point(67, 215))

    stopSign.setFill("red")
    stopSign.setOutline("black")
    wheel1.setFill("black")
    wheel2.setFill("black")

    wheel1.draw(win)
    wheel2.draw(win)
    line1.draw(win)
    line2.draw(win)
    line3.draw(win)
    line4.draw(win)
    line5.draw(win)
    line6.draw(win)
    line7.draw(win)
    line8.draw(win)
    line9.draw(win)
    window1.draw(win)
    window2.draw(win)
    window3.draw(win)
    window4.draw(win)
    stopSign.draw(win)
    win.getMouse()


main()
