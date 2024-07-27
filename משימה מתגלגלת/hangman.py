import os
import random
from enum import Enum

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

HANGMAN_PHOTOS = {
                  '0': """
    x-------x





""",
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

from enum import Enum

class FileError(Enum):
    FILE_NOT_FOUND = "File not found"
    INVALID_FILE_FORMAT = "Invalid file format"

def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[str(num_of_tries)])


def clear_screen():
    os.system(('cls' if os.name == 'nt' else 'clear') if os.getenv('TERM') else '')


def is_valid_input(letter_guessed):
    if (not letter_guessed.isalpha()) or len(letter_guessed) > 1:
        return False
    else:
        return True


def check_valid_input(letter_guessed, old_letters_guessed):
    return is_valid_input(letter_guessed) and not (letter_guessed in old_letters_guessed)


def try_update_letter_guessed(letter_guessed, old_letters_guessed: list):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    elif not check_valid_input(letter_guessed, old_letters_guessed):
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
    print(display_word.rstrip())


def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True


def choose_word(file_path, index):
    try:
        index -= 1
        file = open(file_path, 'r')
        word_list = file.read().split(' ')
        file.close()
        num = len(list(set(word_list)))
        while index >= len(word_list):
            index -= len(word_list)
        return word_list[index]
    except FileNotFoundError:
        print('שגיאה: הקובץ לא נמצא')
        return FileError.FILE_NOT_FOUND
    except Exception:
        print('שגיאה: פורמט הקובץ לא תקין')
        return FileError.INVALID_FILE_FORMAT


def is_exit():
    while True:
        is_next = input('Would you like to try again? (y/n)').lower()
        if is_next == 'n':
            exit(0)
        elif is_next == 'y':
            break


def main():
    while True:
        num_of_tries = 0
        old_letters_guessed = []

        secret_word = ''
        while secret_word == '' or secret_word == FileError.FILE_NOT_FOUND or secret_word == FileError.INVALID_FILE_FORMAT:
            print('')
            path = input('Enter a file path: ')
            index = ''
            while not index.isdigit():
                index = input('Enter a index of the word: ')
                if not index.isdigit():
                    print('הערך שהוזן אינו מספר...')
            index = int(index)
            clear_screen()
            secret_word = choose_word(path, index)

        print(HANGMAN_ASCII_ART)
        print('מספר נסיונות מרבי: ' + str(MAX_TRIES))
        print('')
        print_hangman(num_of_tries)
        print('')

        while not check_win(secret_word, old_letters_guessed) and num_of_tries < MAX_TRIES:
            char = input("Guess a letter: ").lower()
            clear_screen()

            status = try_update_letter_guessed(char, old_letters_guessed)

            if status and char not in secret_word:
                num_of_tries += 1

            print_hangman(num_of_tries)
            show_hidden_word(secret_word, old_letters_guessed)
            print('')

        if check_win(secret_word, old_letters_guessed):
            print('Nice, you won!👌')
            print('Number of wrong guesses: ' + str(num_of_tries))
            print('Try again to see if you are lucky today.🔮')
            print('')
            is_exit()
        if num_of_tries >= MAX_TRIES:
            print('Sorry, you lost!')
            print('Try again, you might get lucky.')
            print('')
            is_exit()

        print('')


if __name__ == '__main__':
    main()
