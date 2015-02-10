# Desc: Lec 5, Problem 1.
# Author: Javier Herrero Arnanz.

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1
    for i in range(1,exp + 1):
        result *= base

    return round(result,4)
    
print iterPower(2,5)
