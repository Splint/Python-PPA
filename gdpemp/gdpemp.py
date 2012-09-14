"""
Filename:   gdpemp.py
Author:     Sang Shin
Date:       09/13/2012
"""
#!/bin/env python
import sys
import lib as GDPLIB

CONST_MIN_DATE = 1948
CONST_MAX_DATE = 2008

def main():
    # Ask the user for a valid GDP file.
    # If none exists, prompt the user with a message, and repeat.
    status = 0
    while not status:
        gdpFilename = raw_input("Enter a GDP file: ")
        (gdpFile, status) = GDPLIB.valid_filename(gdpFilename)

        if not status:
            print "File not found. Try again."
            print
    
    # Ask the user for a valid CSV file.
    # If none exists, prompt the user with a message, and repeat.
    status = 0
    while not status:
        csvFilename = raw_input("Unemployment File: ")
        (csvFile, status) = GDPLIB.valid_filename(csvFilename)

        if not status:
            print "File not found. Try again."
            print

    # As the user for a valid year date.
    # If the date is less than 1948 or greater than 2008, repeat.
    # If the date is garbage, repeat.
    while True:
        year = raw_input("Year to examine: ")
        if int(year) in range(CONST_MIN_DATE, CONST_MAX_DATE + 1):
            break

        else:
            print "Bad year, try again."
            print
    
    # Get the average GDP for the specified year
    avgGDP = GDPLIB.calculate_average_gdp(gdpFile, year)

    # Get average unemployment for the specified year
    avgUnemp = GDPLIB.calculate_average_unemp(csvFilename, year)

    # Print out what we have
    print "For %d, average GDP: %f and average unemployment: %.3f" % (int(year), float(avgGDP), float(avgUnemp))

if __name__ == "__main__":
    main()
