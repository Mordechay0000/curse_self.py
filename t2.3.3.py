all_long = int(input("num"))
all_short = (all_long // 100) + ((all_long % 100) // 10) + ((all_long % 100) % 10)
print(all_short)
print(int(all_short / 3))
print(all_short % 3)
print(not(bool(all_short % 3)))



