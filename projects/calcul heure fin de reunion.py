# calcul heure de fin reunion
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
hourinmin = hour* 60
newhourinmin = hourinmin + mins + dura
newmin = newhourinmin % 60
newhour = (newhourinmin - newmin) / 60
print("your event will finish at: ", str(int(newhour))+":"+str(newmin))
# Starting time (hours): 5
# Starting time (minutes): 45
# Event duration (minutes): 60
# your event will finish at:  6:45
