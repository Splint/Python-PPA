"""
Filename:   numpersistence.py
Author:     Sang Shin
Date:       08/11/2012
"""
#!/bin/env python
import digicount as digi
import sys

PERSISTENCE_ADD_COUNT = 0
PERSISTENCE_MUL_COUNT = 0

def printProgression(val, state):
    global PERSISTENCE_ADD_COUNT, PERSISTENCE_MUL_COUNT

    if state == "add":
        PERSISTENCE_ADD_COUNT += 1
        print "Sum: %s" % val
        
    elif state == "multiply":
        PERSISTENCE_MUL_COUNT += 1
        print "Mul: %s" % val

    else:
        print "An error occurred. Exiting"
        sys.exit()

def performArithmetic(arr, state):
    result_add = 0
    result_mul = 1

    if state == "add":
        for i in arr:
            result_add = result_add + int(i)
         
        return result_add

    elif state == "multiply":
        for i in arr:
            result_mul = result_mul * int(i)

        return result_mul
    
    else:
        print "An error occurred. Exiting."
        sys.exit()

def additivePersistence(arr):
    print "----- Performing Additive Loop -----"
    result_add = performArithmetic(arr, "add")
    printProgression(result_add, "add")

    result_add_split = splitInput(result_add)
    result_sum = performArithmetic(result_add_split, "add")
    
    printProgression(result_sum, "add")
    
    while(len(str(result_sum)) != 1):
        result_split = splitInput(result_sum)
        result_sum = performArithmetic(result_split, "add")
        printProgression(result_sum, "add")
    
    return result_sum

def multiplicativePersistence(arr):
    print "----- Peforming Multiplicative Loop -----"
    result_mul = performArithmetic(arr, "multiply")
    printProgression(result_mul, "multiply")

    result_mul_split = splitInput(result_mul)
    result_sum = performArithmetic(result_mul_split, "multiply")

    printProgression(result_sum, "multiply")
    
    while(len(str(result_sum)) != 1):
        result_split = splitInput(result_sum)
        result_sum = performArithmetic(result_split, "multiply")
        printProgression(result_sum, "multiply")
    
    return result_sum

def splitInput(arr):
    new_arr = [elem for elem in str(arr)]
    return new_arr

def main():
    userInput = digi.userInputChecker("Enter an integer: ")
    arr = splitInput(userInput)
    print

    additive_root = additivePersistence(arr)
    multiplicative_root = multiplicativePersistence(arr)
    
    print
    print
    print "Summary for the integer %d" % userInput
    print "\t Additive Persistence %d, Additive Root %d" % (PERSISTENCE_ADD_COUNT, additive_root)
    print "\t Multiplicative Persistence %d, Multiplicative Root %d" % (PERSISTENCE_MUL_COUNT, multiplicative_root)

if __name__ == "__main__":
    main()
