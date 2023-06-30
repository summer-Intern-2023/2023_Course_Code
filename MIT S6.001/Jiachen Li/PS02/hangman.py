# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

# WORDLIST_FILENAME = "words.txt"
WORDLIST_FILENAME = '/home/mb/2023code/2023codevm/vm/2023python/2023summer/Li_Jiachen/2023Summer-Intern/MIT S6.001/Jiachen Li/PS02/words.txt'


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("[Hangman]: Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("[Hangman]:", len(wordlist), "words loaded.")
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


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean,pantomimeist (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass
    
    

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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print(f"[Hangman]: The word has {len(secret_word)} letters.")
    print("[Hangman]: You have 6 times to guesses.")
    
    attempts = 6
    guesses = ""
    
    while attempts > 0:
      failed = 0
      for char in secret_word:
        if char in guesses:
            print(char, end=' ')
        else:
            print('_', end=' ')
            failed += 1

      if failed == 0:
        print('\n[Hangman]: Congratulations! You guessed the word correctly!')
        break

      guess = input('\n\n[Hangman]: Enter a letter: ')
      guesses += guess

      if guess not in secret_word:
          attempts -= 1
          print('[Hangman]: Wrong guess! You have', attempts, 'attempts left.')

      if attempts == 0:
          print('[Hangman]: You ran out of attempts. The word was %', secret_word, "% .")


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    
    if len(my_word) != len(other_word):
        return False
    
    for i in range(len(my_word)):
        if my_word[i] != '_' and my_word[i] != other_word[i]:
            return False
    
    return True
    
    # FILL IN YOUR CODE HERE AND DELETE "pass"


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matches = []
    
    for word in wordlist:
        if len(word) == len(my_word):
            match = True
            for i in range(len(word)):
                if my_word[i] != '_' and my_word[i] != word[i]:
                    match = False
                    break
            if match:
                matches.append(word)
    
    print("Possible matches: ", matches)




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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print(f"[Hangman]: The word has {len(secret_word)} letters.")
    print("[Hangman]: You have 6 times to guesses.")
    
    attempts = 6
    guesses = ""
    
    while attempts > 0:
      failed = 0
      for char in secret_word:
        if char in guesses:
            print(char, end=' ')
        else:
            print('_', end=' ')
            failed += 1

      if failed == 0:
        print('\n[Hangman]: Congratulations! You guessed the word correctly!')
        break

      guess = input('\n\n[Hangman]: Enter a letter: ')
      guesses += guess

      if guess not in secret_word:
          attempts -= 1
          print('[Hangman]: Wrong guess! You have', attempts, 'attempts left.')

      if attempts == 0:
          print('[Hangman]: You ran out of attempts. The word was %', secret_word, "% .")


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
