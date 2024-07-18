def is_greater(my_list, n):
    new_list = []
    for element in my_list:
        if element > n:
            new_list.append(element)
    return new_list