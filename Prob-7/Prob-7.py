# Module 5
#   Programming Assignment 6
#       Prob-7.py

# <Grant Parkinson>

from graphics import *


def main():
    win = GraphWin("Face", 1000, 1000)

    circle = Circle(Point(500, 500), 400)

    nose = Polygon(Point(450, 500), Point(550, 500), Point(500, 450))

    eye1 = Oval(Point(300, 300), Point(450, 400))
    eye2 = Oval(Point(700, 300), Point(550, 400))

    iris1_center = eye1.getCenter()
    iris2_center = eye2.getCenter()
    iris1 = Circle(iris1_center, 20)
    iris2 = Circle(iris2_center, 20)

    mouth = Oval(Point(300, 800), Point(700, 600))

    tooth1 = Rectangle(Point(500, 600), Point(480, 620))
    tooth2 = Rectangle(Point(500, 600), Point(520, 620))

    ear1 = Oval(Point(100, 700), Point(0, 300))
    ear2 = Oval(Point(900, 700), Point(1000, 300))

    strand1 = Line(Point(500, 100), Point(850, 150))
    strand2 = Line(Point(500, 100), Point(850, 170))
    strand3 = Line(Point(500, 100), Point(850, 140))
    strand4 = Line(Point(500, 100), Point(150, 150))
    strand5 = Line(Point(500, 100), Point(150, 170))
    strand6 = Line(Point(500, 100), Point(150, 140))

    iris1.setFill("blue")
    iris2.setFill("blue")

    mouth.setFill("red")

    tooth1.setFill("white")
    tooth2.setFill("white")

    circle.draw(win)
    nose.draw(win)
    eye1.draw(win)
    eye2.draw(win)
    iris1.draw(win)
    iris2.draw(win)
    mouth.draw(win)
    tooth1.draw(win)
    tooth2.draw(win)
    ear1.draw(win)
    ear2.draw(win)
    strand1.draw(win)
    strand2.draw(win)
    strand3.draw(win)
    strand4.draw(win)
    strand5.draw(win)
    strand6.draw(win)

    win.getMouse()


main()
