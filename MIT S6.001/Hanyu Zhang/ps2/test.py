secret_word = "apple"
letters_guessed = ["a", "p", "l"]
available_letters = ""
all_letters = "abcdefghijklmnopqrstuvwxyz"
for letter in all_letters :
    if letter in letters_guessed :
        continue
    else :
        available_letters = available_letters + letter