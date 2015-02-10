# Desc: Problem Set 1 - Problem 3 - Alphabetical Substrings.
# Author: Javier Herrero Arnanz.

# String to evaluate.
s = 'azcbobobegghakl'

# Search the longest alphabetical substring.
alphStr = ''
currentStr = ''
for i in range(len(s)):
        currentStr += s[i]
        if ((i == len(s)-1) or (s[i] > s[i + 1])):
            # Check alphabetical substring.
            if (len(currentStr) > len(alphStr)):
                alphStr = currentStr
            currentStr = ''            

# Print the result.       
print ('Longest substring in alphabetical order is: ' + alphStr)
