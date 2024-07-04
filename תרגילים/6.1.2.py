def shift_left(my_list):
    # הנחת היסוד היא שהרשימה באורך 3
    return [my_list[1], my_list[2], my_list[0]]

print(shift_left([1, 2, 3, 4, 5]))