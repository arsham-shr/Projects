import calendar

# Ask user for year and month
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

# Create a calendar instance
cal = calendar.monthcalendar(year, month)

# Print the calendar header
print(calendar.month_name[month], year)
print("Mo Tu We Th Fr Sa Su")

# Print each week
for week in cal:
    week_str = ""
    for day in week:
        if day == 0:
            week_str += "   "
        else:
            week_str += f"{day:2d} "
    print(week_str)
