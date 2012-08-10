"""
Filename:   tgp.py
Author:     Sang Shin
Date:       08/10/2012
"""
#!/bin/env python
import turtle as tu
import sys


def draw_tule(shape, red, blue, green):
    tu.title("Turtle Graphics with Python")
    tu.fillcolor(red, blue, green)
    tu.pencolor(red, blue, green)

    tu.up()
    tu.begin_fill()

    if shape.lower() == 'square':
        tu.goto(100, 100)
        tu.down()
        tu.goto(100, -100)
        tu.goto(-100, -100)
        tu.goto(-100, 100)
        tu.goto(100, 100)
        tu.end_fill()

    elif shape.lower() == "circle":
        tu.down()
        tu.circle(100)
        tu.end_fill()

    elif shape.lower() == "triangle":
        tu.goto(-100, -100)
        tu.down()
        tu.goto(100, -100)
        tu.goto(0, 100)
        tu.goto(-100, -100)
        tu.end_fill()
    
    elif shape.lower() == "rectangle":
        tu.goto(200, 50)
        tu.down()
        tu.goto(200, -50)
        tu.goto(-200, -50)
        tu.goto(-200, 50)
        tu.goto(200, 50)
        tu.end_fill()

    elif shape.lower() == "pentagon":
        tu.goto(0, 100)
        tu.down()
        tu.goto(-100, 0)
        tu.goto(-50, -100)
        tu.goto(50, -100)
        tu.goto(100, 0)
        tu.goto(0, 100)
        tu.end_fill()

    else:
        print "An error occurred. Exiting."
        sys.exit()
    
    tu.done()

def main():
    print "This program will create a polygon with input by the user."
    print "The user will be prompted 4 times to enter specific information."
    print "Turtle Graphics will be used to draw the shape and color it in."
    print "Let's begin..."
    print

    red_str = raw_input("Please enter a red value (0 - 1): ")
    red_fl = float(red_str)

    blue_str = raw_input("Please enter a blue value (0 - 1): ")
    blue_fl = float(blue_str)

    green_str = raw_input("Please enter a green value (0 - 1): ")
    green_fl = float(green_str)

    print
    print "Choose a shape:"
    print "\tTriangle"
    print "\tCircle" 
    print "\tSquare"
    print "\tRectangle"
    print "\tPentagon"
    print
    
    shape_str = raw_input()
    
    print
    print "Summary: "
    print "\t Red Value: %.2f" % red_fl
    print "\t Blue Value: %.2f" % blue_fl
    print "\t Green Value: %.2f" % green_fl
    print "\t Shape: %s" % shape_str
    print
    print "Drawing the turtle..."

    draw_tule(shape_str, red_fl, blue_fl, green_fl)

if __name__ == "__main__":
    main()
