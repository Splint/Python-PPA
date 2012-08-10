"""
Filename:   gasoline.py
Author:     Sang Shin
Date:       08/09/2012
"""
#!/bin/env python
from __future__ import division

CONVERSION_GAL_LITER = 3.7854
CONVERSION_GAL_BARREL = 19.5
CONVERSION_GAL_POUND = 20
CONVERSION_GAL_ENERGY = 115000
CONVERSION_GAL_ENERGY_ETH = 75700
CONVERSION_GAL_DOLLAR = 4.00

def main():
    user_input = raw_input("Please enter the number of gallons of gasoline: ")
    input_fl = float(user_input)
    
    print "Original number of gallons is: %.2f" % input_fl
    
    print "%.2f gallons is the equivalent of %.2f liters" % (input_fl, \
                                                             input_fl * CONVERSION_GAL_LITER)
    
    print "%.2f gallons of gasoline requires %f barrels of oil" % (input_fl, \
                                                                   input_fl / CONVERSION_GAL_BARREL)
    
    print "%.2f gallons of gasoline produces %.2f pounds of C02" % (input_fl, \
                                                                    input_fl * CONVERSION_GAL_POUND)
    print "%.2f gallons of gasoline is energy equivalent to %.2f gallons of ethanol" % (input_fl, \
                                                                    (input_fl * CONVERSION_GAL_ENERGY_ETH)/CONVERSION_GAL_ENERGY)
    
    print "%.2f gallons of gasoline requires $%.2f U.S. Dollars" % (input_fl, input_fl * CONVERSION_GAL_DOLLAR)

    print
    print "Thank you for playing"



if __name__ == "__main__":
    main()
