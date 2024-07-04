def extend_list_x(list_x, list_y):
    list_x[:0] = list_y
    list_x = list_x
    return list_x

print(extend_list_x([4, 5, 6], [1, 2, 3]))