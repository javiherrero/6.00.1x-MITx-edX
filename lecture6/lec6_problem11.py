# Desc: Lec 6, Problem 11.
# Author: Javier Herrero Arnanz.

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    big = ''
    length = 0
    
    if (len(aDict) == 0):
        return
    else:
        for k in aDict.keys():
            if (len(aDict[k]) >= length):
                big = k
                length = len(aDict[k])
        return big

print biggest({'a': [6, 0, 13, 3, 15], 'c': [], 'b': [0, 5, 12]})
