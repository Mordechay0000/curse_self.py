import random

HANGMAN_ASCII_ART = """
Welcome to the game Hangman
  _    _
 | |  | |
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
 |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                      __/ |
                     |___/
"""
MAX_TRIES = 6

one = """
    x-------x
"""
two = """
    x-------x
    |
    |
    |
    |
    |
"""
twee = """
    x-------x
    |       |
    |       0
    |
    |
    |
"""
four = """
    x-------x
    |       |
    |       0
    |       |
    |
    |
"""
five = """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """
six = """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
"""
seven = """
     x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
"""




def is_valid_input(letter_guessed):
    if (not letter_guessed.isalpha()) or len(letter_guessed) > 1:
        return False
    else:
        return True


def check_valid_input(letter_guessed, old_letters_guessed):
    return is_valid_input(letter_guessed) and not (letter_guessed in old_letters_guessed)


def try_update_letter_guessed(letter_guessed, old_letters_guessed: list):
    letter_guessed = letter_guessed.lower()
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print('X')
        print(' -> '.join(sorted(old_letters_guessed)))
        return False

old_letters = ['a', 'p', 'c', 'f']
print(try_update_letter_guessed('A', old_letters))
print(try_update_letter_guessed('s', old_letters))
print(old_letters)
print(try_update_letter_guessed('$', old_letters))
print(try_update_letter_guessed('d', old_letters))
print(old_letters)

"""
try_char = input("Guess a letter: ").lower()
word = input("Please enter a word: ")
a = '_'
b = ((a + ' ') * (len(word) - 1) + "_")
print(b)
"""
