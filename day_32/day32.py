import datetime as dt

now=dt.datetime.now()
year=now.year
month=now.month
day_of_week=now.weekday()
print(now)
print(month)
print(year)
print(day_of_week)

date_of_birth=dt.datetime(year=1992,month=7,day=6)
print(date_of_birth)