########## CALENDAR MODULE ##########

# monday    ==> 0 ==> calendar.MONDAY
# tuesday   ==> 1 ==> calendar.TUESDAY
# wednesday ==> 2 ==> calendar.WEDNESDAY
# thursday  ==> 3 ==> calendar.THURSDAY
# friday    ==> 4 ==> calendar.FRIDAY
# saturday  ==> 5 ==> calendar.SATURDAY
# sunday    ==> 6 ==> calendar.SUNDAY

import calendar 
print(calendar.calendar(2020)) # similar to the result of the cal command available in Unix
#                                    2020
# 
#       January                   February                   March
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#        1  2  3  4  5                      1  2                         1
#  6  7  8  9 10 11 12       3  4  5  6  7  8  9       2  3  4  5  6  7  8
# 13 14 15 16 17 18 19      10 11 12 13 14 15 16       9 10 11 12 13 14 15
# 20 21 22 23 24 25 26      17 18 19 20 21 22 23      16 17 18 19 20 21 22
# 27 28 29 30 31            24 25 26 27 28 29         23 24 25 26 27 28 29
#                                                     30 31
# 
#        April                      May                       June
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#        1  2  3  4  5                   1  2  3       1  2  3  4  5  6  7
#  6  7  8  9 10 11 12       4  5  6  7  8  9 10       8  9 10 11 12 13 14
# 13 14 15 16 17 18 19      11 12 13 14 15 16 17      15 16 17 18 19 20 21
# 20 21 22 23 24 25 26      18 19 20 21 22 23 24      22 23 24 25 26 27 28
# 27 28 29 30               25 26 27 28 29 30 31      29 30
# 
#         July                     August                  September
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#        1  2  3  4  5                      1  2          1  2  3  4  5  6
#  6  7  8  9 10 11 12       3  4  5  6  7  8  9       7  8  9 10 11 12 13
# 13 14 15 16 17 18 19      10 11 12 13 14 15 16      14 15 16 17 18 19 20
# 20 21 22 23 24 25 26      17 18 19 20 21 22 23      21 22 23 24 25 26 27
# 27 28 29 30 31            24 25 26 27 28 29 30      28 29 30
#                           31
#
#       October                   November                  December
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#           1  2  3  4                         1          1  2  3  4  5  6
#  5  6  7  8  9 10 11       2  3  4  5  6  7  8       7  8  9 10 11 12 13
# 12 13 14 15 16 17 18       9 10 11 12 13 14 15      14 15 16 17 18 19 20
# 19 20 21 22 23 24 25      16 17 18 19 20 21 22      21 22 23 24 25 26 27
# 26 27 28 29 30 31         23 24 25 26 27 28 29      28 29 30 31
#                           30

# To change the default calendar formatting, we can use the following parameters:
#   w – date column width (default 2)
#   l – number of lines per week (default 1)
#   c – number of spaces between month columns (default 6)
#   m – number of columns (default 3)



## calendar.month() / calendar.prmonth

import calendar
print(calendar.month(2020, 11))   
#     November 2020
# Mo Tu We Th Fr Sa Su
#                    1
#  2  3  4  5  6  7  8
#  9 10 11 12 13 14 15
# 16 17 18 19 20 21 22
# 23 24 25 26 27 28 29
# 30

# can change the default formatting using the following parameters:
#   w – date column width (default 2)
#   l – number of lines per week (default 1)

import calendar
calendar.prmonth(2020, 11)
#     November 2020
# Mo Tu We Th Fr Sa Su
#                    1
#  2  3  4  5  6  7  8
#  9 10 11 12 13 14 15
# 16 17 18 19 20 21 22
# 23 24 25 26 27 28 29
# 30



## calendar.setfirstweekday

import calendar
calendar.setfirstweekday(calendar.SUNDAY) # or calendar.setfirstweekday(6)
calendar.prmonth(2020, 12)
#    December 2020
# Su Mo Tu We Th Fr Sa
#        1  2  3  4  5
#  6  7  8  9 10 11 12
# 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26
# 27 28 29 30 31



## calendar.weekday
# returns the day of the week as an integer value for the given year, month, and day

import calendar
print(calendar.weekday(2025, 7, 17))
# 3 # = jeudi



## calendar.weekheader()
# requires to specify the width in characters for one day of the week
# If the width you provide is greater than 3 we'll still get the abbreviated weekday names consisting of 3 characters

import calendar
print(calendar.weekheader(2))
# Mo Tu We Th Fr Sa Su
print(calendar.weekheader(5))
#  Mon   Tue   Wed   Thu   Fri   Sat   Sun 



## calendar.isleap()/.leapdays()

import calendar
print(calendar.isleap(2020))
# True
print(calendar.leapdays(2010, 2021))  # Up to but not including 2021, returns the number of leap years in the given range of years
# 3



## calendar.Calendar 
# ==> provides methods to prepare calendar data for formatting

# .itermonthdays() 
# returns a list or tupples
import calendar
cal = calendar.Calendar()
print(list(cal.itermonthdays(2024, 7)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 0, 0, 0, 0]
# Pour compléter la dernière semaine du calendrier, on ajoute des 0 pour les jours manquants (jeudi, vendredi, samedi, dimanche)


import calendar
c = calendar.Calendar()
for iter in c.itermonthdays2(2019, 11): # regroupe date/jour et itération
    print(iter, end=" ")
# (0, 0) (0, 1) (0, 2) (0, 3) (1, 4) (2, 5) (3, 6) (4, 0) (5, 1) (6, 2) (7, 3) (8, 4) (9, 5) (10, 6) (11, 0) (12, 1) (13, 2) (14, 3) (15, 4) (16, 5) (17, 6) 
# (18, 0) (19, 1) (20, 2) (21, 3) (22, 4) (23, 5) (24, 6) (25, 0) (26, 1) (27, 2) (28, 3) (29, 4) (30, 5) (0, 6)


import calendar  
c = calendar.Calendar()
for iter in c.itermonthdays3(2019, 11): # regroupe année/mois/date du jour
    print(iter, end=" ")
# (2019, 10, 28) (2019, 10, 29) (2019, 10, 30) (2019, 10, 31) (2019, 11, 1) (2019, 11, 2) (2019, 11, 3) (2019, 11, 4) (2019, 11, 5) (2019, 11, 6) 
# (2019, 11, 7) (2019, 11, 8) (2019, 11, 9) (2019, 11, 10) (2019, 11, 11) (2019, 11, 12) (2019, 11, 13) (2019, 11, 14) (2019, 11, 15) (2019, 11, 16) 
# (2019, 11, 17) (2019, 11, 18) (2019, 11, 19) (2019, 11, 20) (2019, 11, 21) (2019, 11, 22) (2019, 11, 23) (2019, 11, 24) (2019, 11, 25) (2019, 11, 26) 
# (2019, 11, 27) (2019, 11, 28) (2019, 11, 29) (2019, 11, 30) (2019, 12, 1)


# .iterweekdays()

import calendar  
c = calendar.Calendar(calendar.SUNDAY)
for weekday in c.iterweekdays():
    print(weekday, end=" ")
# 6 0 1 2 3 4 5


# .monthdays2calendar()
# takes the year and month, and returns a list of weeks in a specific month
# Each week is a tuple consisting of day numbers and weekday numbers

import calendar  
c = calendar.Calendar()
for data in c.monthdays2calendar(2020, 12):
    print(data)
# [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)] # de lundi 30/11 au dimanche 6/12
# [(7, 0), (8, 1), (9, 2), (10, 3), (11, 4), (12, 5), (13, 6)]
# [(14, 0), (15, 1), (16, 2), (17, 3), (18, 4), (19, 5), (20, 6)]
# [(21, 0), (22, 1), (23, 2), (24, 3), (25, 4), (26, 5), (27, 6)]
# [(28, 0), (29, 1), (30, 2), (31, 3), (0, 4), (0, 5), (0, 6)]



## calendar.TextCalendar 
# ==> is used to create regular text calendars

import calendar
text_cal = calendar.TextCalendar()
# Afficher le calendrier de juillet 2024 en texte
print(text_cal.formatmonth(2024, 7))
#       July 2024
# Mo Tu We Th Fr Sa Su
#  8  9 10 11 12 13 14
# 15 16 17 18 19 20 21
# 22 23 24 25 26 27 28
# 29 30 31



## calendar.HTMLCalendar 
# ==> is used to create HTML calendars

import calendar
html_cal = calendar.HTMLCalendar()
# Générer le calendrier de juillet 2024 en HTML
html_output = html_cal.formatmonth(2024, 7)
print(html_output)
# <table border="0" cellpadding="0" cellspacing="0" class="month">
# <tr><th colspan="7" class="month">July 2024</th></tr>
# <tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>
# <tr><td class="mon">1</td><td class="tue">2</td><td class="wed">3</td><td class="thu">4</td><td class="fri">5</td><td class="sat">6</td><td class="sun">7</td></tr>
# <tr><td class="mon">8</td><td class="tue">9</td><td class="wed">10</td><td class="thu">11</td><td class="fri">12</td><td class="sat">13</td><td class="sun">14</td></tr>
# <tr><td class="mon">15</td><td class="tue">16</td><td class="wed">17</td><td class="thu">18</td><td class="fri">19</td><td class="sat">20</td><td class="sun">21</td></tr>
# <tr><td class="mon">22</td><td class="tue">23</td><td class="wed">24</td><td class="thu">25</td><td class="fri">26</td><td class="sat">27</td><td class="sun">28</td></tr>
# <tr><td class="mon">29</td><td class="tue">30</td><td class="wed">31</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td></tr>
# </table>

# ==> file:///C:/PythonLearning/calendar.html



## calendar.LocalTextCalendar 
# ==> is a subclass of the calendar.TextCalendar class
#     The constructor of this class takes the local parameter to return the appropriate months and weekday names

import calendar
# Calendrier en français
local_cal = calendar.LocaleTextCalendar(locale='fr_FR.UTF-8')
print(local_cal.formatmonth(2024, 7))
#     juillet 2024
# lu ma me je ve sa di
#  1  2  3  4  5  6  7
#  8  9 10 11 12 13 14
# 15 16 17 18 19 20 21
# 22 23 24 25 26 27 28
# 29 30 31



## calendar.LocalHTMLCalendar 
# ==> is a subclass of the calendar.HTMLCalendar class
#     The constructor of this class takes the locale parameter to return the appropriate months and weekday names
# <table border="0" cellpadding="0" cellspacing="0" class="month">
# <tr><th colspan="7" class="month">juillet 2024</th></tr>
# <tr><th class="mon">lun.</th><th class="tue">mar.</th><th class="wed">mer.</th><th class="thu">jeu.</th><th class="fri">ven.</th><th class="sat">sam.</th><th class="sun">dim.</th></tr>
# <tr><td class="mon">1</td><td class="tue">2</td><td class="wed">3</td><td class="thu">4</td><td class="fri">5</td><td class="sat">6</td><td class="sun">7</td></tr>
# <tr><td class="mon">8</td><td class="tue">9</td><td class="wed">10</td><td class="thu">11</td><td class="fri">12</td><td class="sat">13</td><td class="sun">14</td></tr>
# <tr><td class="mon">15</td><td class="tue">16</td><td class="wed">17</td><td class="thu">18</td><td class="fri">19</td><td class="sat">20</td><td class="sun">21</td></tr>
# <tr><td class="mon">22</td><td class="tue">23</td><td class="wed">24</td><td class="thu">25</td><td class="fri">26</td><td class="sat">27</td><td class="sun">28</td></tr>
# <tr><td class="mon">29</td><td class="tue">30</td><td class="wed">31</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td></tr>
# </table>

# ==> file:///C:/PythonLearning/calendar.html



## .itermonthdates
# retourne les dates complètes pour former des semaines entières d'ou le debut par 10-28, 10-29 etc pour lundi, mardi etc

import calendar  
c = calendar.Calendar()
for date in c.itermonthdates(2019, 11):
    print(date, end=" ")
# 2019-10-28 2019-10-29 2019-10-30 2019-10-31 2019-11-01 2019-11-02 2019-11-03 2019-11-04 2019-11-05 2019-11-06 2019-11-07 2019-11-08 2019-11-09 2019-11-10 2019-11-11 2019-11-12 2019-11-13 2019-11-14 2019-11-15 2019-11-16 2019-11-17 2019-11-18 2019-11-19 2019-11-20 2019-11-21 2019-11-22 2019-11-23 2019-11-24 2019-11-25 2019-11-26 2019-11-27 2019-11-28 2019-11-29 2019-11-30 2019-12-01



## 