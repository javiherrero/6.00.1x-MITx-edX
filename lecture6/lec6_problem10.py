# Desc: Lec 6, Problem 10.
# Author: Javier Herrero Arnanz.

def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    for k in aDict:
        count += len(aDict[k])
    return count
    
print howMany({ 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']})
