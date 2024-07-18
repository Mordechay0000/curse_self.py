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

HANGMAN_PHOTOS = {'0': """x-------x""",
                  '1': """
    x-------x
    |
    |
    |
    |
    |
""",
                  '2': """
    x-------x
    |       |
    |       0
    |
    |
    |
""",
                  '3': """
    x-------x
    |       |
    |       0
    |       |
    |
    |
""",
                  '4': """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """,
                  '5': """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
""",
                  '6': """
     x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
"""}

MAX_TRIES = 6


def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[str(num_of_tries)])


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


def show_hidden_word(secret_word, old_letters_guessed):
    display_word = ''
    for letter in secret_word:
        if letter in old_letters_guessed:
            display_word += (letter + ' ')
        else:
            display_word += ('_ ')
    return display_word.rstrip()


def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True

def choose_word(file_path, index):
    index -= 1
    file = open(file_path, 'r')
    word_list = file.read().split(' ')
    file.close()
    num = len(list(set(word_list)))
    while index >= len(word_list):
        index -= len(word_list)
    return num, word_list[index]

print(choose_word('test_file.txt', 14))


"""
try_char = input("Guess a letter: ").lower()
word = input("Please enter a word: ")
a = '_'
b = ((a + ' ') * (len(word) - 1) + "_")
print(b)
"""
