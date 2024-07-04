def longest(my_list: list):
    my_list.sort(key=len, reverse=True)
    return my_list[0]
