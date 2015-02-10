# Desc: Lec 5, Problem 8.
# Author: Javier Herrero Arnanz.

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if (len(aStr) <= 1):
        return (char == aStr)
    else:
        midPos = len(aStr)/2
        midChar = aStr[midPos]
        
        if (char == midChar):
            return True
        elif (char > midChar):
            return isIn(char,aStr[midPos+1:])
        else:
            return isIn(char,aStr[:midPos])

print isIn('l','')
