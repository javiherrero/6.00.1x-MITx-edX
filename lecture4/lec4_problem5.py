# Desc: Lec 4, Problem 5.
# Author: Javier Herrero Arnanz.

def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    return max(lo,min(hi,x))
    
print clip(10,22,20)
