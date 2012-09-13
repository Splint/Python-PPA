"""
Filename:   wff.py
Author:     Sang Shin
Date:       09/07/2012
"""
#!/bin/env python
import sys, urllib, math
import wff_lib as wffLib

html = "http://api.wefeelfine.org:8080/ShowFeelings?display=text&returnfields=sentence&limit=1500"

def main():
    aStatus = False
    gStatus = False
    cStatus = False
    print "This is a feeling generator that will take data from the website http://www.wefeelfine.org and display it appropriately."
    
    # --- Prompt user for age, gender, and city ---
    age = raw_input("Enter an age (<Enter> for all): ")
    (age, aStatus) = wffLib.check_valid_age(age)
    
    gender = raw_input("Enter a gender (<Enter> for all): ")
    (gender, gStatus) = wffLib.check_valid_gend(gender)

    city = raw_input("Enter a city (<Enter> for all): ")
    (city, cStatus) = wffLib.check_valid_city(city)
    
    # Get the feelings into a list
    feelingList = wffLib.get_feelings_list()

    # Construct HTML string
    constructHtml = wffLib.construct_html_string(html, age, aStatus, gender, gStatus, city, cStatus)
    
    # Make the connection to the website
    print "Requesting to %s" % constructHtml 
    print
    connection = urllib.urlopen(constructHtml)
    pageContent = connection.read()
    
    # Strip the garbage in front of each line and at the end of each line
    contentList = pageContent.split("<br>")
    contentList = [line.lstrip('\r\n') for line in contentList]
    contentList = [line.rstrip('\t') for line in contentList]
    
    print "Records found: %s" % str(len(contentList))

    # Grab the frequency list and print out the list
    frequencyList = wffLib.feelings_frequency(feelingList, contentList)
    print "------------------------------------------------------------"
    print "------------------------------------------------------------"
    for key, value in frequencyList.items():
        print "%25s  :    %s" % (str(key), str(value))

if __name__ == "__main__":
    main()
