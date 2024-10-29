#Due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.
#Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:
#if the year number isn't divisible by four, it's a common year;
#otherwise, if the year number isn't divisible by 100, it's a leap year;
#otherwise, if the year number isn't divisible by 400, it's a common year;
#otherwise, it's a leap year.



year = int(input("Enter a year: "))
l = "leap"
c = "common"
if (year < 1582) :
    print ("The",year,"year is not in the Gregorian calendar period")
elif year%4 != 0:
    print (year%4)
    yeartype = c
    print (yeartype)
    print ("The",year,"year is a",yeartype,"year")
elif year%100 != 0:
    print (year%100)
    yeartype = l
    print (yeartype)
    print ("The",year,"year is a",yeartype,"year")
elif year%400 != 0:
    print (year%400)
    yeartype = c
    print (yeartype)
    print ("The",year,"year is a",yeartype,"year")
else :
    yeartype = l
    print (yeartype)
    print ("The",year,"year is a",yeartype,"year")