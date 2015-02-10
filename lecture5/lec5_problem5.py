# Desc: Lec 5, Problem 5.
# Author: Javier Herrero Arnanz.

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''   
    if (b == 0):
        return a
    else:
        return gcdRecur(b,a%b)
        
print gcdRecur(6,12)
