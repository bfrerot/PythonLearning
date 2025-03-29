# Nombre de caracteres - len()
len('123456789') # compte le nombre de caracteres du string
9
len ('abcd')
4


# Type of data, string/int/float - type()
print (type("homer"))
print (type(234))
<class 'str'>
<class 'int'>


# min() max() function

# min() avec string prendra le code ASCII..

print(min("aAbByYzZ")) # le A est avant le a
A

t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')
[ ] # space =32

 
# list() function

print(list("abcabc"))
['a', 'b', 'c', 'a', 'b', 'c']


# ord() ch() function

ch1 = 'a'
ch2 = ' ' # space
print(ord(ch1)) # ord() = id dans table ascii
print(ord(ch2))
97
32

ch1 = 'α'
ch2 = 'ę' # space
print(ord(ch1))
print(ord(ch2))
945
281

print(chr(97)) # de ASCII vers chr
print(chr(945))
α
ę


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
