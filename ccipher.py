"""
Filename:   ccipher.py
Author:     Sang Shin
Date:       09/05/2012
"""
#!/bin/env python
import sys

CONST_ALBET = 'abcdefghijklmnopqrstuvwxyz'
MOD_ALBET = ''

def exit_program():
    # Prompt the user with a exiting greet and terminate.
    print "Thank you for using the Caesar Cipher Program."
    print "Have a nice day."
    sys.exit()

def rotate_alphabet(rot, direc):
    rot = int(rot)

    # For left rotations, we need to adapt for numbers greater than 26
    # Rotate the alphabet to the left
    if (str(direc).lower() == 'l') or (str(direc).lower() == "left"):
        while rot == len(CONST_ALBET) or rot > len(CONST_ALBET):
            rot = rot - len(CONST_ALBET)

        lowEnd = [CONST_ALBET[i] for i in range(0, rot)]
        highEnd = [CONST_ALBET[i] for i in range(rot, len(CONST_ALBET))]
        modAlphabetList = highEnd + lowEnd
        modAlphabet = "".join(modAlphabetList)
        return modAlphabet

    # For right rotations, we need to adapt for numbers greater than 26
    # Rotate the alpabet to the right
    elif (str(direc).lower() == 'r') or (str(direc).lower() == "right"):
        while rot == len(CONST_ALBET) or rot > len(CONST_ALBET):
            rot = rot - len(CONST_ALBET)

        lowEnd = [CONST_ALBET[i] for i in range(len(CONST_ALBET) - rot, len(CONST_ALBET))]
        highEnd = [CONST_ALBET[i] for i in range(0, (len(CONST_ALBET) - rot))]
        modAlphabetList = lowEnd + highEnd
        modAlphabet = "".join(modAlphabetList)
        return modAlphabet

    else:
        print "An error occurred. Exiting."
        sys.exit()

def encode_string(userString):
    (encodedString, encodedSplitString) = ([],[])
    # Check to see if the letter is in the alphabet. If not, add it to the array.
    # If the letter is in the alphabet, we need to find the index of it in the 
    # original alphabet, and find the corresponding letter in the modified alphabet.
    for lett in str(userString).lower():
        if lett in str(CONST_ALBET):
            idx = str(CONST_ALBET).index(lett.lower())

            count = 0
            for lett_mod in str(MOD_ALBET):
                if int(idx) == count:
                    encodedString.append(lett_mod)
                    break

                else:
                    count += 1

        else:
            encodedString.append(lett)
    
    # We have a list that contains only letters. We are going to combine the letters
    # to create the word and add it to a list.
    encodedString = ''.join(encodedString)
    encodedSplitString = encodedString.split()
    
    return encodedSplitString

def encode_procedure():
    global MOD_ALBET
    userString = raw_input("Enter a string to encode: ")
    userRotation = raw_input("Enter a rotation: ")

    while True:
        userDirection = raw_input("Enter a direction (L or R): ")

        # Check for correction direction
        if (str(userDirection).lower() == 'l') or \
                (str(userDirection).lower() == 'left') or \
                (str(userDirection).lower() == 'r') or \
                (str(userDirection).lower() == 'right'):
                    break

        else:
            print "Invalid input. Try again."

    MOD_ALBET = rotate_alphabet(userRotation, userDirection)
    encodedUserString = encode_string(userString)
    encodedUserString = ' '.join(encodedUserString)
    print
    print "Encoded String: %s" % encodedUserString

def check_decode_procedure(userString, userWord):
    # We want to loop through every possible combination of
    # rotations of the alphabet and see if the word provided
    # by the user is in the decoded string.
    #
    # There are two possible outcomes for every decoding method
    # for left and right rotations. Since these rotations overlap
    # somewhere, we need to find both.
    global MOD_ALBET
    decodedData = {}

    for i in range(1, len(CONST_ALBET) + 1):
        MOD_ALBET = rotate_alphabet(i, 'l')
        decodedUserString = decode_string(userString)
        if userWord in decodedUserString:
            decodedData["Left"] = i
            break

    for i in range(1, len(CONST_ALBET) + 1):
        MOD_ALBET = rotate_alphabet(i, 'r')
        decodedUserString = decode_string(userString)
        if userWord in decodedUserString:
            decodedData["Right"] = i
            break

    return (decodedUserString, decodedData)

def decode_string(userString):
    (decodedString, decodedSplitString) = ([],[])
    # Check to see if the letter is in the MOD_Alphabet. If not, add it to the array.
    # If the letter is in the MOD_Alphabet, we need to find the index of it in the 
    # MOD_Alphabet, and find the corresponding letter in the original alphabet.
    for lett_mod in str(userString).lower():
        if lett_mod in str(MOD_ALBET):
            idx = str(MOD_ALBET).index(lett_mod.lower())

            count = 0
            for lett in str(CONST_ALBET):
                if int(idx) == count:
                    decodedString.append(lett)
                    break

                else:
                    count += 1

        else:
            decodedString.append(lett_mod)
    
    # We have a list that contains only letters. We are going to combine the letters
    # to create the word and add it to a list.
    decodedString = ''.join(decodedString)
    decodedSplitString = decodedString.split()

    return decodedSplitString

def decode_procedure():
    global MOD_ALBET
    userString = raw_input("Enter a string to decode: ")
    userWord = raw_input("Enter a word in the string: ")
    
    (decodedUserString, decodeData) = check_decode_procedure(userString, userWord)
    decodedUserString = ' '.join(decodedUserString)
    print
    print "Decoded String: %s" % decodedUserString
    print "Possible Combinations: "
    if "Left" in decodeData:
        print "\t Direction: Left \t Rotation: %s" % decodeData["Left"]
    
    if "Right" in decodeData:
        print "\t Direction: Right \t Rotation: %s" % decodeData["Right"]
    
    else:
        print "\t None. Decoding procedure failed."

def main():
    print "This is the Caesar Cipher Program."
    print "This will either encode or decode a string with the Caesar Algorithm."
    while True:
        print
        print "\t 'e' to ENCODE"
        print "\t 'd' to DECODE"
        print "\t 'q' to QUIT"
        print
        userInput = raw_input("\t ---> ")

        if (str(userInput).lower() == 'e') or (str(userInput).lower() == 'encode'):
            encode_procedure()

        elif (str(userInput).lower() == 'd') or (str(userInput).lower() == 'decode'):
            decode_procedure()
        
        elif (str(userInput).lower() == 'q') or (str(userInput).lower() == 'quit'):
            exit_program()

        else:
            print "Invalid Input. Try again."

if __name__ == "__main__":
    main()
