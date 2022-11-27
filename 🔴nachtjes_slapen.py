from datetime import date, datetime


year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))

d = date(year, month, day)
print(d)