def count_chars(my_str):
    dic = {}
    for letter in my_str:
        if letter == ' ':
            continue
        dic[letter] = dic.get(letter, 0) + 1
    return dic

print(count_chars("abra cadabra"))