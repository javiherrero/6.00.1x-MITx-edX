# Desc: Quiz - Problem 4.
# Author: Javier Herrero Arnanz.

def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    
    # Search the exponent until the square will be higher than x.
    exp = 0
    while (b**exp <= x):
        exp += 1
        
    return (exp - 1)
    
print myLog(16,2)
print myLog(15,3)
