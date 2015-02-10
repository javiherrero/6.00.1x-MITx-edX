# Desc: Lec 3, Problem 9.
# Author: Javier Herrero Arnanz.

# Initial range [0, 100).
start=0
end=100

# Enter secret number.
number=-1
while (number not in range(start,end)):
    number = int(raw_input('Please think of a number between ' + str(start) + ' and ' + str(end) + '! '))
    if (number not in range(start,end)):  
        # Out of the range.
        print('The number should be in the range [' + str(start) + ', ' + str(end) + ')')

# Number search.
found = False
while (not found):
    # Ask the user.
    half=(start+end)/2
    print('')
    print('Is your secret number ' + str(half) + '? ')
    print('Enter \'h\' to indicate the guess is too high.'),
    print('Enter \'l\' to indicate the guess is too low.'),
    answer = raw_input('Enter \'c\' to indicate I guessed correctly. ')
    if (answer not in ['h','l','c']):
        print('Sorry, I did not understand your input.')
    else:
        if (answer == 'h'):
            # Too high
            end = half
        elif (answer == 'l'):
            # Too low
            start = half
        elif (answer == 'c'):
            # Correct
            if (half == number):
                found = True
                print('Game over. Your secret number was: ' + str(half))
            else:
                print('Do not be a liar. That is not your secret number')
