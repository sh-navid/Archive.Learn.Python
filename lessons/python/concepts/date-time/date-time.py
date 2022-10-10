from datetime import datetime, date, time

print(datetime.now())
print(date(2020, 12, 10))
print(time(hour=12, minute=31))

print(datetime.now().strftime("%Y - %m - %d --- %H:%M':%S\""))
