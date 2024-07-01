a = input("Please enter a string: ").lower().replace(' ', '')
if a[len(a) - 1] == 'c':
    c = float(a[:len(a) - 1])
    print((c * 1.8) + 32)
else:
    f = float(a[:len(a) - 1])
    print((f - 32) / 1.8)