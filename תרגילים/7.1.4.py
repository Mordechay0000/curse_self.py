def squared_numbers(start, stop):
    squared_numbers_list = []
    while start <= stop:
        squared_numbers_list.append(start * start)
        start += 1
    return squared_numbers_list

print(squared_numbers(-3, 3))