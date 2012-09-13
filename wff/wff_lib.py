"""
Filename:   wff_lib.py
Author:     Sang Shin
Date:       09/12/2012

Core functions that are used in the we feel fine program
"""
#!/bin/env python
import sys

def feelings_frequency(feelings, content):
    # Check each line of content for the feeling
    # If the feeling is in the line of content, increase the frequency
    # Include it as a dictionary
    frequencyDict = {}
    for feel in feelings:
        count = 0
        for line in content:
            if feel in str(line):
                count += 1
        
        if count != 0: 
            frequencyDict[feel] = count
        else:
            continue

    return frequencyDict

def construct_html_string(html, age, aStatus, gender, gStatus, city, cStatus):
    # Construct the html string that we are going to get data from.
    # 9 possible combinations:
    #       age - gender - city
    #   1. T - T - T
    #   2. F - T - T
    #   3. F - F - T
    #   4. F - F - F
    #   5. T - F - T
    #   6. T - F - F
    #   7. T - T - F
    #   8. F - T - F
    if (aStatus, gStatus, cStatus) == (True, True, True):
        if str(age) == "":
            aQuery = ""
        else:
            aQuery = "&agerange=" + str(age)
        
        if str(gender) == "":
            gQuery = ""
        else:
            gQuery = "&gender=" + str(gender)
        
        if str(city) == "":
            cQuery = ""
        else:
            cQuery = "&city=" + str(city)
        
        fQuery = str(html) + aQuery + gQuery + cQuery + "&"
        return fQuery
    
    elif (aStatus, gStatus, cStatus) == (False, True, True):
        if str(gender) == "":
            gQuery = ""
        else:
            gQuery = "&gender=" + str(gender)
        
        if str(city) == "":
            cQuery = ""
        else:
            cQuery = "&city=" + str(city)
        
        fQuery = str(html) + gQuery + cQuery + "&"
        return fQuery
    
    elif (aStatus, gStatus, cStatus) == (False, False, True):
        if str(city) == "":
            cQuery = ""
        else:
            cQuery = "&city=" + str(city)
        
        fQuery = str(html) + cQuery + "&"
        return fQuery

    elif (aStatus, gStatus, cStatus) == (False, False, False):
        return fQuery

    elif (aStatus, gStatus, cStatus) == (True, False, True):
        if str(age) == "":
            aQuery = ""
        else:
            aQuery = "&agerange=" + str(age)
        
        if str(city) == "":
            cQuery = ""
        else:
            cQuery = "&city=" + str(city)
        
        fQuery = str(html) + aQuery + cQuery + "&"
        return fQuery

    elif (aStatus, gStatus, cStatus) == (True, False, False):
        if str(age) == "":
            aQuery = ""
        else:
            aQuery = "&agerange=" + str(age)
        
        fQuery = str(html) + aQuery + "&"
        return fQuery

    elif (aStatus, gStatus, cStatus) == (True, True, False):
        if str(age) == "":
            aQuery = ""
        else:
            aQuery = "&agerange=" + str(age)
        
        if str(gender) == "":
            gQuery = ""
        else:
            gQuery = "&gender=" + str(gender)
        
        fQuery = str(html) + aQuery + gQuery + "&"
        return fQuery

    elif (aStatus, gStatus, cStatus) == (False, True, False):
        if str(gender) == "":
            gQuery = ""
        else:
            gQuery = "&gender=" + str(gender)
        
        fQuery = str(html) + gQuery + "&"
        return fQuery

    else:
        print "An error occurred. Exiting!"
        sys.exit()

def get_feelings_list():
    # Get the different feelings from a text file
    # 2 scenarios for getting the feelings:
    #   a. Check to see if the file exists. If not, exit the entire program.
    #   b. Get all feelings into a list and return the value
    try:
        fi = open('feelings.txt', 'r')
    except IOError:
        print "File was not found. Exiting the system!"
        sys.exit()
    
    feelings_list = [line.split()[0] for line in fi]

    return feelings_list

def check_valid_city(inp):
    # Check the validity of the city
    # 2 scenarios for getting the cities:
    #   a. Check to see if the file exists. If not, exit the entire program.
    #   b. Get all cities into a list to compare
    #
    # 3 scenarios for checking the user input:
    #   a. If the city is valid
    #   b. If nothing is entered as city, city = ""
    #   c. If garbage is entered, omit the city option from string
    VALID_CITY = False
    try:
        fi = open('worldcitiespop.txt', 'r')
    except IOError:
        print "File was not found. Exiting the system!"
        sys.exit()
    
    city_list = [line.split(',')[1] for line in fi]

    try:
        if str(inp) == "":
            inp = ""
            VALID_CITY = True
            return (inp, VALID_CITY)
        
        elif str(inp).lower() in city_list:
            VALID_CITY = True
            return (inp, VALID_CITY)
        
        else:
            return (inp, VALID_CITY)

    except ValueError:
        return (inp, VALID_CITY)
        

def check_valid_gend(inp):
    # Check the validity of the gender
    # 3 scenarios for checking the user input:
    #   a. If gender is valid
    #   b. If nothing is entered as gender, gender = ""
    #   c. If garbage is entered, omit the gender option from string
    VALID_GEND = False
    try:
        if str(inp) == "":
            inp = ""
            VALID_GEND = True
            return (inp, VALID_GEND)

        elif str(inp).lower() == "m" or str(inp).lower() == "male":
            inp = 1
            VALID_GEND = True
            return (inp, VALID_GEND)

        elif str(inp).lower() == "f" or str(inp).lower() == "female":
            inp = 0
            VALID_GEND = True
            return (inp, VALID_GEND)
        
        else:
            return (inp, VALID_GEND)

    except ValueError:
        return (inp, VALID_GEND)
        
def check_valid_age(inp):
    # Check the validity of the age
    # 3 scenarios for checking the user input:
    #   a. If age is valid, divisible by 10
    #   b. If age is valid, not divisible by 10, make it divisible by 10
    #   c. If nothing is entered as age, age = ""
    #   d. If garbage is entered, omit the age option from string
    VALID_AGE = False
    try:
        if str(inp) == "":
            inp = ""
            VALID_AGE = True
            return (inp, VALID_AGE)

        elif int(inp) % 10:
            firstDigit = int(inp) / 10
            inp = str(firstDigit) + str(0)
            VALID_AGE = True
            return (inp, VALID_AGE)

        elif (int(inp) % 10) == 0:
            VALID_AGE = True
            return (inp, VALID_AGE)

        else:
            return (inp, VALID_AGE)
    
    except ValueError:
        return (inp, VALID_AGE)
