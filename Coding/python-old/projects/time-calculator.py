# MON PROGRAMME
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

new_mins = (mins + dura) % 60
new_mins_STR = str(new_mins)
new_hour_en_min = (hour*60) + dura + mins
new_hour_en_hour = new_hour_en_min // 60
new_hour_en_hour_STR = str(new_hour_en_hour)

print ("The event will end at:", new_hour_en_hour_STR+":"+new_mins_STR)






# CORRECTION
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
# find a total of all minutes
totalmin = (mins + (hour * 60))
print (totalmin)
# find a number of hours hidden in minutes and update the hour
newtotalmin = (totalmin + dura)
print (newtotalmin)
newhour = (newtotalmin//60)
print (newhour)
newmin = (newtotalmin%60)
print (newmin)
# correct minutes to fall in the (0..59) range
# correct hours to fall in the (0..23) range
print(newhour, ":", newmin, sep='')