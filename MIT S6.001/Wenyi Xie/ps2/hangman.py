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

WORDLIST_FILENAME = "words.txt"


def load_words():
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
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    
    for secret_letter in secret_word:
      res = 0
      for guessed in letters_guessed:
        if secret_letter == guessed:
          res = 1
          break
      if res == 0:
        return False
    return True
  



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    current = list()
    for secret_letter in secret_word:
      res = 0
      for guessed in letters_guessed:
        if secret_letter == guessed:
          current.append(secret_letter)
          res = 1
          break
      if res == 0:
        current.append("_ ")
    return "".join(current)




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letter = list()
    for letter in string.ascii_lowercase:
      res = 0
      for guessed in letters_guessed:
        if letter == guessed:
          res = 1
          break
      if res == 0:
        available_letter.append(letter)
    return "".join(available_letter)


    
    

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
    print("Welcome to the game Hangman!")
    len_secret = len(secret_word)
    print("I am thinking of a word that is ", len_secret, " letters long.")
    letters_guessed = list()
    i = 6 #guessing number
    j = 3 #warning number
    k = 0 #number unique letters in secret_word
    res = 0
    fun = get_guessed_word(secret_word, letters_guessed)
    print("You have ", j, " warnings left.")
    while i > 0:
      print("-------------")
      print("You have ", i, " guesses left.")
      available_letters = get_available_letters(letters_guessed)
      print("Available letters: ", available_letters)
      letter = input("Please guess a letter:")
      if letter.isalpha(): #input error exp:&*%12
        letter.lower()
      else:
        if j == 0:
          i = i - 1
        else:
          j = j - 1
        print("Oops! That is not a valid letter. You have {} warnings left:{}".format(j, new_fun))
        continue
      if available_letters.find(letter) == -1: #判断输入的字母在不在可选字母中
        if j == 0:
          i = i - 1
        else:
          j = j - 1
        print("Oops! That is already been guessed. You have {} warnings left:{}".format(j, new_fun))
        continue
      letters_guessed.append(letter)
      new_fun = get_guessed_word(secret_word, letters_guessed) 
      if fun == new_fun: #判断输入的字母是否在secret_word里
        if letter in ('a', 'e', 'i', 'o'):
          i = i - 2
        else:
          i = i - 1
        print("Oops! That letter is not in my word:", new_fun)
      else:
        k = k + 1
        print("Good guess:", new_fun)
      fun = new_fun
      if fun == secret_word: #判断是否完成猜词
        print("Congratulations!")
        Total_score = i * k
        print("Your total score for this game is: ", Total_score)
        res = 1
        break
    if res == 0:
      print("-----------")
      print("Sorry, you ran out of guesses")
      print("Secret word is: ", secret_word)


#secret_word = input()
'''letters_guessed = list(input())
print(get_available_letters(letters_guessed))'''
#hangman(secret_word)


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
    my_word = "".join(my_word.split())
    len_my = len(my_word)
    len_other = len(other_word)
    if len_my != len_other:
      return False
    i = 0
    while i < len_my:
      if my_word[i] != other_word[i] and my_word[i] != '_':
        return False
      elif my_word[i] == '_' and my_word.find(other_word[i]) != -1:
        return False
      i = i + 1
    return True






def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    res = 0
    for word in wordlist:
      if match_with_gaps(my_word, word):
        res = 1
        print(word, end=" ")
    if res == 0:
      print("No matches found")
    print("", end='\n')
    


#my_word = input()
#show_possible_matches(my_word)

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
    print("Welcome to the game Hangman!")
    len_secret = len(secret_word)
    print("I am thinking of a word that is ", len_secret, " letters long.")
    letters_guessed = list()
    i = 6 #guessing number
    j = 3 #warning number
    k = 0 #number unique letters in secret_word
    res = 0
    fun = get_guessed_word(secret_word, letters_guessed)
    print("You have ", j, " warnings left.")
    while i > 0:
      print("-------------")
      print("You have ", i, " guesses left.")
      available_letters = get_available_letters(letters_guessed)
      print("Available letters: ", available_letters)
      letter = input("Please guess a letter:")
      if letter.isalpha(): #input error exp:&*%12
        letter.lower()
      elif letter != '*':
        if j == 0:
          i = i - 1
        else:
          j = j - 1
        print("Oops! That is not a valid letter. You have {} warnings left:{}".format(j, new_fun))
        continue
      if letter == '*':
        print("Possible word matches are: ")
        show_possible_matches(fun)
        continue
      if available_letters.find(letter) == -1: #判断输入的字母在不在可选字母中
        if j == 0:
          i = i - 1
        else:
          j = j - 1
        print("Oops! That is already been guessed. You have {} warnings left:{}".format(j, new_fun))
        continue
      letters_guessed.append(letter)
      new_fun = get_guessed_word(secret_word, letters_guessed) 
      if fun == new_fun: #判断输入的字母是否在secret_word里
        if letter in ('a', 'e', 'i', 'o'):
          i = i - 2
        else:
          i = i - 1
        print("Oops! That letter is not in my word:", new_fun)
      else:
        k = k + 1
        print("Good guess:", new_fun)
      fun = new_fun
      if fun == secret_word: #判断是否完成猜词
        print("Congratulations!")
        Total_score = i * k
        print("Your total score for this game is: ", Total_score)
        res = 1
        break
    if res == 0:
      print("-----------")
      print("Sorry, you ran out of guesses")
      print("Secret word is: ", secret_word)
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
