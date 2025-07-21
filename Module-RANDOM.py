########## RANDOM MODULE ##########


# RANDOM module delivers some mechanisms allowing to operate with pseudorandom numbers

# a random number generator takes a value called a seed, treats it as an input value, calculates a "random" number based on it 
# the method depends on the chosen algorithm and produces a new seed value
# The length of a cycle in which all seed values are unique may be very long, but it is finite
# sooner or later the seed values will start repeating and the generating values will repeat as well
# The initial seed value, set during the start of the program, determines the order in which the generated values will appear



### seed() 
# function which directly sets the generator's seed
# Possible variants of its invocation are:
#   seed() ==> sets the seed with the current time which makes the seed a bit unpredictable
#   seed(int_value) ==> sets the seed with the integer value int_value

import random
random.seed(0) # The code will always print the same value, regardless of the number of launches.
print(random.random())
# 0.8444218515250481
import random
random.seed(0) # try 2
print(random.random())
# 0.8444218515250481
import random
random.seed(0) # try 3
print(random.random())
# 0.8444218515250481

from random import random, seed
seed(0)
for i in range(5):
    print(random())
0.8444218515250481
0.7579544029403025
0.420571580830845
0.25891675029296335
0.5112747213686085
# apply code again
0.8444218515250481
0.7579544029403025
0.420571580830845
0.25891675029296335
0.5112747213686085
# same values each time



### random() 
# produces a float number x, which falls within the range 0.0 ≤ x < 1.0

import random
print(random.random())
# 0.7579544029403025

from random import random
for i in range(5):
    print(random())
0.3487027093205528
0.04681702702249857
0.3734602288166339
0.9930295466333776
0.023790533052207796



### random.randrange(start, stop ,step)
# produces an integer number x, which is taken from the range start ≤ x < stop with step 
# start argument defaults to 0 
# step argument defaults to 1

from random import randrange
print(randrange(10)) 
# 9
print(randrange(10))
# 4
print(randrange(3, 10)) 
#7
print(randrange(3, 10))
# 6
print(randrange(3, 10, 2))
# 3
print(randrange(3, 10, 2))
# 5



### random.randint(start, stop) 
# stop inclus

from random import randrange, randint
print(randint(0, 2))
# soit 0 soit 1 soit 2

import random 
secretNumber = random.randint(1, 20)
print (secretNumber)
# 13
print (secretNumber) # ne change pas tant qu on ne remet pas l egalite
# 13
secretNumber = random.randint(1, 20)
print (secretNumber)
# 12
secretNumber = random.randint(1, 20)
print (secretNumber) # equal to (left,right + 1)
# 7



### random.choice(liste, tuple, string)

from random import choice
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tup = 20,23,24
var = "palestine"
print(choice(lst)) # 1 element de la list
# 9
print(choice(tup)) # 1 elem du tuple
# 23
print(choice(var))
# a



### random.sample(lst/tupple/string,int)
from random import sample
print(sample(lst, 5))    #   5 elements de la liste dans un sens au hasard
[10, 9, 8, 1, 4]
print(sample(lst, 10))     #   10 elements de la liste dans un sens au hasard
[4, 10, 5, 2, 7, 3, 9, 6, 1, 8]