def chocolate_maker(small, big, x):
    small = small * 1
    big = big

    from_bigs = x // 5
    from_smalls = x % 5
    if from_bigs <= big:
        if from_smalls <= small:
            return True
    if small >= x:
        return True
    elif (big * 5) + small >= x:
        return True
    else:
        return False

print(chocolate_maker(3, 2, 10))