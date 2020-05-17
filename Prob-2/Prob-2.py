# Module 5
#   Programming Assignment 6
#       Prob-2.py

# <Grant Parkinson>

from graphics import *


def main():
    win = GraphWin(title="Square clones", width=400, height=400)
    # Creates rectangle and tells shape what its color is
    shape = Rectangle(Point(50, 50), Point(100, 100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(5):
        # gets location of mouse click and subtracts 50 and 100 (coord values of upper left corner) from the x and y values of the mouse click
        llc = win.getMouse()
        dx = llc.getX() - 50
        dy = llc.getY() - 100
        # Creates a cloned object of shape named shape2 and draws that object and moves it to the coords provided by mouse click
        shape2 = shape.clone()
        shape2.draw(win)
        shape2.move(dx, dy)
    # Creates quit message and formats message
    message = Text(Point(200, 200), "Click again to quit")
    message.setSize(34)
    message.setStyle("bold")
    message.draw(win)
    win.getMouse()
    win.close()


main()
