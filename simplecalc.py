"""
Filename:   simplecalc.py
Author:     Sang Shin
Date:       08/12/2012
"""
#!/bin/env python
import sys

def printUsage():
    print
    print "[USAGE]: Operand Operator Operand"
    print "A space is required between the operand and operator."
    sys.exit()

def main():
    print "----- SIMPLE CALCULATOR -----"
    cont = "y"

    while cont.lower() == "y":
        try:
            operand1, operator, operand2 = raw_input("Enter a calculation (+, -, *, /): ").split()
        except ValueError:
            printUsage()
    
        if operator == "+":
            result_add = int(operand1) + int(operand2)
            print "%s %s %s = %d" % (operand1, operator, operand2, result_add)

        elif operator == "-":
            result_sub = int(operand1) - int(operand2)
            print "%s %s %s = %d" % (operand1, operator, operand2, result_sub)

        elif operator == "*":
            result_mul = int(operand1) * int(operand2)
            print "%s %s %s = %s" % (operand1, operator, operand2, result_mul)

        elif operator == "/":
            result_div = int(operand1) / int(operand2)
            result_div_rem = int(operand1) % int(operand2)
            print "%s %s %s = %s with remainder %s" % (operand1, operator, operand2, result_div, result_div_rem)

        else:
            print "An error occurred. Exiting."
            sys.exit()
        
        print    
        cont = raw_input("Continue (y or n)? ")
        print
        print "Thanks for using the simple calculator."

if __name__ == "__main__":
    main()
