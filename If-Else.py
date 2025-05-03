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