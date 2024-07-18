"""
def arrow(my_char, max_length):
    arr = ''
    a = 1
    for i in range(max_length):
        for j in range(a):
            arr += my_char + ' '
        arr = arr.rstrip()
        arr += '\n'
        a += 1
    a -= 1
    for i in range(a - 1):
        for j in range(a - 1):
            arr += my_char + ' '
        arr += '\n'
        a -= 1
    return arr
"""


#The function I wrote above ↑ and the function upgraded by chatgpt below ↓ and upgraded by me to remove the space at the end of a line
def arrow(my_char, max_length):
    arr = ''
    for i in range(1, max_length + 1):
        arr += ((my_char + ' ') * i)
        arr = arr.rstrip() + '\n'
    for i in range(max_length - 1, 0, -1):
        arr += ((my_char + ' ') * i)
        arr = arr.rstrip() + '\n'
    return arr


# בדיקת הדוגמה
print(arrow('*', 10))
