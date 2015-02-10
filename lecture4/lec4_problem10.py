# Desc: Lec 4, Problem 10.
# Author: Javier Herrero Arnanz.

def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    if (char == 'a')or(char == 'A')or(char == 'e')or(char == 'E')or(char == 'i')or(char == 'I')or(char == 'o')or(char == 'O')or(char == 'u')or(char == 'U'):
        return True
    else:
        return False

print isVowel('a')
print isVowel('b')
