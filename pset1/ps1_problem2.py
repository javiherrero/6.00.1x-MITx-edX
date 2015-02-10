# Desc: Problem Set 1 - Problem 2 - Counting Bobs.
# Author: Javier Herrero Arnanz.

# String to evaluate.
s = 'azcbobobegghakl'

# Replace b -> bb
s = s.replace('b','bb')

# Count the bobs.
nBobs = s.count('bob',0,len(s))

# Print the result.    
print ('Number of times bob occurs is: ' + str(nBobs))
