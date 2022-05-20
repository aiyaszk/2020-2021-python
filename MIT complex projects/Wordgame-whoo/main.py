'''
Dealing the hands:
A player is dealt a hand of n letters chosen at random (assume n=7 for now).

The player arranges the hand into as many words as they want out of the letters, using each letter at most once.

Some letters may remain unused (these won't be scored).

Scoring:
The score for the hand is the sum of the scores for each word formed.

The score for a word is the sum of the points for letters in the word, multiplied by the length of the word, plus 50 points if all n letters are used on the first word created.

Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, D is worth 2, E is worth 1, and so on. The dictionary SCRABBLE_LETTER_VALUES that maps each lowercase letter to its Scrabble letter value.

For example, 'weed' would be worth 32 points ((4+1+1+2) for the four letters, then multiply by len('weed') to get (4+1+1+2)*4 = 32).

As another example, if n=7 and you make the word 'waybill' on the first try, it would be worth 155 points (the base score for 'waybill' is (4+1+4+3+1+1+1)*7=105, plus an additional 50 point bonus for using all n letters).

'''

# The 6.00 Word Game

import random

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    
    b=0
    for i in range(len(word)):
      b+=SCRABBLE_LETTER_VALUES[word[i]]
    b=b*len(word)
    if n==len(word):
      b=b+50
    return b



#
# Problem #2:
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    a=0
    for j in range(len(word)):
      if hand[word[j]]==0:
        a=1
    
    for i in range(len(word)):
      if word[i] in hand and a==0:
        hand[word[i]]-=1
    return hand

#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    displayHand(hand)
    word=str(word)
    if set(word) & set(displayHand(hand)) & set(wordList) == set(word):
        return True
    else:
        return False


#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    a=0
    b=hand.values()
    b=list(b)
    
    for i in range(len(b)):
        a+=b[i]
    return a


def displayHandd(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    a=''
    for letter in hand.keys():
        for j in range(hand[letter]):
             a+=(letter+' ')       # print all on the same line
                           # print an empty line
    return a
    
def displayHand2(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    a=''
    for letter in hand.keys():
        for j in range(hand[letter]):
             a+=(letter)       # print all on the same line
                           # print an empty line
    return a
    
def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    
        # Display the hand
        
        # Ask user for input
        
        # If the input is a single period:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not a single period):
        
            # If the word is not valid:
            
                # Reject invalid word (print a message followed by a blank line)

            # Otherwise (the word is valid):

                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                
                # Update the hand 
                

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    Tpnt=0
    cur_hand=displayHandd(hand)
    curhand2=displayHand2(hand)
    z=displayHandd(hand)
    lcurhand2=list(curhand2)
    while True:
      pnt=0
      print('Current Hand:',z)
      input1=input('Enter word, or a "." to indicate that you are finished: ')
      if input1 == '.' :
        print('Goodbye! Total score:',Tpnt,'points.')
        break
      if input1 in wordList:              
        for i in range(len(input1)):
          pnt+=SCRABBLE_LETTER_VALUES[input1[i]]
        pnt*=len(input1)
        if n==len(input1):
          pnt+=50
        #return pnt
        Tpnt+=pnt



        for j in range (len(input1)): 
          if input1[j] in lcurhand2:
            lcurhand2.remove(str(input1[j]))


        z=''
        for t in range(len(lcurhand2)):
          z+=lcurhand2[t]+' '

        print('"',input1,'"','earned',pnt,'points. Total:',Tpnt,'points')
        
      else:
        print('Invalid word, please try again.')

      
      print()
      if z=='':
        print('Run out of letters. Total score:',Tpnt,'points.')
        break
# Problem #5: Playing a game
# 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    
    

    clock=0
    while True:
      codeput=input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
      
      if codeput=='n':
        clock+=1
        hand=dealHand(HAND_SIZE)
        print()
        playHand(hand, wordList, HAND_SIZE)
        print()
      elif codeput=='r' and clock==0:
        print("You have not played a hand yet. Please play a new hand first!")
      elif codeput=='r':
        clock+=1
        print()
        playHand(hand, wordList, HAND_SIZE)
        print()
      elif codeput=='e':
        break
      else:
        print('Invalid command.')
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


#alternative playgame to make the word game between you and the computer
'''

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
    solveE=0
    clock=0
    
    while True:
      if solveE==0:
        codeput=input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')           
      if codeput=='n' or solveE==1:
        clock+=1
        print()
        comput=input('Enter u to have yourself play, c to have the computer play: ')
        if comput=='u':          
          hand=dealHand(HAND_SIZE)
          print()
          playHand(hand, wordList, HAND_SIZE)
          print()
          solveE=0
        elif comput=='c':
          hand=dealHand(HAND_SIZE)
          compPlayHand(hand, wordList, HAND_SIZE)
          solveE=0
        else:
          print('Invalid command.')
          solveE=1
      
          
      elif codeput=='r' and clock==0:
        print("You have not played a hand yet. Please play a new hand first!")

      elif codeput=='r' or solveE==1:
        clock+=1
        print()
        comput=input('Enter u to have yourself play, c to have the computer play: ')
        if comput=='u':          
          print()
          playHand(hand, wordList, HAND_SIZE)
          print()
          solveE=0
        elif comput=='c':
          compPlayHand(hand, wordList, HAND_SIZE)
          solveE=0
        else:
          print('Invalid command.')
          solveE=1
        
      elif codeput=='e':
        break
      else:
        print('Invalid command.')

'''
