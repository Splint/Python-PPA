"""
Filename:   lib.py
Author:     Sang Shin
Date:       09/13/2012

Library for core functions of the GDP-Employment program
"""
#!/bin/env python
import sys, csv

def calculate_average_unemp(fi, year):
    # We take in the filename of the csv and the year
    # We use the csv module in python to read the file
    # The reader contain rows that are in forms of lists
    # We check each list to see if the year is in any of them
    # If we find a hit, we want to grab all the numbers in the row
    #   * Since the numbers are in a month format we want 1 - 12
    # We add all 12 numbers together and find the average
    monthStart = 1
    monthEnd = 12
    summation = 0.0
    average = 0.0
    with open(fi, 'rb') as fi:
        reader = csv.reader(fi)
        try:
            for row in reader:
                if year in row:
                    for i in range(monthStart, monthEnd + 1):
                        summation += float(row[i])

            average = (float(summation) / float(monthEnd))
            return average
        except csv.Error, e:
            print "An error occurred. Exiting!"
            sys.exit()

def calculate_average_gdp(fi, year):
    # We are given the file content and the year
    # We need to split the file content into 3 parts: Year - Quarter - GDP
    # We split the file content into a list and find the year in that list
    # For each year we hit, we want to add the GDP together and increment the count
    # We then want to calculate the average and return
    summation = 0.0
    average = 0.0
    count = 0.0
    fi_list = [line.split() for line in fi]
    for block in fi_list:
        if year in block:
            count += 1
            summation += float(block[2])

    average = (float(summation) / float(count))
    return average

def valid_filename(fn):
    # Check to see if the filename is valid.
    # If not, return with a 0. If so, return with a 1.
    try:
        vfn = open(fn, 'r')
        if vfn:
            return (vfn, 1)

    except IOError:
        vfn = ""
        return (vfn, 0)
