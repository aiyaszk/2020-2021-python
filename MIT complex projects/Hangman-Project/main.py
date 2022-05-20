'''
Hangman game, a user is allowed 8 guesses. Make sure to remind the user of how many guesses s/he has left after each round. Assume that players will only ever submit one character at a time (A-Z).

A user loses a guess only when s/he guesses incorrectly.

If the user guesses the same letter twice, do not take away a guess - instead, print a message letting them know they've already guessed that letter and ask them to try again.

The game should end when the user constructs the full word or runs out of guesses. If the player runs out of guesses (s/he "loses"), reveal the word to the user when the game ends.
'''


import random
import string

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
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    if set(secretWord) & set(lettersGuessed)==set(secretWord):
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secretWord = list(secretWord)
    a = "_" * len(secretWord)
    a = list(a)

    for i in range(len(secretWord)):
      for j in range(len(lettersGuessed)):
        if secretWord[i] == lettersGuessed[j]:
          a[i]=secretWord[i]
    
    b=""
    for e in range(len(a)):
      b+=a[e]
    return b



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    a_str = "abcdefghijklmnopqrstuvwxyz"
    a_list = list(a_str) 
    
    b_list = lettersGuessed
    
    for element in b_list:
        if element in a_list:
            a_list.remove(element)
    a_print = ""
    for i in a_list:
        a_print += i
    return a_print
    

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
    print("Welcome to the game Hangman!")

    print("I am thinking of a word that is", len(secretWord), "letters long.")
    print('-----------')
    
    a_str = "abcdefghijklmnopqrstuvwxyz"
    a_list = list(a_str)
    print("You have 8 guesses left.")
    print("Available letters: abcdefghijklmnopqrstuvwxyz")
    guessleft=8
    b=""
    a = "_" * len(secretWord)
    a = list(a)
    q=0
    f=[]
    while q==0:
      a1=0
      z=0
      u=0
      guess=input('Please guess a letter: ')
      f+=guess
      list(f)
      
      
      b_list = guess
      
      for element in b_list:
        if element in a_list:
          a_list.remove(element)
  
      a_print = ""
      for i in a_list:
        a_print += i
      
      o = list(secretWord)


      
      for i in range(len(o)):
        if o[i] == guess:
          a[i]=o[i]
          z=1


      for y in range(len(f)):
        if f[y]==guess:
          a1+=1

        
      if a1>1:
        print('Oops! You\'ve already guessed that letter:',b)
        u=1
            
      b=""
      for e in range(len(secretWord)):
        b+=a[e]
      

      if z==1 and u==0:
        print("Good guess:",b)     
               




      if z!=1 and u==0:        
        print('Oops! That letter is not in my word:',b)
        guessleft-=1
        
      
      print('-----------')
      if str(b)==str(secretWord):
        print('Congratulations, you won!')
        q=1
        break
      if guessleft==0:
        print('Sorry, you ran out of guesses. The word was', secretWord+'.' )
        q=1
        break      

      print("You have",guessleft,"guesses left.")  
      print("Available letters:", a_print)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
