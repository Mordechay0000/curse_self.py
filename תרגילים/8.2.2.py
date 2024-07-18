def sort_to_value_in_tupe(tuple: tuple):
    return tuple[1]


def sort_prices(list_of_tuples: list):
    return sorted(list_of_tuples, key=sort_to_value_in_tupe, reverse=True)

products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
print(sort_prices(products))