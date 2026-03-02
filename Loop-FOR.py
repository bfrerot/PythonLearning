##########  FOR  ##########



### print i if i in ITERABLE_thing

animals = ['girafe','tiger','monkey','mouse']
for i in animals:   #  for each iteration "i" in the list "animals"
	print (i)       # print l'itération "i"
#girafe
#tiger
#monkey
#mouse

# we can iterate thru: 
#       a letter or a word
#       a word including number(s) AFTER the 1st character
#       underscore "_"

animals = ['girafe','tiger','monkey','mouse']
for any in animals:   
	print (any)  

animals = ['girafe','tiger','monkey','mouse']
for _ in animals: 
	print (_)   
 
animals = ['girafe','tiger','monkey','mouse']
for 3 in animals:  
	print (3)
# SyntaxError: cannot assign to literal

animals = ['girafe','tiger','monkey','mouse']
for ! in animals:
	print (!) 
# SyntaxError: invalid syntax  



### ITERATOR value
# it keeps its last value after the loop has ended
for i in range(3):
    print(i, end=" ")
    
print(i)
# 0 1 2 2

for j in range(5):
    pass
print(j)
# 4    last value of j in the for loop


# contrairement à une boucle for DANS une fonction
def boucle():
    for i in range(3):
        print(i, end=" ")
boucle()
# 0 1 2

# Ici, `i` n'existe pas en dehors de la fonction
try:
    print(i)
except NameError:
    print("La variable 'i' n'existe pas ici")
# 0 1 2 La variable 'i' n'existe pas ici



### NESTED loop = a loop into a loop into a loop etc etc
for n in range(1, 4):
    for j in range(4, 7):
        print(f"n = {n} and j = {j}") # f-string
#n = 1 and j = 4
#n = 1 and j = 5
#n = 1 and j = 6
#n = 2 and j = 4
#n = 2 and j = 5
#n = 2 and j = 6
#n = 3 and j = 4
#n = 3 and j = 5
#n = 3 and j = 6

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)
#red apple
#red banana
#red cherry
#big apple
#big banana
#big cherry
#tasty apple
#tasty banana
#tasty cherry



### INFINITE LOOP

data = ['peter', 'paul', 'mary']
for d in data:
    data.append(d.upper()) # la list va augementer sans arret
    print(data)
    
    
    
### USE CASES

# print i if i in string + add a space
exampleString = 'silly walks'
for ix in range(len(exampleString)):
  print(exampleString[ix], end=' ')
#s i l l y   w a l k s


# print i in list by indexation
animals = ['girafe','tiger','monkey','mouse']
for i in animals[1:3]: # indexation
    print (i)
#tiger
#monkey


# print i in list by indexation + range()
animals = ['girafe','tiger','monkey','mouse']
for i in range(4): # On peut melanger avec du range pour n'afficher qu'une partie ou tout
	print (animals[i]) # 0,1,2,3
#girafe
#tiger
#monkey
#mouse


# print i in list + its index using enumerate()
animals = ['girafe','tiger','monkey','mouse']
for i, ani in enumerate(animals): # enumerate() gives the object + its index
	print (i,ani)
#0 girafe
#1 tiger
#2 monkey
#3 mouse 

print(enumerate(animaux))
# <enumerate object at 0x0000010E5DF093F0>

vendors = ['arista', 'juniper', 'big_switch', 'cisco']
for index, each in enumerate(vendors):
    print(str(index) + ' ' + each) # index is a integer so we need to change it in a str to add it with each 'vendors'
#0 arista
#1 juniper
#2 big_switch
#3 cisco


# to know 2^n values with n in range(x)
pow = 1
for exp in range(16):
    print("2 to the power of", exp, "is", pow)
    pow *= 2
#2 to the power of 0 is 1
#2 to the power of 1 is 2
#2 to the power of 2 is 4
#2 to the power of 3 is 8
#2 to the power of 4 is 16
#2 to the power of 5 is 32
#2 to the power of 6 is 64
#2 to the power of 7 is 128
#2 to the power of 8 is 256
#2 to the power of 9 is 512
#2 to the power of 10 is 1024
#2 to the power of 11 is 2048
#2 to the power of 12 is 4096
#2 to the power of 13 is 8192
#2 to the power of 14 is 16384
#2 to the power of 15 is 32768


# to count and add a word (123 soleil)
import time
for second in range(1,6): 
    print(second, "Mississippi")
    time.sleep(3) # add an unseen counter between each iteration, here = 3s
print("Ready or not, here I come!")
#1 Mississippi
#..3sec
#2 Mississippi
#..3sec
#3 Mississippi
#..3sec
#4 Mississippi
#..3sec
#5 Mississippi


# Rebuild a string
user_word = input("Give me a word: ")
user_word = user_word.upper()  # Convert in UPPER case
forbidden_letter = ['I', 'O', 'U', 'E', 'A']  # create a list of "forbidden" letters
result = ""  # store the final value
for letter in user_word: 
    if letter not in forbidden_letter:  # we keep only non-forbidden letters
        result += letter
print(result)
#Give me a word: GREGORY
#GRGRY


# Share money or bill
amount = float(input("Enter an amount: "))
for num_people in range(2, 6):
    print(f"{num_people} people: ${amount / num_people:,.2f} each")
#Enter an amount: 100
#2 people: $50.00 each
#3 people: $33.33 each
#4 people: $25.00 each
#5 people: $20.00 each