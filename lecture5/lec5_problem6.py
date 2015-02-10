# Desc: Lec 5, Problem 6.
# Author: Javier Herrero Arnanz.

def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    length = 0
    for letter in aStr:
        length += 1
    return length
    
print lenIter('abcd')
