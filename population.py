"""
Filename:   population.py
Author:     Sang Shin
Date:       08/09/2012
"""
#!/bin/env python
FIXED_POPULATION = 307357870
CONVERSION_YEAR_DAY = 365
CONVERSION_DAY_HOUR = 24
CONVERSION_HOUR_MINUTE = 60
CONVERSION_MINUTE_SECOND = 60
BIRTH_SECOND = 7
DEATH_SECOND = 13
IMMIGRANT_SECOND = 35

def main():
    user_input = input("Enter the number of years to predict: ")
   
    """
    We want to make the conversion from years to seconds.
        * There are 365 days in 1 year
        * There are 24 hours in 1 day
        * There are 60 minutes in 1 hour
        * There are 60 seconds in 1 minute
    """
    result_seconds = user_input * CONVERSION_YEAR_DAY * CONVERSION_DAY_HOUR * CONVERSION_HOUR_MINUTE * CONVERSION_MINUTE_SECOND
    result_birth = result_seconds / BIRTH_SECOND
    result_death = result_seconds / DEATH_SECOND
    result_immigrant = result_seconds / IMMIGRANT_SECOND

    result_new = result_birth + result_immigrant - result_death
    
    print "New popluation in %s years will change by %s to be %s" % (user_input, result_new, FIXED_POPULATION + result_new)

if __name__ == "__main__":
    main()
