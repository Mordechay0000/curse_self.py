SAVE_FILE_NAME = 'found.txt'
def who_is_missing(file_name):
    missing_number = 0
    number_list = []
    with open(file_name) as f:
        number_list = f.read().split(',')
    number_list.sort()
    last_num = int(number_list[0])
    for number in number_list[1:]:
        if int(number) != int(last_num) + 1:
            missing_number = int(number) - 1
        last_num = int(number)
    with open(SAVE_FILE_NAME, 'w') as f:
        f.write(str(missing_number))
    return missing_number