def mult_tuple(tuple1, tuple2):
    pair = ()
    for item1 in tuple1:
        for item2 in tuple2:
            pair += ((item1 ,item2, ), )
    for item1 in tuple1:
        for item2 in tuple2:
            pair += ((item2 ,item1, ), )

    """
    אם הסדר לא חשוב
    for item1 in tuple1:
        for item2 in tuple2:
            pair += ((item1 ,item2, ), )
            pair += ((item2 ,item1, ), )
    """
    return pair

first_tuple = (1, 2)
second_tuple = (4, 5)
print(mult_tuple(first_tuple, second_tuple))