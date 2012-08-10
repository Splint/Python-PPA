"""
Filename:   einsteinpuzzle.py
Author:     Sang Shin
Date:       08/10/2012
"""
#!/bin/env python
def reverseInt(n):
    return int(str(n)[::-1])

def main():
    print "This is a puzzle favored by Einstein." 
    print "You will be asked to enter a three digit, where the hundred's digit differs from the one's digit by at least two."
    print "The procedure will always yield 1089."
    print

    user_input = raw_input("Please enter a valid number: ")
    input_int = int(user_input)
    input_rev = reverseInt(input_int)

    print "The difference between %d and %d is %d" % (input_int, input_rev, input_int - input_rev)
    print "The reverse of the difference is %s" % reverseInt(input_int - input_rev)
    print "The sum of the difference (%d) and reverse difference (%d) is: %d" % (input_int - input_rev, reverseInt(input_int - input_rev), (input_int - input_rev) + reverseInt(input_int - input_rev))
if __name__ == "__main__":
    main()
