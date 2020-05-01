# Notes
#
# Working with "time" library
#
# "import time" imports time library
# " unix epic time" refers to a format of time that displays the number of seconds that have passed since January 1st 1970
# "time.localtime(x)" will return a tuple with the given "unix epic time"
# "time.time()" will return the "unix epic time" representation of the current time
# "time.localtime(time.time())" will return a tuple containing the current time
# "time.asctime(t)" takes in a tuple, t, and returns a string that represents the time given by the tuple
# Heirarchy is "unix epic time", "time tuple", and "asc time"
# "time.clock()"
# 
# Calendar
#
# "import calendar"
# "calendar.month(year, month)" will return a string representation of a month's view of a calendar
# You can print these calendars and they will be already formatted
# "calendar.isleap(year)" will return true if it is a leap year or not


import time
import datetime

timeToday = time.asctime(time.localtime(time.time()))
timeTomorrow = time.asctime(time.localtime(time.time() + 86400))
timeOneYearAgo =  time.asctime(time.localtime(time.time() - 31536000))
timeIn100Hours =  time.asctime(time.localtime(time.time() + 360000))

print("Now it is", timeToday)
print("Tomorrow it will be", timeTomorrow)
print("A year ago it was", timeOneYearAgo)
print("In 100 hours it will be", timeIn100Hours)

birthday = datetime.datetime(2000, 5, 6, 11, 00)print("I was born on ", birthday.isoformat(' '))