from datetime import date, time, datetime

today = date.today()
now = datetime.now()

print("today's day is",today)
print("\ncurrentdate and time is ",now)
print("\nDate caomponents are ",today.year, today.month, today.day)