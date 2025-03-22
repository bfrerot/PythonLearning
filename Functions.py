#########  --------- FUNCTIONS ----------  ########

#A function is able to:
#   cause some effect
#   evaluate a value


#Every function has two parts:
# 1. The function signature defines the name of the function and any inputs it expects.
# 2. The function body contains the code that runs every time the function is used.
def multiply(x, y): # Function signature
# Function body below
    product = x * y
    return product


#The function signature has four parts:
# 1. The def keyword
# 2. The function name, multiply
# 3. The parameter list, (x, y)
# 4. A colon (:) at the end of the line


#Function name STARTS by a letter and conatins ONLY letters, numbers and _


#Functions come from at least three places:
# 1- from Python itself - numerous functions (like print()) are an integral part of Python, and are always available without any additional effort on behalf of the programmer; we call these functions built-in functions;
# 2- from Python's preinstalled modules - a lot of functions, very useful ones, but used significantly less often than built-in ones, are available in a number of modules installed together with Python; the use of these functions requires some additional steps from the programmer in order to make them fully accessible (we'll tell you about this in a while);
# 3- directly from your code - you can write your own functions, place them inside your code, and use them freely;


#The process for executing a function can be summarized in three steps:
# 1. The function is called, and any arguments are passed to the function as input.
# 2. The function executes, and some action is performed with the arguments.
# 3. The function returns, and the original function call is replaced with the return value.


#Regarding returns:
# 1- you are always allowed to ignore the function's result, and be satisfied with the function's effect (if the function has any)
# 2- if a function is intented to return a useful result, it must contain the second variant of the return instruction.


#Scopes:
#The function func() has a different scope than the code that exists outside of the function. 
#We can name an object inside func() the same name as something outside func() and Python can keep the two separated.
# 1- a var defined out the function is usable into a function
# 2- a var defined in a function is not recognised out of it
# 3- if a var has the same name into a function and out of it, the function uses the var as defined into it
#    use "global" to overcome this
# 4- with lists, if a list is processed by a function, it will reflect the changes outside the function (see example)

# Python resolves scope in the order in which each scope appears in the list LEGB.
# 1- Local (L): The local, or current, scope. The scope that the Python interpreter is currently working in.
# 2- Enclosing (E): The enclosing scope. This is the scope one level up from the local scope. 
#If the local scope is an inner function, the enclosing scope is the scope of the outer function. 
#If the scope is a top-level function, the enclosing scope is the same as the global scope.
# 3- Global (G): The global scope, which is the top-most scope in the script. This contains all of the names 
#defined in the script that are not contained in a function body.
# 4- Built-in (B): The built-in scope contains all of the names, such as keywords, that are built-in to Python. Functions such as round()

#ex
x = 5
def outer_func():
    y = 3
    def inner_func():
        z = x + y
        return z
    return inner_func()
print (outer_func())
8

# Here the case we can have an error, and how to fix it

total = 0
def add_to_total(n):
    total = total + n
add_to_total(5)
print(total)
Traceback (most recent call last):
  File "C:\Users\bfrerot\OneDrive - ID Logistics\Documents\Python\IDLE.py", line 4, in <module>
    add_to_total(5)
  File "C:\Users\bfrerot\OneDrive - ID Logistics\Documents\Python\IDLE.py", line 3, in add_to_total
    total = total + n
UnboundLocalError: local variable 'total' referenced before assignment # The problem here is that the script attempts to make an assignment to
# the variable total, which creates a new name in the local scope. Then,when Python executes the right-hand side of the assignment it finds
# the name total in the local scope with nothing assigned to it yet.
# We need to use the global keyword to fix it:
total = 0
def add_to_total(n):
    global total
    total = total + n
add_to_total(5)
print(total)
5



#Documenting a function with a DOCSTRING:
def multiply(x, y):
    """Return the product of two numbers x and y.""" # comment in function =  docstring
    product = x * y
    return product
help(multiply)
Help on function multiply in module __main__:

multiply(x, y)
    Return the product of two numbers x and y. # comment retruned when help function is used







# ------- Function VS Methods -------

#A method is a specific kind of function - it behaves like a function and looks like a function,
#but differs in the way in which it acts, and in its invocation style.
#result = data.method(arg)
#MEthods are used to play with lists

#A function doesn't belong to any data - it gets data, it may create new data and it (generally) produces a result.
#result = function(arg)
#ex:
# var TO function - OK
import marshal
from termios import VSTART


def myFunction():
    print("Do I know that variable?", var)
var = 1
myFunction()
Do I know that variable? 1


#type(anything)
a=5
print(type(a))
int
a=5.2
print(type(a))
float
a="papa"
print(type(a))
<class 'str'>

## fonctions pour changer de type

# de float ou int vers str
a= 2.2
print (str(a))
2.2
d= 4
print (str(d))
4 # en fait "4"

b = "20.2"
print (str(int(float(b))))
20

total_pancakes = 10
pancakes_eaten = 5
print ("Only " + str(total_pancakes - pancakes_eaten) + " pancakes left.")
Only 5 pancakes left.# on a changé le resultat d'une operation en str

# de string vers int, attention si virgule on ne pourra pas convertir en int
# par contre possible dans l'autre sens de float vers int vers str (cf au-dessus)
b = "20.2"
print (int(b))
Traceback (most recent call last):
  File "C:\Users\bfrerot\OneDrive - ID Logistics\Documents\Python\IDLE.py", line 2, in <module>
    print (int(b))
ValueError: invalid literal for int() with base 10: '20.2'

e = float(b)
print (e)
20.2



##input()
#the result of the input() function is a string.

print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")
anything = input()
print("What do you mean by ", anything)
Tell me anything...
yes
Hmm... yes ... Really?
no
What do you mean by  no
# la meme variable peut changer au cours du programme, ici anything = yes puis no


#calcul carré d'un nombre
anything = int(input("Enter a number: ")) #the result of the input() function is a string.
something = anything*2
print(anything, "to the power of 2 is", something)
Enter a number: 2
2 to the power of 2 is 4


#calcul carré d'un nombre
anything = float(input("Enter a number: ")) the result of the input() function is a string.
something = anything*2
print(anything, "to the power of 2 is", something)
Enter a number: 2
2.0 to the power of 2 is 4.0


#calcul longueur hypoténuse triangle rectangle à 2 chiffres après la virgule
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = round((leg_a**2 + leg_b**2) ** .5,2)
print("Hypotenuse length is", hypo)
Input first leg length: 4
Input second leg length: 8
Hypotenuse length is 8.94


# nom prenom ?
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("Your name is " + fnam + " " + lnam + ".")
May I have your first name, please? benoit
May I have your last name, please? frerot
Thank you.
Your name is benoit frerot.


# hostname
ceorpe = input("is the router a ce or a pe? ")
cityairportref = input("what is the city airport trigram? ")
customer = input("who is the customer? ")
customer = customer [0:3]
occurence = input("what is the equipment number? ")
print("Your router hostname is " + ceorpe + cityairportref + customer + "-" + occurence)
ce
mrs
natixis
36
Your router hostname is cemrsnat-36


# calcul heure de fin reunion
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
hourinmin = hour* 60
newhourinmin = hourinmin + mins + dura
newmin = newhourinmin % 60
newhour = (newhourinmin - newmin) / 60
print("your event will finish at: ", str(int(newhour))+":"+str(newmin))
Starting time (hours): 5
Starting time (minutes): 45
Event duration (minutes): 60
your event will finish at:  6:45


# donner des operations enfonction de variables
a = float(input("give a float a:"))# input a float value for variable a here
b = float(input("give a float b:"))# input a float value for variable b here
print("a+b=",a+b)# output the result of addition here
print("a-b=",a-b)# output the result of subtraction here
print("a*b=",a*b)# output the result of multiplication here
print("a/b=",a+b)# output the result of division here
print("That's all, folks!")
give a float a:2.0
give a float b:4
a+b= 6.0
a-b= -2.0
a*b= 8.0
a/b= 6.0
That's all, folks!


# function TO var - NOK
def scopeTest():
    x = 123
scopeTest()
print(x)
Traceback (most recent call last):
  File "main.py", line 5, in <module>
    print(x)
NameError: name 'x' is not defined

# same var name in and out the function
def myFunction():
    var = 2
    print("Do I know that variable?", var)
var = 1
myFunction()
print(var)
Do I know that variable? 2
1

# export a var out the function with "global"
def myFunction():
    global var
    var = 2
    print("Do I know that variable?", var)

var = 1
myFunction()
Do I know that variable? 2

def myFunction(myList1):
    print(myList1)
    del myList1[0]

myList2 = [2, 3]
myFunction(myList2)
print(myList2)

def myFunction(n1):
    print(n1)
    n1 += 1

# Si pas de return dans la function, alors function affichera "None" à la fin du process

var1 = (float(input("give me a number: ")))
def double(var1):
    print(var1*2)
    print(var1*4)
    print(var1*8)
#   return "Thanks"
print(double(var1))
4.0
8.0
16.0
None

var1 = (float(input("give me a number: ")))
def double(var1):
    print(var1*2)
    print(var1*4)
    print(var1*8)
    return "Thanks"
print(double(var1))
4.0
8.0
16.0
Thanks



spam = print('Hello!')
print (None == spam)
Hello!
True

n2 = 2
myFunction(n2)
print(n2)

You can define your own function using the def keyword and the following syntax:
 
def yourFunction(optional parameters):
    # the body of the function

	
You can define a function which doesn't take any arguments, e.g.:

def message():    # defining a function
    print("Hello")    # body of the function

message()    # calling the function 


You can define a function which takes arguments, too, just like the one-parameter function below:

def hello(name):    # defining a function
    print("Hello,", name)    # body of the function
name = input("Enter your name: ")
hello(name)    # calling the function 


## difference entre invoquer et printer la function
#invoquer
def wishes():
    print("My Wishes")
    return "Happy Birthday"
wishes()
My Wishes

#printer
def wishes():
    print("My Wishes")
    return "Happy Birthday"
print(wishes())
My Wishes
Happy Birthday


Une variable peut avoir le meme nom qu'une variable

#


# Definir un message et l'incorporer avec des input - simple

def message():
    print("Enter a value: ")

message()
a = int(input()) # definit une variable en meme temps
message()
b = int(input())
message()
c = int(input())
Enter a value: 
1
Enter a value: 
1
Enter a value: 
1





def message(what, number):
    print("Enter", what, "number", number)

message("telephone", 11)
message("price", 5)
message("number", "number")
Enter telephone number 11
Enter price number 5
Enter number number number


# parameters dans l'odre
def introduction(firstName, lastName):
    print("Hello, my name is", firstName, lastName)

introduction("Luke", "Skywalker") # if parameter is not specified with an = + parameter value, default order is respected
introduction("Jesse", "Quick")
introduction("Clark", "Kent")
Hello, my name is Luke Skywalker
Hello, my name is Jesse Quick
Hello, my name is Clark Kent


# parameters dans le desordre
def introduction(firstName, lastName):
    print("Hello, my name is", firstName, lastName)

introduction(firstName = "James", lastName = "Bond")
introduction(lastName = "Skywalker", firstName = "Luke") # if parameters are set in a different order with an = + parameter, the function doesn't care and sort it in the right way 
Hello, my name is James Bond
Hello, my name is Luke Skywalker


# paremeters par defaut
def introduction(firstName, lastName="Smith"):
    print("Hello, my name is", firstName, lastName)
introduction("James")
Hello, my name is James Smith # parameter unique = premier (ici first name) + deuxieme par defaut

# un seul peut suffire

def fun(inp=2,out=3):
    return inp * out
print (fun(out=2))
4

# parameter par defaut ecrasé par celui indiqué
def introduction(firstName, lastName="Smith"):
    print("Hello, my name is", firstName, lastName)
introduction("James","Doe")
Hello, my name is James Doe # Smith (default parameter) is replaced by Doe (specified parameter)


# SyntaxError: non-default argument follows default argument
def sum(a, b=1, c):
    print(a + b + c)

sum(1, 2, 3)
File "main.py", line 1
    def sum(a, b=1, c):
           ^
SyntaxError: non-default argument follows default argument # a non default parameter CANNOT follow a default one

OU

def func(a,b):
    return b ** a
print (func(b=2,2))
SyntaxError: positional argument follows keyword argument

	
# faire une somme
def sum(a, b, c): 
    print(a, "+", b, "+", c, "=", a + b + c)
sum(1,2,3)
1 + 2 + 3 = 6


# definir une adresse
def address(street, city, postalCode):
    print("Your address is:", street, "St.,", city, postalCode)

s = input("Street: ")
pC = input("Postal Code: ")
c = input("City: ")

address(s, c, pC)
Street: eugene
Postal Code: 
Street: eugene
Postal Code: 92150
City: rueil
Your address is: eugene St., rueil 92150


# return

doit etre place à la fin
def hi():
    return
    print("Hi!") # pas pris en compte
none


# return without an expression
def happyNewYear(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes: # donc si wishes = False
        return
    
    print("Happy New Year!")
happyNewYear ()
Three...
Two...
One...
Happy New Year!

OR

def happyNewYear(wishes = False):
ou
if wishes
on aura:

Three...
Two...
One...


# return with an expression

def boringFunction():
    return 123
x = boringFunction()
print("The boringFunction has returned its result. It's:", x)
The boringFunction has returned its result. It's: 123

!! We can ignore the return result !!
ex:
def boringFunction():
    print("'Boredom Mode' ON.")
    return 123
print("This lesson is interesting!)
boringFunction()
print("This lesson is boring...")
This lesson is interesting!
'Boredom Mode' ON.
This lesson is boring... # return value 123 is not used and it is fine

ex: jeu de la fortune
import random
 
v def getAnswer(answerNumber): w     if answerNumber == 1:        return 'It is certain'    elif answerNumber == 2:        return 'It is decidedly so'    elif answerNumber == 3:        return 'Yes'    elif answerNumber == 4:        return 'Reply hazy try again'    elif answerNumber == 5:        return 'Ask again later'    elif answerNumber == 6:        return 'Concentrate and ask again'    elif answerNumber == 7:        return 'My reply is no'    elif answerNumber == 8:        return 'Outlook not so good'    elif answerNumber == 9:        return 'Very doubtful'
 
x r = random.randint(1, 9) y fortune = getAnswer(r) z print(fortune)


# return / none default if no result from the function

def strangeFunction(n):
    if(n % 2 == 0):
        return True
print(strangeFunction(2))
print(strangeFunction(1))
True
None # 1%2 = 1 donc return = None car rien de prevu par la function



## functions et boucles "for"

# donner le double d'un input
def doubles(num):
    """Return the result of multiplying an input number by 2."""
    return num * 2
my_num = float(input("give me a number: "))
for i in range(0, 3):
    my_num = doubles(my_num)
    print(my_num)

give me a number: 2
4.0
8.0
16.0

#illustrer les resultats d'un investissement
#display a welcome message
print("Welcome to the Future Value Calculator")
print()
def invest(amount, rate, years):
    for i in range(1, years+1):
        amount = amount * (1 + (rate/100))
        print(f"year {i}: ${amount:,.2f}")
        print()
amount = float(input("How much do you want to invest? "))
rate = float(input("At each rate? "))
years = int(input("For how many years? "))
invest(amount, rate, years)
print("Bye!")

Welcome to the Future Value Calculator

How much do you want to invest? 1000
At each rate? 5
For how many years? 6
year 1: $1,050.00

year 2: $1,102.50

year 3: $1,157.62

year 4: $1,215.51

year 5: $1,276.28

year 6: $1,340.10

Bye!

# list comme parameter d'une function

def sumOfList(lst):
    sum = 0
    for elem in lst:
        sum += elem
    return sum
print(sumOfList([5, 4, 3]))
12

!! do not use this with an integer as it is not intended to be etirated by a for loop

def sumOfList(lst):
    sum = 0
    
    for elem in lst:
        sum += elem
    
    return sum
print(sumOfList(5)
File "main.py", line 9
    
                      ^
SyntaxError: unexpected EOF while parsing


def hiEverybody(myList):
    for name in myList:
        print("Hi,", name)

hiEverybody(["Adam", "John", "Lucy"])
Hi, Adam
Hi, John
Hi, Lucy

!! ON NE PEUT PAS DEL les elm d une list dans un function
list = ['mary','has', 'a,', 'little','lamb']
def list(lst):
    del list[3]
    lst[3] = 'ram'
print (list(list))
TypeError: 'function' object does not support item deletion

# list comme result d'une function

def strangeListFunction(n):
    strangeList = []
    
    for i in range(0, n):
        strangeList.insert(0, i)
    
    return strangeList

print(strangeListFunction(5))
[4, 3, 2, 1, 0]


def createList(n):
    myList = []
    for i in range(n):
        myList.append(i)
    return myList

print(createList(5))
[0, 1, 2, 3, 4]


# function pour determiner si une année est leap ou non + comparer les results à des pre-results pour checker si le code est bon

def isYearLeap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

testdata = [1900, 2000, 2016, 1987]
testresults = [False, True, True, False]
for i in range(len(testdata)):
	yr = testdata[i]
	print(yr,"-> ",end="")
	result = isYearLeap(yr)
	if result == testresults[i]:
		print("OK")
	else:
		print("Failed")
1900 -> OK
2000 -> OK
2016 -> OK
1987 -> OK



# function pour determiner le nombre de jours en donnant un mois et une année + comparer les results à des pre-results pour checker si le code est bon

def isYearLeap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

def daysInMonth(year,month):
	if year < 1582 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]
	if month == 2 and isYearLeap(year):
		res = 29
	return res

testyears = [1900, 2000, 2016, 1987]
testmonths = [ 2, 2, 1, 11]
testresults = [28, 29, 31, 30]
for i in range(len(testyears)):
	yr = testyears[i]
	mo = testmonths[i]
	print(yr,mo,"-> ",end="")
	result = daysInMonth(yr, mo)
	if result == testresults[i]:
		print("OK")
	else:
		print("Failed")
		

# Determiner je jour de l'année en fonction du trio annee/mois/jour		
		

def isYearLeap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

def daysInMonth(year, month):
	if year < 1582 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]
	if month == 2 and isYearLeap(year):
		res = 29
	return res

def dayOfYear(year, month, day):
	days = 0
	for m in range(1, month):
		md = daysInMonth(year, m)
		if md == None:
			return None
		days += md
	md = daysInMonth(year, month)
	if day >= 1 and day <= md:
		return days + day
	else:
		return None

print(dayOfYear(2000, 12, 31))


# Determiner les nombres premiers

def isPrime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

for i in range(1, 20): # nombres premiers inferieurs à 20
    if isPrime(i + 1):
        print(i + 1, end=" ")
print()


# Changer la consommation nbreLitres/100km en gallons/mile

# 1 American mile = 1609.344 metres
# 1 American gallon = 3.785411784 litres

def l100kmtompg(litres):
    gallons = litres / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons

def mpgtol100km(miles):
    km100 = miles * 1609.344 / 1000 / 100
    litres = 3.785411784
    return litres / km100

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
60.31143162393162
31.36194444444444
23.52145833333333
3.9007393587617467
7.490910297239916
10.009131205673757


# Calcul du BMI - simple

def bmi(weight, height):
    return weight / height ** 2

print(bmi(52.5, 1.65))
19.283746556473833


# Calcul du BMI - avec ajout d'une function de conversion lb to kg et feet to main

def ftintom(ft, inch = 0.0): # inch = 0.0 --> default value si aucune n'est donnée
    return ft * 0.3048 + inch * 0.0254

def lbstokg(lb):
    return lb * 0.45359237

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200: # Condition d'exclusion
        return None
    
    return weight / height ** 2

print(bmi(weight = lbstokg(176), height = ftintom(5, 7)))
27.565214082533313


# Determiner si on a un triangle 

def isItATriangle(a, b, c):
    if a + b <= c:
        print ("it cannot be a triangle")
        return False
        
    if b + c <= a:
        print ("it cannot be a triangle")
        return False
        
    if c + a <= b:
        print ("it cannot be a triangle")
        return False
            			
    return True
    print ("it is a triangle !")

print(isItATriangle(1, 1, 1))
print(isItATriangle(1, 1, 3))
it is a triangle !
True
it cannont be a triangle
False

OR simpler

def isItATriangle(a, b, c):
    if a + b > c and b + c > a and c + a > b == True:
        return ("it is a triangle")
    else:
        return ("it cannot be a triangle")
    
print(isItATriangle(1, 1, 1))
print(isItATriangle(1, 1, 3))
it is a triangle
it cannot be a triangle


# Determiner si on a un triangle à angle droit

def isItATriangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def isItRightTriangle(a, b, c):
    if not isItATriangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    # pourquoi n'a-t-on pas besoin de la ligne avec b >a et c ????

print(isItRightTriangle(5, 3, 4))
print(isItRightTriangle(1, 4, 3))


# Determiner la somme d'un produit factoriel

def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

for n in range(1, 6): # testing
    print(n, factorialFun(n))
1 1
2 2
3 6
4 24
5 120	

# Afficher les nombres de Fibonacci --> Fib(i) = Fib(i-1) + Fib(i-2)
def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum

for n in range(1, 10): # testing
    print(n, "->", fib(n))
1 -> 1
2 -> 1
3 -> 2
4 -> 3
5 -> 5
6 -> 8
7 -> 13
8 -> 21
9 -> 34

OR simpler

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2) #
for n in range(1, 10):
    print(n, "->", fib(n))
1 -> 1
2 -> 1
3 -> 2
4 -> 3
5 -> 5
6 -> 8
7 -> 13
8 -> 21
9 -> 34


# Exemple de boucle et correction avec insertion d'une termination condition

#SANS
def fun(a):
    return a + fun(a + 3)

print(fun(25))
...
[Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded

#AVEC
def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)

print(fun(25))
56  # 25 + 28 + fun(31)=3 --> 56


# Exception handling

def spam(divideBy):
    return 42 / divideBy
print(spam(2)) 
print(spam(12)) 
print(spam(0)) # erreur due au fait qu on ne peut pas diviser par 0
print(spam(1))

def spam(divideBy):
    try:
    	return 42 / divideBy    
	except ZeroDivisionError: 
	    print('Error: Invalid argument.')
print(spam(2)) 
print(spam(12)) 
print(spam(0)) 
print(spam(1))
21.0 
3.5 
Error: Invalid argument. # msg d erreur mais le programme continue
None 
42.0

OU

def spam(divideBy):    
    return 42 / divideBy
try:
    print(spam(2))    
	print(spam(12))    
	print(spam(0))    
	print(spam(1)) 
except ZeroDivisionError:    
	print('Error: Invalid argument.')
21.0 
3.5 
Error: Invalid argument. # ca ne continuera pas sur print(spam(1)), 
                         # car le code passe a except pour spam(0) et ne remontera pas 


# afficher vendors

def print_vendor(net_vendor):
    print(net_vendor)

vendors = ['arista', 'juniper', 'big_switch', 'cisco']
for vendor in vendors:
    print_vendor(vendor)

arista
juniper
big_switch
cisco



# generer configuration

#devices = [{'hostname' : 'switch1' , 'ip' : '1'},{'hostname' : 'switch2' , 'ip' : '2'},{'hostname' : 'switch3' , 'ip' : '3'}]
devices = ['switch1', 'switch2', 'switch3']
vlans = [{'id': '10', 'name': 'USERS'}, {'id': '20', 'name': 'VOICE'},{'id': '30', 'name': 'WLAN'}]

def get_commands(vlan, name):
    commands = []
    commands.append('vlan ' + vlan)
    commands.append('name ' + name)
#    commands.append('exit')
#    commands.append('interface ' + vlan)
#    commands.append('ip address 10.10' + vlan + ip)

    return commands

def push_commands(device, commands):
    print('Connecting to device: ' + device)
    for cmd in commands:
        print('Sending command: ' + cmd)

for vlan in vlans:
    id = vlan.get('id')
    name = vlan.get('name')
#    ip = vars
    print('\n')
    print('CONFIGURING VLAN:' + id)
    commands = get_commands(id, name)
    for device in devices:
        push_commands(device, commands)
        print('\n')



