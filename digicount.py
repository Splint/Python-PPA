"""
Filename:   digicount.py
Author:     Sang Shin
Date:       08/10/2012
"""
#!/bin/env python

def userInputChecker(diag):
    check = 1
    while check == 1:
        try:
            inp_str = raw_input(diag)
            inp_int = int(inp_str)
            check = 0

        except ValueError:
            check = 1
            print "Please enter a valid number."

    return inp_int

def main():
    inp_int = userInputChecker("Enter a number: ")
    print "The number entered is %d" % inp_int
    print

    inp_int_digi = userInputChecker("Enter a digit: ")
    print "The digit entered is %d" % inp_int_digi
    print
    
    digi_arr = [digi for digi in str(inp_int)]
    count = digi_arr.count(str(inp_int_digi))

    print "The number of %s's in %s is %d" % (str(inp_int_digi), str(inp_int), count)

if __name__ == "__main__":
    main()
