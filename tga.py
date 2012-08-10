"""
Filename:   tga.py
Author:     Sang Shin
Date:       08/10/2012
"""
#!/bin/env python
import turtle as tu
import math
import sys

def drawTurtle(xpt1, ypt1, xpt2, ypt2):
    tu.title("tule Graphics with Python")
    
    tu.down()    
    tu.goto(xpt1, ypt1)
    tu.write(xpt1, ypt1)
    
    tu.goto(xpt2, ypt2)
    tu.write(xpt2, ypt2)

    tu.up()

    tu.done()

def main():
    x_coord_pt1_str = raw_input("Point 1 -> Enter the x-coordinate: ")
    y_coord_pt1_str = raw_input("Point 1 -> Enter the y-coordinate: ")
    x_coord_pt1 = int(x_coord_pt1_str)
    y_coord_pt1 = int(y_coord_pt1_str)
    print
    x_coord_pt2_str = raw_input("Point 2 -> Enter the x-coordinate: ")
    y_coord_pt2_str = raw_input("Point 2 -> Enter the y-coordinate: ")
    x_coord_pt2 = int(x_coord_pt2_str)
    y_coord_pt2 = int(y_coord_pt2_str)

    m1 = y_coord_pt1 / x_coord_pt1

    try:
        m2 = (y_coord_pt2 - y_coord_pt1) / (x_coord_pt2 - x_coord_pt1)

    except ZeroDivisionError:
        print "Can't divide by zero. Exiting."
        sys.exit()

    tan_angle = (m2 - m1) / (1 + m1*m2)
    angle_rad = math.atan(abs(tan_angle))
    angle_deg = (angle_rad * 180) / math.pi

    drawTurtle(x_coord_pt1, y_coord_pt1, x_coord_pt2, y_coord_pt2)

if __name__ == "__main__":
    main()
