def filter_teens(a=13, b=13, c=13):
    return fix_age(a) + fix_age(b) + fix_age(c)


def fix_age(age):
    if 13 <= age <= 19 and age != 15 and age != 16:
        return 0
    return age


print(filter_teens())
