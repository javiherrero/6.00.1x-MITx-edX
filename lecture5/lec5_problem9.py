 Desc: Lec 5, Problem 9.
# Author: Javier Herrero Arnanz.

def semordnilapWrapper(str1, str2):
    
    def semordnilap(str1, str2):
        '''
        str1: a string
        str2: a string
    
        returns: True if str1 and str2 are semordnilap;
                False otherwise.
        '''
        if (len(str1) != len(str2)):
            return False
        elif (len(str1) == 1):
            return str1 == str2
        else:
            return ((str1[-1] == str2[0]) and (semordnilap(str1[:-1],str2[1:])))
    
    
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)
    
print semordnilapWrapper('dog', 'god')
