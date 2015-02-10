# Desc: Lec 4, Problem 8.
# Author: Javier Herrero Arnanz.

def square(x):
    '''
    x: int or float.
    result: x²
    '''
    return x*x

def fourthPower(x):
    '''
    x: int or float.
    '''
    return (square(x)*square(x))
    
print fourthPower(2)
