########## IF/ELSE/ELIF ##########


# you must not use else without a preceding if
# else is always the last branch of the cascade, regardless of whether you've used elif or not
# else is an optional part of the cascade, and may be omitted
# if there is an else branch in the cascade, only one of all the branches is executed
# if there is no else branch, it's possible that none of the available branches is executed
# else execute si le if d'avant est False


## basic if
n = int(input("Enter n value: "))
if n < 50:
    print ("bad")
if n >= 50 and n <100:
    print ("good")
if n==100:
    print ("perfect!")
 

## nesting way
if the_weather_is_good:
    if nice_restaurant_is_found:
        have_lunch()
    else:
        eat_a_sandwich()
else:
    if tickets_are_available:
        go_to_the_theater()
    else:
        go_shopping()


## cascade
if the_weather_is_good
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()


## IF vs ELIF
# si plusieurs IF de suite matchent les conditions, elles sont toutes appliquées
# si IF suivi de ELIF, seul 1 occurence sera matchée, la première qui matche

# ==> How much will the delivery cost be if the order value is 1700 and the state is FL (Florida)?

# avec IF ELIF
order = int(input('Please enter the order value: ')) # 1700
state = input('Please enter the state (as postal abbreviation): ') # FL
delivery = 0
 
if state in ['NC', 'SC', 'VA']:
    if order <= 1000:
        delivery = 70
    elif 1000 < order < 2000:
        delivery = 80
    else:
        delivery = 90
else:
    delivery = 50
    
if state in ['GA', 'WV', 'FL']:
    if order > 1000: # matche une seule fois
        delivery += 30
    elif order < 2000 and state in ['WV', 'FL']:
        delivery += 40
    else:
        delivery += 25
print(delivery)
# 80

# avec IF IF IF ..
order = int(input('Please enter the order value: ')) # 1700
state = input('Please enter the state (as postal abbreviation): ') # FL
delivery = 0
 
if state in ['NC', 'SC', 'VA']:
    if order <= 1000:
        delivery = 70
    elif 1000 < order < 2000:
        delivery = 80
    else:
        delivery = 90
else:
    delivery = 50
    
if state in ['GA', 'WV', 'FL']:
    if order > 1000: # matche une fois
        delivery += 30
    elif order < 2000 and state in ['WV', 'FL']: # matche une 2ème fois
        delivery += 40
    else:
        delivery += 25
print(delivery)
# 120


## how to identify the larger of two numbers

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
print("The larger number is:", larger_number)
# Enter the first number: 4
# Enter the second number: 6
# The larger number is: 6

# OR

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
largest_number = number1
if number2 > largest_number:
    largest_number = number2
if number3 > largest_number:
    largest_number = number3
print("The largest number is:", largest_number)


## Quelle est ta plante preferrée ?
preferredplant = "Spathiphyllum"
plant = input("Which plant do you like ?")
if plant == preferredplant :
    print ("Yes - Spathiphyllum is the best plant ever!")
else:
    print ("Oh great")
	

## Quelle taxe dois-je payer ?
income = float(input("Enter the annual income: "))
tax = 0
if income <= 85528: tax = (0.18*income) - 556.02
else: tax = 14839.02 + 0.32*(income - 85528)
if tax <= 0: tax = 0 # on ne peut pas recevoir de l'argent.. seulement payer la taxe
tax = round(tax, 0)
print("The tax is:", tax, "thalers")


## login/password
name = input("login ? ")
print('Hello ',name)
if name == 'Mary':
        password = input("password ? ")
        if password == 'swordfish': 
            print('Access granted.')  
        else: 
            print('Wrong password.')


## savoir quelle type d'année on est 

year = int(input("Enter a year: "))
if ((year%4) != 0): # on se sert de modulo pour savoir si une int est divisible par X
    print ("Common year")
elif ((year%100) != 0):
    print ("Leap year")
elif ((year%400) != 0):
    print ("Common year")
elif (year < 1582):
    print ("Not within the Gregorian calendar period")
else:
    print ("Leap year")


## while vs for avec else branch

i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
# 1
# 2
# 3
# 4
# else: 5

for i in range(5):
    print(i)
else:
    i += 1
    print("else:", i)
# 0
# 1
# 2
# 3
# 4
# else: 5