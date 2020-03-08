# Problem Set 2, hangman.py
# Name: Ali Kalaycı

# This problem was taken from MIT 6.0001 Fall 2016 course
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/ 
# Function names and instructions to write functions are given.
# I wrote code according to them.

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions

import random
import string



def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open('words.txt', 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

# I started to write from here.

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True    


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    secretw= ''
    for char in secret_word:
        if not char in letters_guessed:
            secretw += '_ '
        else:
            secretw += char
    
    return secretw
       

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    availablel=''
    for char in string.ascii_lowercase:
        if char not in letters_guessed:
            availablel += char
    
    return availablel
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is {} letters long.'.format(len(secret_word)))
    print('You have 6 guesses and 3 warnings. Be careful')
    g=6
    w=3
    letters_guessed= []
    while True:
        print('------------------------------------') 
        print('guesses left', g)
        print('warnings left',w)
        print('available letters',get_available_letters(letters_guessed))
        gletter= input('enter one letter, if you write longer it will take first one\n ')[0]
        if gletter.isalpha():
            if gletter.islower():
                if gletter not in letters_guessed:
                    letters_guessed.append(gletter)
                    guess= get_guessed_word(secret_word, letters_guessed)
                    if not guess.find(gletter)== -1:
                        print('good guess',guess)
                    else:
                        if gletter in 'aeiou':
                            print('Oops! That letter is not in my word ',gletter)
                            print('Guessed letter is vovel so -2')
                            print('please guess a letter', guess)
                            g -= 2
                        else:
                            print('Oops! That letter is not in my word ', gletter)
                            g -= 1
                            print('please guess a letter', guess)
                
                else:
                    print('have already guessed')
                    w-=1
            else:
                w -= 1
                
        else:
            print('please guess letter')
            w-=1
        if w ==0:
            print('You now have no warnings left so you lose one guess')
            w = 3
            g -= 1
        
        print('***********************************')
            
        if is_word_guessed(secret_word, letters_guessed):
            unique_letters_in_secret_word = []
            for char in secret_word:
                if char not in unique_letters_in_secret_word:
                    unique_letters_in_secret_word.append(char)
            
            print('Congratulations, you won!')
            print('Your total score for this game is {}'.format(g * len(unique_letters_in_secret_word)))
            break
        
        if g== 0:
            print('Sorry, you ran out of guesses. The word was',secret_word)
            break
            
## Hangman with hints    
    
def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    myword= my_word.replace(' ','')
    if len(myword)==len(other_word):
        for mi in range(len(myword)):
            if myword[mi] != '_':
                if myword[mi] != other_word[mi]:
                    return False
                otherw= ''.join(sorted(other_word))
                a= myword.count(myword[mi])
                c= otherw.count(myword[mi])
                if a!=c :
                    return False
        return True
                
    else:
        return False
            



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    matchedw = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matchedw.append(word)
    
    if len(matchedw) > 0:
        for word in matchedw:
            print(word, end=' ')
    else:
        print('No matches found')


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is {} letters long.'.format(len(secret_word)))
    print('You have 6 guesses and 3 warnings. Be careful')
    g=6
    w=3
    letters_guessed= []
    while True:
        print('------------------------------------') 
        print('guesses left', g)
        print('warnings left',w)
        print('available letters',get_available_letters(letters_guessed))
        gletter= input('enter one letter, if you write longer it will take first one\n, (if you put * it will give hint )')[0]
        if gletter == '*':
            my_word = get_guessed_word(secret_word, letters_guessed)
            print(show_possible_matches(my_word))
            continue
        if gletter.isalpha():
            if gletter.islower():
                if gletter not in letters_guessed:
                    letters_guessed.append(gletter)
                    guess= get_guessed_word(secret_word, letters_guessed)
                    if not guess.find(gletter)== -1:
                        print('good guess',guess)
                    else:
                        if gletter in 'aeiou':
                            print('Oops! That letter is not in my word ',gletter)
                            print('Guessed letter is vovel so -2')
                            print('please guess a letter', guess)
                            g -= 2
                        else:
                            print('Oops! That letter is not in my word ', gletter)
                            g -= 1
                            print('please guess a letter', guess)
                
                else:
                    print('have already guessed')
                    w-=1
            else:
                w -= 1
                
        else:
            print('please guess letter')
            w-=1
        if w ==0:
            print('You now have no warnings left so you lose one guess')
            w = 3
            g -= 1
        
        print('***********************************')
            
        if is_word_guessed(secret_word, letters_guessed):
            unique_letters_in_secret_word = []
            for char in secret_word:
                if char not in unique_letters_in_secret_word:
                    unique_letters_in_secret_word.append(char)
            
            print('Congratulations, you won!')
            print('Your total score for this game is {}'.format(g * len(unique_letters_in_secret_word)))
            break
        
        if g== 0:
            print('Sorry, you ran out of guesses. The word was',secret_word)
            break

# To test part 2, comment out the pass line above and
# uncomment the following two lines.
    
#secret_word = choose_word(wordlist)
#hangman(secret_word)

###############
    
# To test part 3 re-comment out the above lines and 
# uncomment the following two lines. 
    
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)
