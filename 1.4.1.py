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

try_char = input("Guess a letter: ").upper()
word = input("Please enter a word: ")
a = '_'
b = ((a + ' ') * (len(word) - 1) + "_")
print(b)