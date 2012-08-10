"""
Filename:   arithmetic.py
Author:     Splint
Date:       08/09/2012
"""
#!/bin/env python

def main():
    x = input('Please enter the first integer: ')
    y = input('Please enter the second integer: ')
    
    print "The sum of %s and %s is: %s" % (x, y, x + y)
    print "The difference of %s and %s is: %s" % (x, y, x - y)
    print "The product of %s and %s is: %s" % (x, y, x * y)
    print "The quotient of %s and %s is: %s with remainder %s" % (x, y, x/y, x%y)

if __name__ == "__main__":
    main();
