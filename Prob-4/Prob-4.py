# Module 5
#   Programming Assignment 6
#       Prob-4.py

# <Grant Parkinson>

from graphics import*


def main():
    win = GraphWin("House", 500, 500)
    win.setCoords(0, 0, 30, 30)
    # Gets first 2 clicks and creates a rectangle using the first click as the lower left corner and the second click as the upper right corner
    first_click = win.getMouse()
    second_click = win.getMouse()
    square = Rectangle(first_click, second_click)
    square.draw(win)

    # Creating variables needed to calculate door dimensions
    third_click = win.getMouse()
    x1 = first_click.getX()
    x2 = second_click.getX()
    x3 = third_click.getX()
    y1 = first_click.getY()
    y2 = third_click.getY()
    door_width = (x2 - x1) / 5

    # Drawing door
    door = Rectangle(Point(x3 - door_width / 2, y2),
                     Point(x3 + door_width / 2, y1))
    door.draw(win)

    # Getting coords of 4th mouse click, calculating square dimensions and drawing a square
    fourth_click = win.getMouse()
    x4 = fourth_click.getX()
    y3 = fourth_click.getY()
    width_w = door_width / 4
    window = Rectangle(Point((x4 - width_w), (y3 - width_w)),
                       Point((x4 + width_w), (y3 + width_w)))
    window.draw(win)

    # getting 5th mouse click and creating/drawing 2 lines
    fith_click = win.getMouse()
    y4 = second_click.getY()

    right_roof = Line(fith_click, second_click)
    left_roof = Line(fith_click, Point(x1, y4))
    right_roof.draw(win)
    left_roof.draw(win)

    # Exit message and window close
    message = Text(Point(15, 15), "Click to quit")
    message.draw(win)
    win.getMouse()
    win.close()


main()
