# 6.00x Problem Set 6.
#
# Part 2 - RECURSION
#
# Student: Javier Herrero Arnanz.

import string

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    assert (len(aStr) > 0), "The string is empty"
    
    if (len(aStr) == 1): # Base case.
        return aStr
    else: # Recursive case.
        return reverseString(aStr[1:]) + aStr[0]


#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    assert (len(x) > 0), "The string x is empty"
    assert (len(word) > 0), "The string word is empty"
    
    if (len(x) == 1): # Base case.
        if (x in word):
            return True
        else: 
            return False
    else:
        if (x[0] in word): # Recursive case.
            i = string.find(word,x[0])  
            return x_ian(x[1:], word[i+1:])
        else: # Base case.
            return False
        
        
#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    assert (lineLength > 0), "The lineLenght should be greater than zero"
    
    words = text.split()
    if  ((len(text) <= lineLength) or (len(words) == 1)): # Base case.
        return text
    else:
        newLine = ''
        while (len(newLine) < lineLength):
            newLine += words[0] + ' '
            words.pop(0)
            
        if (len(words) > 0): # Recursive case.
            return newLine + "\n" + insertNewlines(' '.join(words), lineLength)
        else: # Base case.
            return newLine
