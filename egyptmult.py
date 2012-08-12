"""
Filename:   egyptmult.py
Author:     Sang Shin
Date:       08/12/2012
"""
#!/bin/env python
import sys

def perfAdd(arr):
    result_add = 0
    for i in arr:
        result_add = result_add + int(i)

    return result_add

def perfEgyptAlgo(val_a, val_b):
    val_a = int(val_a) * 2
    val_b = int(val_b) / 2

    return val_a, val_b

def printValues(val_a, val_b):
    print "A = %d and B = %d" % (int(val_a), int(val_b))

def checkIfBIsOdd(val_b):
    if int(val_b) % 2 == 0:
        return False
    
    else:
        return True

def main():
    val_a, val_b = raw_input("Please input the 2 numbers separated by a space: ").split()
    state_b = checkIfBIsOdd(val_b)
    run_arr = []

    while(int(val_b) != 0):
        if state_b == True:
            """
            If the value of b is odd, we want to add the value of A to an array
            """
            printValues(val_a, val_b)
            print "B was odd, we add A to list: %d" % int(val_a)
            run_arr.append(val_a)
            val_a, val_b = perfEgyptAlgo(val_a, val_b)
            state_b = checkIfBIsOdd(val_b) 
        
        elif state_b == False:
            """
            If the value of b is even, we want to ignore the value of A
            """
            printValues(val_a, val_b)
            val_a, val_b = perfEgyptAlgo(val_a, val_b)
            state_b = checkIfBIsOdd(val_b)

        else:
            print "An error occurred. Exiting."
            sys.exit()
    
    final_product = perfAdd(run_arr)
    print
    print "Final Product: %d" % int(final_product)

if __name__ == "__main__":
    main()
