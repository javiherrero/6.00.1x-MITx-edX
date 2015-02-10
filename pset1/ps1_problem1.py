# Desc: Problem Set 1 - Problem 1 - Counting Vowels
# Author: Javier Herrero Arnanz.

# String to evaluate.
s ='hiugawea'

# Count the vowels.
nVowels = 0
for letter in ('aeiou'):
    nVowels += s.count(letter,0,len(s))

# Print the result.    
print ('Number of vowels: ' + str(nVowels))
