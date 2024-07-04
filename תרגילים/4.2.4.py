import calendar
days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]

data = input("Enter a date: ")
day, month, year = data.split('/')
print(days[calendar.weekday(int(year), int(month), int(day))])