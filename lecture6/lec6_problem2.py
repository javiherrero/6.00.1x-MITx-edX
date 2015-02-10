# Desc: Lec 6, Problem 2.
# Author: Javier Herrero Arnanz.

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    return aTup[0::2]
    
print oddTuples(('I', 'am', 'a', 'test', 'tuple'))
