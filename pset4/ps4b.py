# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Modified by: Sarina Canelake <sarina>
#
# Student: Javier Herrero Arnanz.

from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    
    def isWordInHand(hand, word):
        """
        Returns True if word is entirely composed of letters in the hand. 
        Otherwise, returns False.

        Does not mutate hand.

        hand: dictionary (string -> int)   
        word: string
        """
        
        freqDict = getFrequencyDict(word)
        for letter in freqDict:
            if (freqDict[letter] > hand.get(letter, 0)):
                return False
        return True
    
    
    # Create a new variable to store the maximum score seen so far (initially 0).
    maxScore = 0

    # Create a new variable to store the best word seen so far (initially None).  
    bestWord = None

    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if(isWordInHand(hand, word)):
            # Find out how much making that word is worth
            wordScore = getWordScore(word, n)
            
            # If the score for that word is higher than your best score
            if (wordScore > maxScore):
                # Update your best score, and best word accordingly
                maxScore = wordScore
                bestWord = word

    # Return the best word you found.
    return bestWord



#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    
    # Keep track of the total score.
    totalScore = 0
    
    ########### As long as there are still letters left in the hand: ###########
    while (calculateHandlen(hand) > 0):
        # Display the hand.
        print ('Current Hand: '),
        displayHand(hand)
        
        # The computer chooses a word.
        word = compChooseWord(hand, wordList, n)
        if (word == None):
            # Computer has exhausted its possible choices.
            break
        
        # Tell the computer how many points the word earned, and the updated total score, in one line followed by a blank line.
        wordScore = getWordScore(word,n)
        totalScore += wordScore
        print('"' + word + '" earned '+str(wordScore)+' points. Total: '+str(totalScore)+' points')
        print('')
                
        # Update the hand. 
        hand = updateHand(hand,word)
    ############################################################################
    
    # Game is over, tell the computer the total score.
    print('Total score: '+str(totalScore)+' points.')
    
    
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    
    # The hand is initially empty
    hand = {}
        
    # Play a hand as far as the user finishes the game.
    finish = False
    while (not finish):        
        # Ask user for input.
        uInput1 = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ').lower()
    
        # Check user input.
        if ((uInput1 == 'n') or (uInput1 == 'r')):
            if (uInput1 == 'n'):
                # New hand.
                hand = dealHand(HAND_SIZE)
            elif ((uInput1 == 'r') and (len(hand) == 0)):
                # Is impossible to replay the last hand.
                print('You have not played a hand yet. Please play a new hand first!')
                continue
            
            # Who plays?
            uInput2 = ''
            while ((uInput2 != 'u') and (uInput2 != 'c')):
                uInput2 = raw_input('Enter u to have yourself play, c to have the computer play: ').lower()
                if (uInput2 == 'u'):
                    # The user plays.
                    playHand(hand,wordList,HAND_SIZE)   
                elif (uInput2 == 'c'):
                    #The computer plays.
                    compPlayHand(hand,wordList,HAND_SIZE)
                else:
                    print('Invalid command.')
        elif (uInput1 == 'e'):
            # End game.
            finish = True
        else:
            print('Invalid command.')

        
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
