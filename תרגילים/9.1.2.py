import re

path = input('enter file path:\n')
select_action = input('Enter a task from:\nsort, rev, last:\n')


def sort_file(file):
    body_file = list(set(re.split(r'[ \n]', file.read())))
    return sorted(body_file)


def rev_file(file):
    body_file = ''
    for line in file:
        body_file += line[::-1] + '\n'
    return body_file


def last_file(file):
    lines = int(input('enter number lines:\n'))
    body_file = file.readlines()
    return ''.join(body_file[lines *(-1):])


def open_file(path):
    file = open(path, 'r')
    return file


if select_action == 'sort':
    print(sort_file(open_file(path)))
elif select_action == 'rev':
    print(rev_file(open_file(path)))
elif select_action == 'last':
    print(last_file(open_file(path)))
