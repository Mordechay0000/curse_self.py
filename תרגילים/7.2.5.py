def sequence_del(my_str):
    new_str_list = []
    for i in range(len(my_str) - 1):
        if my_str[i] != my_str[i+1]:
            new_str_list.append(my_str[i])
    new_str_list.append(my_str[-1])
    return ''.join(new_str_list)
