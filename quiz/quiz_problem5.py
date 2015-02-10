# Desc: Quiz - Problem 5.
# Author: Javier Herrero Arnanz.

def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    
    # Alternate the elements of each string.
    laceStr = ''
    minLen = min(len(s1),len(s2))
    for i in range(0,minLen):
        laceStr += s1[i] + s2[i]
    
    # Add the remaining elements of the longer string.
    if (len(s1) > len(s2)):
        laceStr += s1[minLen:]
    elif (len(s2) > len(s1)):
        laceStr += s2[minLen:]
        
    return laceStr
    
print laceStrings('abcd','efghi')
