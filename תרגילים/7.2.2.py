def numbers_letters_count(my_str: str):
    num_len = 0
    else_len = 0
    for char in my_str:
        if char.isdigit():
            num_len += 1
        else:
            else_len += 1
    return [num_len, else_len]