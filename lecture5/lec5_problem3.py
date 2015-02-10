# Desc: Lec 5, Problem 3.
# Author: Javier Herrero Arnanz.

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    if (exp == 0):
        return 1
    elif ((exp > 0) and (exp%2 == 1)):
        return (base * recurPowerNew(base,exp-1))
    elif ((exp > 0) and (exp%2 == 0)):
        return (recurPowerNew(base*base,exp/2))

print recurPowerNew(2,5)
