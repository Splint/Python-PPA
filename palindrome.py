"""
Filename:    palindrome.py
Author:      Sang Shin
Date:        08/13/2012
"""
#!/bin/env python
import sys
NAT_PALINDROME_COUNT = 0
LYCHREL_NUM_COUNT = 0
NON_LYCHREL_NUM_COUNT = 0

def algorithm196(num):
    for i in range(0, 60):
	num_reverse = int(str(num)[::-1])
	new_num = int(num) + int(num_reverse)
	state = isPalindrome(new_num)
	if state == 1:
	    return 1
	else:
	    num = new_num
	
    return 0
		
def isPalindrome(num):
    num_reverse = int(str(num)[::-1])
    if int(num) == int(num_reverse):
	return 1
	
    else:
	return 0
	
def main():
    global NAT_PALINDROME_COUNT, LYCHREL_NUM_COUNT, NON_LYCHREL_NUM_COUNT
	
    range1 = raw_input("Enter the first integer: ")
    range2 = raw_input("Enter the second integer: ")
	
    try:
    	range1 = int(range1)
    	range2 = int(range2)
    except ValueError:
    	print "An error has occurred. Exiting."
    	sys.exit()

    for elem in range(range1, range2 + 1):
	""" 
	* For each element in the range provided, we want to check the following:
            1. Is the number a natural palindrome?
	      	a. Yes -> Increment the natural palindrome counter and exit
	        b. No -> Check to see if it is a Lychrel Number (Goto step 2)
	    2. Perform the 196-algorithm on the number. Is the number a non_lychrel number?
	    	a. Yes -> Increment the non_lychrel number counter and exit
	    	b. No -> Check 60 times to determine if it is a non_lychrel number (Goto step 3)
	    3. If the number is a Lychrel number, print the number out. Increment the counter
	"""
		
	""" PERFORM STEP 1: Natural Palindrome? """
	state = isPalindrome(elem)
	if state == 1:
	    NAT_PALINDROME_COUNT += 1
		
	else:
	    """ PERFORM STEP 2: Non_Lychrel Number? """
	    state = algorithm196(elem)
	    if state == 1:
		NON_LYCHREL_NUM_COUNT += 1
			
	    else:
		""" The number is Lychrel """
		LYCHREL_NUM_COUNT += 1
		print "%s looks to be a non_lychrel number" % str(elem)
    print
    print "-------------------------------------"
    print "Summary for the range %s to %s" % (str(range1), str(range2))
    print "\t Palindrome Number Count: %d" % NAT_PALINDROME_COUNT
    print "\t Non-Lychrel Number Count: %d" % NON_LYCHREL_NUM_COUNT
    print "\t Lychrel Number Count: %d" % LYCHREL_NUM_COUNT

if __name__ == "__main__":
    main()
