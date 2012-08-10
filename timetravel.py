"""
Filename:   timetravel.py
Author:     Sang Shin
Date:       08/10/2012
"""
#!/bin/env python
import math

SPEED_LIGHT_METER_SECOND = 299792458
FIXED_SHUTTLE_WEIGHT = 70000
ASTRO_EXP_ALPHA = 4.3
ASTRO_EXP_BARNARD = 6
ASTRO_EXP_BETELGEUSE = 309
ASTRO_EXP_ANDROMEDA = 2000000

def main():
    user_input = raw_input("Please enter the velocity (percentage of speed of light): ")
    input_fl = float(user_input)
    
    temp_var = SPEED_LIGHT_METER_SECOND * (input_fl/100)
    result = SPEED_LIGHT_METER_SECOND - temp_var

    factor = 1/math.sqrt(1-(math.pow(result, 2)/math.pow(SPEED_LIGHT_METER_SECOND, 2)))

    print "Ship is traveling at %.2f%% of the speed of light." % input_fl
    print
    print "At this speed:"
    print "\t Weight of the shuttle is %f kilograms" % (FIXED_SHUTTLE_WEIGHT * factor)
    print "\t Perceived time to travel to Alpha Centauri is %f years" % (ASTRO_EXP_ALPHA / factor)
    print "\t Perceived time to travel to Barnard's Star is %f years" % (ASTRO_EXP_BARNARD / factor)
    print "\t Perceived time to travel to Betelgeuse is %f years" % (ASTRO_EXP_BETELGEUSE / factor)
    print "\t Perceived time to travel to Andromeda Galaxy is %f years" % (ASTRO_EXP_ANDROMEDA / factor)

if __name__ == "__main__":
    main()
