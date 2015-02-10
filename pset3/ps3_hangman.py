# Desc: Problem Set 3 - Problem 2 - Hangman game
# Author: Javier Herrero Arnanz.

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist



def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    
    return random.choice(wordlist)



# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    # If a char is not in the guessed letters, the word has not been guessed.
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    # If a char is not in the guessed letters, insert an underscore 
    # in the result string. Otherwise insert the char.
    resStr = ''
    for char in secretWord:
        if char in lettersGuessed:
            resStr += char + ' '
        else:
            resStr += '_ '
    return resStr



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    # Remove all guessed alphabet chars.
    resStr = string.ascii_lowercase
    for char in lettersGuessed:
        resStr = string.replace(resStr,char,'')
    return resStr
  
      

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    # Main variables.
    lettersGuessed = []
    availableLetters = []
    maxMistakes = 8
    mistakesMade = 0
    separator = '--------------------------------------------------'
    
    # Welcome.
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    print(separator) 

    # Initialize available letters list.
    for letter in string.ascii_lowercase:
        availableLetters.append(letter)
    
    ########## Round (main loop). Communication between user and machine. ##########
    while ((mistakesMade < maxMistakes) and (not isWordGuessed(secretWord, lettersGuessed))):
        # Show how many guesses the user has left and the available letters.
        print('You have ' + str(maxMistakes - mistakesMade) + ' guesses left.')
	print('Available letters: ' + getAvailableLetters(lettersGuessed))
	
	# Guess input.
	guess = raw_input('Please guess a letter: ').lower()[0]
	
	# Check if it is a letter and if it is in the available letters 
	# or in the guessed letters.
        if (guess not in string.ascii_lowercase):
            print('Oops! You have entered an invalid letter: '),
        elif (guess in availableLetters):
            lettersGuessed.append(guess)
            availableLetters.remove(guess)
            # Is the letter in the secret word?
            if (guess in secretWord):
                print('Good guess: '),
            else:
                mistakesMade += 1
                print('Oops! That letter is not in my word: '),
        elif (guess in lettersGuessed):
            print('Oops! You\'ve already guessed that letter: '),
        
        print getGuessedWord(secretWord, lettersGuessed)             
        print(separator)
    ################################################################################
    
    # Why did the game finish?
    if (isWordGuessed(secretWord, lettersGuessed)):
        print ('Congratulations, you won!')
    else:
        print ('Sorry, you ran out of guesses. The word was ' + secretWord)



secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
