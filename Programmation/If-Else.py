# -------- IF/ELSE/ELIF---------

# else execute si le if d'avant est False

# basic if
n = int(input("Enter n value: "))
 if n < 50 print ("bad")
 if n >= 50 and n <100 print ("good")
 if n=100 print ("perfect!")
 
# nesting way
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

# cascade
if the_weather_is_good
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()
	
# you mustn't use else without a preceding if;
# else is always the last branch of the cascade, regardless of whether you've used elif or not;
# else is an optional part of the cascade, and may be omitted;
# if there is an else branch in the cascade, only one of all the branches is executed;
# if there is no else branch, it's possible that none of the available branches is executed.


# how to identify the larger of two numbers:
# read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
# choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
# print the result
print("The larger number is:", larger_number)
Enter the first number: 4
Enter the second number: 6
The larger number is: 6

# OR

# read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1
# we check if the second number is larger than current largest_number
# and update largest_number if needed
if number2 > largest_number:
    largest_number = number2
# we check if the third number is larger than current largest_number
# and update largest_number if needed
if number3 > largest_number:
    largest_number = number3
# print the result
print("The largest number is:", largest_number)

# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
# Choose the larger number
if number1 > number2: larger_number = number1
else: larger_number = number2
# Print the result
print("The larger number is:", larger_number)
# if any of the if-elif-else branches contains just one instruction, 
# you may code it in a more comprehensive form (you don't need to make an indented line after the keyword, but just continue the line after the colon


# Quelle est ta plante preferrée ?
preferredplant = "Spathiphyllum"
plant = input("Which plant do you like ?")
if plant == preferredplant :
    print ("Yes - Spathiphyllum is the best plant ever!")
else:
    print ("Oh great")
	

# Quelle taxe dois-je payer ?
income = float(input("Enter the annual income: "))
tax = 0
if income <= 85528: tax = (0.18*income) - 556.02
else: tax = 14839.02 + 0.32*(income - 85528)
if tax <= 0: tax = 0 # on ne peut pas recevoir de l'argent.. seulement payer la taxe
tax = round(tax, 0)
print("The tax is:", tax, "thalers")


#login/password
name = input("login ? ")
print('Hello ',name)
if name == 'Mary':
        password = input("password ? ")
        if password == 'swordfish': 
            print('Access granted.')  
        else: 
            print('Wrong password.')

# savoir quelle type d'année on est 

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


# ---- while vs for avec else branch


i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
1
2
3
4
else: 5


for i in range(5):
    print(i)
else:
    i += 1
    print("else:", i)
0
1
2
3
4
else: 5


# break

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")
The break instruction:
Inside the loop. 1
Inside the loop. 2
Outside the loop.

while True:
  print('Please type your name.')
  name = input() 
  if name == 'your name':
    break
print('Thank you!')
Please type your name.
bounouar
Please type your name.
your name
Thank you!

while True:
    word = input("You're stuck in an infinite loop! Enter the secret word to leave the loop: ")
    if word == "chupacabra":
        break
print("You've successfully left the loop!")


# continue/break

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        break # on sort des que i=3
    print("Inside the loop.", i)
print("Outside the loop.")

Inside the loop. 1
Inside the loop. 2
Outside the loop.



# continue


# afficher les consonnes seulement
userWord = input("Enter your word: ")
userWord = userWord.upper()
for letter in userWord: # la variable est utilisée dans le code sans avoir ete definie par une valeur defaut ou depart auparavant
    if letter == "A": # si la lettre est A on continue mais on la print pas
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    elif letter == "Y":
        continue
    else:
        print(letter) 
Enter your word: azerty
Z
R
T

-- autre example
text = "pyxpyxpyx"
for letter in text:
    if letter == "x": 
        continue  # on saute la lettre x
    print(letter, end="")
pypypy

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")
john.smith


# modifier l'input et le printer
wordWithoutVowels = ""

userWord = input("Enter your word: ")
userWord = userWord.upper()

for letter in userWord:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        wordWithoutVowels += letter
		
print(wordWithoutVowels)	

OU

for digit in "0165031806510":
    if digit == "0":
        digit = "x"
        print (digit, end="")
        continue
    print (digit, end="")
x165x318x651x	
		
print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue # on continue meme si i=3
    print("Inside the loop.", i)
print("Outside the loop.")
Inside the loop. 1
Inside the loop. 2
Inside the loop. 4
Inside the loop. 5
Outside the loop.

while True: 
  print('Who are you?')  
  name = input() 
  if name != 'Joe': 
    continue  
  print('Hello, Joe. What is the password? (It is a fish.)') 
  password = input()   
  if password == 'swordfish': 
    break
print('Access granted.')


# break vs continue

largestNumber = -99999999
counter = 0
while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
	
    if number > largestNumber:
        largestNumber = number

if counter != 0:
    print("The largest number is", largestNumber)
else:
    print("You haven't entered any number.")
	
	
largestNumber = -99999999
counter = 0
number = int(input("Enter a number or type -1 to end program: "))
while number != -1:
    if number == -1:
        continue # !!! comprend pas !!!
    counter += 1

    if number > largestNumber:
        largestNumber = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largestNumber)
else:
    print("You haven't entered any number.")	
	
	
	

