########## WHILE ##########



### simple loop + incrementation

spam = 0
while spam < 5:  
  print('Hello, world.')
  spam = spam + 1  # to avoid INFINITE LOOP
#Hello, world.
#Hello, world.
#Hello, world.
#Hello, world.
#Hello, world.

i = 1
while i <= 4:
  print (i)
  i = i+1 # to avoid INFINITE LOOP
#1
#2
#3
#4

#INSERT A COUNTER TO EXIT FROM THE LOOP
counter = 5
while counter: # = while counter !=0:
    print("Inside the loop.", counter)
    counter -= 1	
print("Outside the loop.", counter)
#Inside the loop. 5
#Inside the loop. 4
#Inside the loop. 3
#Inside the loop. 2
#Inside the loop. 1
#Outside the loop. 0


### WHILE NOT
# condition IS not name ==> continues as long as the variable name is False or empty
# In Python, an empty chain ('') is considered falsy meaning False
# not name sera True when name is empty

name = '' 
while not name:
  print('Enter your name:') 
  name = input() 
print('How many guests will you have?') 
numOfGuests = int(input())
if numOfGuests: # means !=0 
  print('Be sure to have enough room for all your guests.')
print('Done')
#Enter your name:# no name + Enter --> the loop restart
#
#Enter your name:
#benoit
#How many guests will you have?
#1
#Be sure to have enough room for all your guests.
#Done



### IF/BREAK

i = 1
while i < 6:
  print(i)
  if (i == 3):
    break # we go out from the loop and i += 1 below is not applied
  i += 1
print(i) # REMINDR, i keeps its last value at the end of the loop
#1
#2
#3
#3


word = input('Enter a word: ')
while word != 'chupacabra':
    word = input ('Enter a word: ')
    if word == 'chupacabra':
        break
print ('You\'ve successfully left the loop.')
# Enter a word: oiu
# Enter a word: chupacabra
# You've successfully left the loop.



# IF/ELIF/ELSE

wordwithoutvowel=''
userword = input('Please enter any word: ')    # gregory
print (userword)                               # gregory
userword = userword.upper()
print (userword)                               # GREGORY
for letter in userword:
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else:
        wordwithoutvowel = wordwithoutvowel + letter

print (wordwithoutvowel)
#GRGRY



### Use cases

word = "Python"
index = 0
while index < len(word):
    print(word[index])
    index = index + 1
#P
#y
#t
#h
#o
#n


# force a user àto give a positive number
num = float(input("Enter a positive number: "))
while num <= 0:
    print("That's not a positive number!")
    num = float(input("Enter a positive number: "))
#Enter a positive number: -9
#That's not a positive number!
#Enter a positive number: -0.99999
#That's not a positive number!
#Enter a positive number:


# Print only odd umbers
x = 1
while x < 11:
    if x%2 != 0:
        print (x,end="")
    x += 1
#13579


# Count odd and even numbers separately
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
#Enter a number or type 0 to stop: 2
#Enter a number or type 0 to stop: 4
#Enter a number or type 0 to stop: 8
#Enter a number or type 0 to stop: 10
#Enter a number or type 0 to stop: 11
#Enter a number or type 0 to stop: 13
#Enter a number or type 0 to stop: 0 ## we go OUT from the WHILE loop
#Odd numbers count: 2
#Even numbers count: 4


# Find the good number or stay blocked for ever
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
number = int(input("Give ma a number: "))
while number!=secret_number:
    print("Ha ha! You're stuck in my loop!") 
    number = int(input("Give ma a number: "))
print("Well done, muggle! You are free now.")
#+================================+
#| Welcome to my game, muggle!    |
#| Enter an integer number        |
#| and guess what number I've     |
#| picked for you.                |
#| So, what is the secret number? |
#+================================+

#Give ma a number: 14
#Ha ha! You're stuck in my loop!
#Give ma a number: 85
#Ha ha! You're stuck in my loop!
#Give ma a number: 4566288
#Ha ha! You're stuck in my loop!
#Give ma a number: 777
#Well done, muggle! You are free now.