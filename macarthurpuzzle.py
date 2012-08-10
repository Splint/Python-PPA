"""
Filename:   macarthurpuzzle.py
Author:     Sang Shin
Date:       08/10/2012
"""
#!/bin/env python
SECRET_NUM = 115
MONTH_LIST = {  "1":"January",
                "2":"February",
                "3":"March",
                "4":"April",
                "5":"May",
                "6":"June",
                "7":"July",
                "8":"August",
                "9":"September",
                "10":"October",
                "11":"November",
                "12":"December"}

def main():
    print "This is a puzzle favored by Gen. MacArthur."
    print "You will be asked to type in your birth month (integer) and your age."
    print "The computer will make a special calculation, yielding a new integer."
    print "The computer will then calculate, using only that special number, your birth month and age."
    print "Let's get started..."
    print

    input_mon = raw_input("Please enter your birth month: ")
    input_age = raw_input("Please enter your age: ")

    special_num = (((((int(input_mon) * 2) + 5) * 50) + int(input_age)) - 365)
    
    print "The special number is %d" % special_num
    
    result = special_num + SECRET_NUM

    length = len(str(result))

    if length < 4:
        user_mon = str(result)[:1] 
        user_age = str(result)[1:]

    elif length < 5:
        user_mon = str(result)[:2]
        user_age = str(result)[2:5]

    else:
        user_mon = str(result)[:3]
        user_age = str(result)[3:6]

    print "The computer calculates that you were born in %s and currently is %s years old" % (MONTH_LIST[user_mon], user_age)


if __name__ == "__main__":
    main()
