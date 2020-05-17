# Module 5
#   Programming Assignment 6
#       Prob-1.py

# <Grant Parkinson>

# INSTRUCTIONS:
#   Insert a comment above each line of code in the program below to describe
#   what the code does

# imports entirity of graphics librearyt
from graphics import *


def main():
    # Makes window
    win = GraphWin()
    # Makes a circle with a center point of (50,50) and a radius of 20
    shape = Circle(Point(50, 50), 20)
    # Sets circle outline to red
    shape.setOutline("red")
    # Sets inside of the circle to be filled with red
    shape.setFill("red")
    # Draws the circle in the window
    shape.draw(win)
    # Creates a for loop that will execute 5 time
    for i in range(5):
        # sets coordinates of mouse click to p
        p = win.getMouse()
        # sets center of circle to c
        c = shape.getCenter()
        # subtracts new mouse click x coordinate from x coordinate of old circle center
        dx = p.getX() - c.getX()
        # subtracts new mouse click y coordinate from y coordinate of old circle center
        dy = p.getY() - c.getY()
        # moves center of circle to newly calculated coordinates
        shape.move(dx, dy)
    # closes window after for loop runs 5 times
    win.close()


main()
