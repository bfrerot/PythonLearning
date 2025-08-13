########## IF/ELSE/ELIF ##########


# elif/else come AFTER if or SYNTAX ERROR
# else is always the LAST branch of the cascade, regardless of whether you've used elif or not
# else is an optional part of the cascade, and may be omitted
# if there is an else branch in the cascade, only one of all the branches is executed
# if there is no else branch, it's possible that none of the available branches is executed
# else s'execute si le if d'avant est False



### BASIC IF
# si plusieurs IF de suite matchent les conditions, elles sont toutes appliquées

n = int(input("Enter n value: ")) # 70
if n < 50:
    print ("bad")
if n >= 50 and n <100:  # MATCH
    print ("good")
if n==100:
    print ("perfect!")
# good

n = int(input("Enter n value: ")) # 100
if n < 50:
    print ("bad")
if n >= 50:         # MATCH
    print ("good")
if n==100:          # MATCH
    print ("perfect!")
# good
# perfect!
 


### NESTING WAY
# si IF suivi de ELSE/ELIF, seul 1 occurence sera matchée, la première qui matche
''' 
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
'''

order = int(input('Please enter the order value: ')) # 1700
state = input('Please enter the state (as postal abbreviation): ') # FL
delivery = 0

# 1er bloc indépendant 
if state in ['NC', 'SC', 'VA']:
    if order <= 1000:
        delivery = 70
    elif 1000 < order < 2000:
        delivery = 80
    else:
        delivery = 90
else:                           # MATCH
    delivery = 50  

# 2ème bloc indépendant    
if state in ['GA', 'WV', 'FL']:
    if order > 1000:            # MATCH
        delivery += 30
    elif order < 2000 and state in ['WV', 'FL']:
        delivery += 40
    else:
        delivery += 25
print(delivery)
# 80



### CASCADE
# si IF suivi de ELSE/ELIF, seul 1 occurence sera matchée, la première qui matche
''' 
if the_weather_is_good
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()
'''

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
else:                             # MATCH
    delivery = 50
    
if state in ['GA', 'WV', 'FL']:
    if order > 1000:              # MATCH
        delivery += 30
    elif order < 2000 and state in ['WV', 'FL']: # NE MATCH PAS une 2ème fois... dommage,  du à une mauvaise priorisation
        delivery += 40
    else:
        delivery += 25
print(delivery)
# 80

# ==> version plus cohérente
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
else:                             # MATCH
    delivery = 50
    
if state in ['GA', 'WV', 'FL']:
    if order < 2000 and state in ['WV', 'FL']: # MATCH
        delivery += 40
    elif order > 1000:              
        delivery += 30
    else:
        delivery += 25
print(delivery)
# 90



### EXEMPLES USAGE 


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
	

## login/password
name = input("login ? ")
print('Hello ',name)
if name == 'Mary':
        password = input("password ? ")
        if password == 'swordfish': 
            print('Access granted.')  
        else: 
            print('Wrong password.')


