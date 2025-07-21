########## DATETIME MODULE ##########


# Date and time some examples:

#   event logging ==> thanks to the knowledge of date and time, we are able to determine when exactly a critical error occurs 
#                     When creating logs we can specify the date and time format

#   tracking changes in adatabase ==> sometimes it's necessary to store information about when a record was created or modified
#                                     The datetime module will be perfect for this case

#   data validation ==> Knowing the current date and time, we'll be able to validate various types of date
#                       ex: whether a discount coupon entered by a user in our application is still valid

#   storing important information ==> can we imagine bank transfers without storing the information of when they were made? 
#                                     The date and time of certain actions must be preserved and we must deal with it


## datetime(year, month, day, hour, minute, second, microsecond, tzinfo, fold)

# year = 1 - 9999
# month = 1 - 12
# day = 1 -last day of month
# hour = 0 - 23
# minute = 0 - 59
# second = 0 - 59
# microsecond = 0 - 1000000
# tzinfo = tzinfo.subclass ou None
# fold = 0/1



## datetime.today()/.now()/.utcnow()

from datetime import datetime

print("today:", datetime.today())
# today: 2025-07-16 18:01:38.853576
print("now:", datetime.now())
# now: 2025-07-16 18:01:38.854341
print("utcnow:", datetime.utcnow())
# utcnow: 2025-07-16 18:01:38.854552



## date.today()

from datetime import date

# avec ue variable
today = date.today()
print("Today:", today)
# Today: 2025-07-15
print("Year:", today.year)
# Year: 2025
print("Month:", today.month)
# Month: 7
print("Day:", today.day)
# Day: 15

# en direct
print((date.today()).year)
# 2025



## date(year, month, day) 
# To create a date object we must pass the year, month, and day parameters as follows:

from datetime import date
my_date = date(2019, 11, 4)
print(my_date)
# 2019-11-04

# 1 <= date <= 9999
# 1 <= month <= 12
# 1 <= day <= last day of given month



## datetime.timestamp()
# eturns a float value expressing the number of seconds elapsed between the date and time indicated by the datetime object and January 1, 1970, 00:00:00 (UTC)
from datetime import datetime
dt = datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dt.timestamp())
# Timestamp: 1601823300.0



## date.fromtimestamp()

timestamp = time.time()
d = date.fromtimestamp(timestamp) # method fromtimestamp() = déduit la date en fonction du timestamp (time.time())
print("Date:", d)
# Date: 2025-07-15



## date.fromisoformat()

from datetime import datetime

# Date et heure au format ISO
iso_string = "2024-12-15T14:30:00"
dt = datetime.fromisoformat(iso_string)
print(f"Date/heure : {dt}")
# Date/heure : 2024-12-15 14:30:00
print(f"Année : {dt.year}")
# Année : 2024
print(f"Mois : {dt.month}")
# Mois : 12
print(f"Jour : {dt.day}")
# Jour : 15
print(f"Heure : {dt.hour}")
# Heure : 14

# Avec fuseau horaire
iso_string_tz = "2024-12-15T14:30:00+02:00"
dt_tz = datetime.fromisoformat(iso_string_tz)
print(f"\nAvec fuseau horaire : {dt_tz}")
# Avec fuseau horaire : 2024-12-15 14:30:00+02:00

# Juste une date
from datetime import date
date_string = "2024-12-15"
d = date.fromisoformat(date_string)
print(f"\nJuste la date : {d}")
# Juste la date : 2024-12-15

# Avec microsecondes
iso_micro = "2024-12-15T14:30:00.123456"
dt_micro = datetime.fromisoformat(iso_micro)
print(f"\nAvec microsecondes : {dt_micro}")
# Avec microsecondes : 2024-12-15 14:30:00.123456



## .replace(year, month, day)

from datetime import date

d = date(1991, 2, 5)
print(d)
# 1991-02-05

d = d.replace(day=16, year=1992, month=1)
print(d)
# 1992-01-16

e = (date(1991, 2, 5)).replace(1992, 1, 16) # position arguments par défaut
print(e)
# 1992-01-16


## .weekday()  isoweekday()
# returns the day of the week as an integer from 0 = Monday to 6 = Sunday
# with isoweekdy(), integer from 1 = Monday to 7 = Sunday

from datetime import date
d = date(2019, 11, 4)
print(d.weekday()) # 0 = lundi
# 0

from datetime import date
d = date(2019, 11, 4)
print(d.isoweekday()) # 1 = lundi
# 1



## time() - time(hour, minute, second, microsecond, tzinfo, fold)

# hour 0-23
# minute 0-59
# second 0-59
# microsecond 0 1000000
# tinfo = tzinfo-subclass or None
# fold = 0 par defaut, 0 ou 1h

from datetime import time
t = time(14, 53, 20, 1)
print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)
# Time: 14:53:20.000001
# Hour: 14
# Minute: 53
# Second: 20
# Microsecond: 1



## time.ctime()
# converts the time in seconds since January 1, 1970 (Unix epoch) to a string

import time
timestamp = 1572879180
print(time.ctime(timestamp))
# Mon Nov  4 15:53:00 2019

import time
print(time.ctime())
# Wed Jul 16 18:59:23 2025



## time.sleep()
# suspends program execution for the given number of seconds

import time
class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("I slept well! I feel great!")
student = Student()
student.take_nap(5)
# I'm very tired. I have to take a nap. See you later.
# ==> 5 4 3 2 1s
# I slept well! I feel great!   
    


## time.time() & timestamp

# The date class gives the ability to create a date object from a timestamp

# In Unix the timestamp expresses the number of seconds since January 1, 1970, 00:00:00 (UTC)
# This date is called the Unix epoch because this is when the counting of time began on Unix systems

# timestamp is actually the difference between a particular date (including time) and January 1, 1970, 00:00:00 (UTC), expressed in seconds
# To create a date object from a timestamp we must pass a Unix timestamp to the fromtimestamp method
# We can use the time module which provides time-related functions
# One of them is a function called time(), which returns the number of seconds from 1st January 1970 to the current moment in the form of a float number

from datetime import date
import time

print(time)
# <module 'time' (built-in)>
timestamp = time.time() # method time() du module time = nbre de sec depuis le 1/1/1970
print("Timestamp:", timestamp)
# Timestamp: 1752567892.3991797



## time.struct_time - gmtime() - localtime()
# the class looks like, and support indentation:

# 0     tm_year   # Specifies the year.
# 1     tm_mon    # Specifies the month (value from 1 to 12)
# 2     tm_mday   # Specifies the day of the month (value from 1 to 31)
# 3     tm_hour   # Specifies the hour (value from 0 to 23)
# 4     tm_min    # Specifies the minute (value from 0 to 59)
# 5     tm_sec    # Specifies the second (value from 0 to 61 )
# 6     tm_wday    # Specifies the weekday (value from 0 to 6)
# 7     tm_yday   # Specifies the year day (value from 1 to 366)
# 8     tm_isdst  # Specifies whether daylight saving time applies (1 – yes, 0 – no, -1 – it isn't known)
# -     tm_zone   # Specifies the timezone name (value in an abbreviated form)
# -     tm_gmtoff # Specifies the offset east of UTC (value in seconds)

import time
timestamp = 1572879180
print(time.gmtime(timestamp))
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)
print(time.localtime(timestamp))
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=15, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)
    
# time.localtime() utilise la configuration locale du système pour déterminer le fuseau horaire et ajuster l'heure en conséquence
 
 
 
## asctime() - mktime()

import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.asctime(st))
# converts a struct_time object or a tuple to a string
# Mon Nov  4 14:53:00 2019

print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))
# converts a struct_time object or a tuple that expresses the local time to the number of seconds since the Unix epoch
# 2019 => tm_year
# 11 => tm_mon
# 4 => tm_mday
# 14 => tm_hour
# 53 => tm_min
# 0 => tm_sec
# 0 => tm_wday
# 308 => tm_yday
# 0 => tm_isdst

# ==> 1572879180.0



## .strftime()
# very important method, it allows to return the date and time in the format we specify
# The strftime method takes only one argument in the form of a string specifying a format that can consist of directives
# A directive is a string consisting of the character % (percent) and a lowercase or uppercase letter
# For example, the directive %Y means the year with the century as a decimal number

from datetime import date
d = date(2020, 1, 4)
print(d.strftime('%y/%m/%d'))
# 20/01/04

from datetime import time
from datetime import datetime
t = time(14, 53)
print(t)
# 14:53:00
print(t.strftime("%H:%M:%S"))
# 14:53:00
dt = datetime(2020, 11, 4, 14, 53)
print(dt)
# 2020-11-04 14:53:00
print(dt.strftime("%y/%B/%d %H:%M:%S")) # le B indique de mettre en lettres le mois
# 20/November/04 14:53:00

import time
timestamp = 1572879180
st = time.gmtime(timestamp)
print(time.strftime("%Y/%m/%d %H:%M:%S", st)) # à partir d'un timestamp
# 2019/11/04 14:53:00
print(time.strftime("%Y/%m/%d %H:%M:%S")) # à partir de l'heure du système local
# 2025/07/17 11:43:06



## .strptime()
# creates a datetime object from a string representing a date and time
# requires to specify the format in which we saved the date and time

from datetime import datetime
print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S")) # données AVANT , format AVANT
# 2019-11-04 14:53:00 # ..a juste mis des "-" à la place des "/"

# doit matcher entre données et format sinon error, pa de valeur par defaut
from datetime import datetime
print(datetime.strptime("2019/11/04 14:53", "%Y/%m/%d %H:%M:%S")) # manque les sec dans les données
# ValueError: time data '2019/11/04 14:53' does not match format '%Y/%m/%d %H:%M:%S'

import time
print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=-1)



## date & time operation
# To create a timedelta object, just perform a subtraction on the date or datetime objects

from datetime import date
from datetime import datetime
d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)
print(d1 - d2)
# 366 days, 0:00:00
dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)
print(dt1 - dt2)
# 365 days, 9:07:00



## timedelta
# arguments accepted by the class constructor:
#   days, seconds, microseconds, milliseconds, minutes, hours, and weeks
#   each of them is optional and defaults to 0

from datetime import timedelta
delta = timedelta(weeks=2, days=2, hours=3)
print(delta)
# 16 days, 3:00:00

from datetime import timedelta
delta = timedelta(weeks=2, days=2, hours=3)
print("Days:", delta.days)
# Days: 16
print("Seconds:", delta.seconds)
# Seconds: 10800
print("Microseconds:", delta.microseconds)
# Microseconds: 0
# ==> Weeks are converted to days, hours and minutes to seconds, and milliseconds to microseconds

from datetime import timedelta
from datetime import date
from datetime import datetime
delta = timedelta(weeks=2, days=2, hours=2)
print(delta)
# 16 days, 2:00:00
delta2 = delta * 2
print(delta2)
# 32 days, 4:00:00 
d = date(2019, 10, 4) + delta2
print(d)
2019-11-05
dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt)
# 2019-11-05 18:53:00   