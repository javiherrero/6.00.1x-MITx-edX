# Desc: Quiz - Problem 6.
# Author: Javier Herrero Arnanz.

def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    
    def helpLaceStrings(s1, s2, out):
        """
        Helper function to lace the strings recursively.
        
        s1, s2: Strings to lace.
        out: String that has been laced.
        """
        
        if s1 == '':
            return (out + s2)
        if s2 == '':
            return (out + s1)
        else:
            return helpLaceStrings(s1[1:], s2[1:], out + s1[0] + s2[0])
    
    return helpLaceStrings(s1, s2, '')
    
print laceStringsRecur('abcd','efghi')
