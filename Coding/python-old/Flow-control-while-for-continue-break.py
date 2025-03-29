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









## -------- WHILE -------- ##
# CONTINUE/BREAK pour gérer la sortie de la loop


# boucle simple
spam = 0
while spam < 5:  
  print('Hello, world.')
  spam = spam + 1
Hello, world.
Hello, world.
Hello, world.
Hello, world.
Hello, world.

i = 1
while i <= 4:
  print (i)
  i = i+1
1
2
3
4

# Afficher les odd numbers seulement
x = 1
while x < 11:
    if x%2 != 0:
        print (x,end="")
    x += 1
13579

# Savoir quel est le plus grand nombre de tous ceux qu'on a tape

largest_number = -999999999 # we will store the current largest number here
number = int(input("Enter a number or type -1 to stop: ")) # input the first value
while number != -1:  # if the number is not equal to -1, we will continue
   	if number > largest_number: # is number larger than largest_number?
        largest_number = number # yes, update largest_number
    number = int(input("Enter a number or type -1 to stop: ")) # input the next number
print("The largest number is:", largest_number) # print the largest number

	
# Compter les nombres pairs et impairs

odd_numbers = 0
even_numbers = 0
# read the first number
number = int(input("Enter a number or type 0 to stop: "))
# 0 terminates execution
while number != 0:
    # check if the number is odd
    if number % 2 == 1:
        # increase the odd_numbers counter
        odd_numbers += 1
    else:
        # increase the even_numbers counter
        even_numbers += 1
    # read the next number
    number = int(input("Enter a number or type 0 to stop: "))# print results
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)


#Inserer un counter pour sortir de la loops

counter = 5
while counter: # pas de precision sur la valeur de counter signifie different de zero
    print("Inside the loop.", counter)
    counter -= 1	
print("Outside the loop.", counter)
Inside the loop. 5
Inside the loop. 4
Inside the loop. 3
Inside the loop. 2
Inside the loop. 1
Outside the loop. 0


# compter et nommer les chats...

catNames = [] 
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +  ' (Or enter nothing to stop.):')    
	name = input() # NE MARCHE PAS
	if name == '':
	    break
	catNames = catNames + [name]  # list concatenation 
print('The cat names are:') 
for name in catNames:
    print('  ' + name)
--------


#Trouver le bon numero OU Rester bloque for ever
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

user_number = int(input("Enter the number: "))
while user_number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    user_number = int(input("Enter the number again: "))
print(secret_number, "Well done, muggle! You are free now.")


# Trouver le nombre de lignes sachant que chaque ligne a une brique de + que celle d'au-dessus (mur de briques) 
# et si manque de brique pour completer une rangée on arrete et on ne compte que les rangées pleines.

blocks = int(input("Enter the number of blocks: "))

height = 0
inlayer = 1
while inlayer <= blocks:
    height += 1
    blocks -= inlayer
    inlayer += 1
print("The height of the pyramid:", height)
Enter the number of blocks: 28
The height of the pyramid: 7



# verifier que:
#In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven)
#which can be described in the following way:
# - take any non-negative and non-zero integer number and name it c0;
# - if it's even, evaluate a new c0 as c0 ÷ 2;
# - otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
# - if c0 ≠ 1, skip to point 2.

c0 = int(input("Enter c0: "))

if c0 > 1:
	steps = 0
	while c0 != 1:
		if c0 %2 != 0:
			cnew = 3 * c0 + 1
		else:
			cnew = c0 // 2 # rappell // pour avoir int sinon sera en float 
		print(c0)
		c0 = cnew
		steps += 1
	print("steps =",steps)
else:
	print("Bad c0 value")
Enter c0: 6
6
3
10
5
16
8
4
2
steps = 8


# while not

name = '' 
while not name:
  print('Enter your name:') 
  name = input() 
print('How many guests will you have?') 
numOfGuests = int(input())
if numOfGuests: # means !=0 
  print('Be sure to have enough room for all your guests.')
print('Done')
Enter your name:# no name + Enter --> the loop restart

Enter your name:
benoit
How many guests will you have?
1
Be sure to have enough room for all your guests.
Done


## -------- FOR -------- ##

animaux = ['girafe','tigre','singe','souris']
for i in animaux:   #  i pour itération, va lister toutes les itérations de la liste
	print i
		
girafe
tigre
singe
souris


animaux = ['girafe','tigre','singe','souris'] --> par indexation
for i in animaux[1:3]:
    print i

tigre
souris

# On peut melanger avec du range pour n'afficher qu'une partie ou tout:

animaux = ['girafe', 'tigre', 'singe', 'souris']
for i in range(4):
	print animaux[i]
	
girafe
tigre
singe
souris

for i in range(2):
	print animaux[i]

girafe
tigre


animaux = ['girafe','tigre','singe','souris'] --> pour avoir l'element ET l'index
for i, ani in enumerate(animaux):
	print i,ani
	
0 girafe
1 tigre
2 singe
3 souris


vendors = ['arista', 'juniper', 'big_switch', 'cisco']
for index, each in enumerate(vendors):
    print(str(index) + ' ' + each) # l'index étant une integer il faudra le changer en string pour pouvoir additionner avec les valeurs 'vendors'


# Pour connaitre les valeurs de 2^n avec n compris entre 0 et 15
pow = 1
for exp in range(16):
    print("2 to the power of", exp, "is", pow)
    pow *= 2

# Pour compter en ajoutant un mot (123 soleil)
import time

for second in range(1,6):
    print(second, "Mississippi")
    time.sleep(3) # ajoute un compte entre chaque occurence, ici 3s
	
print("Ready or not, here I come!")
1 Mississippi
2 Mississippi
3 Mississippi
4 Mississippi
5 Mississippi

lst = [i for i in range (-1,2)]
print (lst)
[-1, 0, 1]

lst = [[0,1,2,3] for i in range (2)]
print (lst)
[0,1,2,3], [0,1,2,3]

t = [[3-i for i in range (3)] for j in range (3)]
s = 0
print (t)
for i in range (3):
    s += t[i][i]
print (s)
[[3, 2, 1], [3, 2, 1], [3, 2, 1]]
6 # 0+ 3 +2 +1


# Pour afficher tous les couples key/value
device = {'hostname': 'router1', 'vendor': 'juniper', 'os': '12.1'}
device.pop('os')
oper = dict(cpu='5%', memory='10%')
print(oper)
device.update(oper)
print(device)

for key, value in device.items():
    print(key + ': ' + value)

{'cpu': '5%', 'memory': '10%'}
{'hostname': 'router1', 'vendor': 'juniper', 'cpu': '5%', 'memory': '10%'}
hostname: router1
vendor: juniper
cpu: 5%
memory: 10%


# Pour générer des commandes reseaux

COMMANDS = {
'description': 'description {}',
'speed': 'speed {}',
'duplex': 'duplex {}',
}
print(COMMANDS)

CONFIG_PARAMS = {
'description': 'auto description by Python',
'speed': '10000',
'duplex': 'auto'
}
commands_list = []

for feature, value in CONFIG_PARAMS.items():
    command = COMMANDS.get(feature).format(value)
    commands_list.append(command)

commands_list.insert(0, 'interface Eth1/1')

print(commands_list)

{'description': 'description {}', 'speed': 'speed {}', 'duplex': 'duplex {}'}
['interface Eth1/1', 'description auto description by Python', 'speed 10000', 'duplex auto']



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
	
	
	
# for/in

print('My name is')
for i in range(5):   
    print('Jimmy Five Times (' + str(i) + ')')
Jimmy Five Times (0)
Jimmy Five Times (1)
Jimmy Five Times (2)
Jimmy Five Times (3)
Jimmy Five Times (4)

--> same with for

print('My name is')
i = 0 
while i < 5: 
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1
Jimmy Five Times (0)
Jimmy Five Times (1)
Jimmy Five Times (2)
Jimmy Five Times (3)
Jimmy Five Times (4)

total = 0
for num in range(4): 
    total = total + num 
print(total)
6


n = range(4)

for num in n:
    print(num - 1)
else:
    print(num)
0
1
2
3
4 # valeur de n non traitée .... a creuser  car range (4) concerne de 0 à 3
