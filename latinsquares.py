"""
Filename:   latinsquares.py
Author:     Sang Shin
Date:       08/10/2012
"""
#!/bin/env python
import digicount as digi

def printLatinSquare(arr, inp_int):
    """
    List    =   [[1, 2, 3, 4], [2, 3, 4, 1]]
     i      =          0             1
    """
    for i in range(0, inp_int):
        print arr[i]

def makeLatinSquare(inp_int, inp_top_left):
    arr = [num for num in range(1, inp_int + 1)]
    
    idx = 0
    idx = arr.index(inp_top_left)

    result_arr = [[arr[i-j] for i in range(idx, inp_int + 1)] for j in range(len(arr), 0, -1)]
    
    printLatinSquare(result_arr, inp_int)

def main():
    inp_int = digi.userInputChecker("How big do you want the square? ")
    inp_top_left = digi.userInputChecker("What number do you want at the top left? ")
    
    makeLatinSquare(inp_int, inp_top_left)

if __name__ == "__main__":
    main()
