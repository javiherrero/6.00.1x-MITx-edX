# Desc: Lec 2, Problem 11.
# Author: Javier Herrero Arnanz.

varA='Hola'
varB=10

if (type(varA) == str) or (type(varB) == str):
    print('String involved')
else:
    if (varA == varB):
        print('Equal')
    elif (varA > varB):
        print('Bigger')
    else:
        print('Smaller')
