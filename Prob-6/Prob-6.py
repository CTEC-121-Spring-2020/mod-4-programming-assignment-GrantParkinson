# Module 5
#   Programming Assignment 6
#       Prob-6.py

# <YOUR NAME>

from graphics import *


def main():
    win = GraphWin("Legos", 1100, 1000)

    blue_brick = Rectangle(Point(10, 280), Point(510, 100))
    blue_brick.setFill("blue")
    blue_brick.setOutline("black")
    blue_brick.setWidth(5)
    blue_brick.draw(win)

    blueBrickNib = Rectangle(Point(35, 100), Point(85, 80))
    blueBrickNib.setFill("blue")
    blueBrickNib.setOutline("black")
    blueBrickNib.setWidth(5)
    blueBrickNib.draw(win)

    for i in range(1, 5):
        blueBrickNextNib = blueBrickNib.clone()
        blueBrickNextNib.move(100 * i, 0)
        blueBrickNextNib.draw(win)

    green_brick = blue_brick.clone()
    green_brick.setFill("green")
    green_brick.move(550, 0)
    green_brick.draw(win)

    greenBrickNib = Rectangle(Point(580, 100), Point(630, 80))
    greenBrickNib.setFill("green")
    greenBrickNib.setOutline("black")
    greenBrickNib.setWidth(5)
    greenBrickNib.draw(win)

    for i in range(1, 5):
        greenBrickNextNib = greenBrickNib.clone()
        greenBrickNextNib.move(100 * i, 0)
        greenBrickNextNib.draw(win)

    yellow_brick = blue_brick.clone()
    yellow_brick.setFill("yellow")
    yellow_brick.move(0, 300)
    yellow_brick.draw(win)

    yellowBrickNib = Rectangle(Point(30, 400), Point(80, 380))
    yellowBrickNib.setFill("yellow")
    yellowBrickNib.setOutline("black")
    yellowBrickNib.setWidth(5)
    yellowBrickNib.draw(win)

    for i in range(1, 5):
        yellowBrickNextNib = yellowBrickNib.clone()
        yellowBrickNextNib.move(100 * i, 0)
        yellowBrickNextNib.draw(win)

    red_brick = blue_brick.clone()
    red_brick.setFill("red")
    red_brick.move(550, 300)
    red_brick.draw(win)

    redBrickNib = Rectangle(Point(585, 400), Point(635, 380))
    redBrickNib.setFill("red")
    redBrickNib.setOutline("black")
    redBrickNib.setWidth(5)
    redBrickNib.draw(win)

    for i in range(1, 5):
        redBrickNextNib = redBrickNib.clone()
        redBrickNextNib.move(100 * i, 0)
        redBrickNextNib.draw(win)

    teal_brick = blue_brick.clone()
    teal_brick.setFill("teal")
    teal_brick.move(0, 600)
    teal_brick.draw(win)

    tealBrickNib = Rectangle(Point(30, 700), Point(80, 680))
    tealBrickNib.setFill("teal")
    tealBrickNib.setOutline("black")
    tealBrickNib.setWidth(5)
    tealBrickNib.draw(win)

    for i in range(1, 5):
        tealBrickNextNib = tealBrickNib.clone()
        tealBrickNextNib.move(100 * i, 0)
        tealBrickNextNib.draw(win)

    black_brick = blue_brick.clone()
    black_brick.setFill("black")
    black_brick.setOutline("red")
    black_brick.setWidth(1)
    black_brick.move(550, 600)
    black_brick.draw(win)

    blackBrickNib = Rectangle(Point(585, 700), Point(635, 680))
    blackBrickNib.setFill("black")
    blackBrickNib.setOutline("red")
    blackBrickNib.setWidth(1)
    blackBrickNib.draw(win)

    for i in range(1, 5):
        blackBrickNextNib = blackBrickNib.clone()
        blackBrickNextNib.move(100 * i, 0)
        blackBrickNextNib.draw(win)

    win.getMouse()


main()
