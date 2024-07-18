def inverse_dict(my_dict):
    inverse_dict = {}
    for key in my_dict.keys():
        if my_dict[key] in inverse_dict.keys() and type(inverse_dict[my_dict[key]]) == list:
            inverse_dict[my_dict[key]].append(key)
        else:
            inverse_dict[my_dict[key]] = [key]
        print(my_dict[key])
    return inverse_dict

print(inverse_dict({'I': 3, 'love': 3, 'self.py!': 2}))