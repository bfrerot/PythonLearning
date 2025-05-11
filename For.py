##########  FOR  ##########


# print i si i in list
animaux = ['girafe','tigre','singe','souris']
for i in animaux:   #  i pour itération, va lister toutes les itérations de la liste
	print (i)
#girafe
#tigre
#singe
#souris


# print i si i in string + ajouter un espace
exampleString = 'silly walks'
for ix in range(len(exampleString)):  #ix pour iteration et autant de fois qu'il y a d'itérations dans le string
  print(exampleString[ix], end=' ')
#s i l l y   w a l k s


# print i in list par indexation
animaux = ['girafe','tigre','singe','souris'] # par indexation
for i in animaux[1:3]: # inclut le premier//exclut le dernier
    print (i)
#tigre
#souris


# print i in list par indexation + usage de range() pour déterminer l'indexation
animaux = ['girafe', 'tigre', 'singe', 'souris']
for i in range(4): # On peut melanger avec du range pour n'afficher qu'une partie ou tout
	print (animaux[i]) # 0,1,2,3
#girafe
#tigre
#singe
#souris
for i in range(2): # 0,1
	print (animaux[i])
#girafe
#tigre


# print i in list et son index + usage de enumerate()
animaux = ['girafe','tigre','singe','souris']
print(enumerate(animaux))
for i, ani in enumerate(animaux): # pour avoir l'element ET l'index
	print (i,ani)
#0 girafe
#1 tigre
#2 singe
#3 souris

vendors = ['arista', 'juniper', 'big_switch', 'cisco']
for index, each in enumerate(vendors):
    print(str(index) + ' ' + each) # l'index étant une integer il faudra le changer en string pour pouvoir additionner avec les valeurs 'vendors'
#0 arista
#1 juniper
#2 big_switch
#3 cisco


# Pour connaitre les valeurs de 2^n avec n compris entre 0 et 15
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


# Pour compter en ajoutant un mot (123 soleil)
import time
for second in range(1,6): # on prend de 1 à 5, dernière valeur exclue
    print(second, "Mississippi")
    time.sleep(3) # ajoute un compte entre chaque occurence, ici 3s
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


# Pour reconstruire un string
user_word = input("Give me a word: ")
user_word = user_word.upper()  # Convertir en majuscules
forbidden_letter = ['I', 'O', 'U', 'E', 'A']  # Liste des lettres interdites
result = ""  # Variable pour stocker le mot sans les lettres interdites
for letter in user_word: 
    if letter not in forbidden_letter:  # On garde les lettres non interdites
        result += letter
print(result)
#Give me a word: GREGORY
#GRGRY


# Partager de l'argent
amount = float(input("Enter an amount: "))
for num_people in range(2, 6):
    print(f"{num_people} people: ${amount / num_people:,.2f} each")
#Enter an amount: 100
#2 people: $50.00 each
#3 people: $33.33 each
#4 people: $25.00 each
#5 people: $20.00 each


# NESTED loop = une loop dans une loop etc
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


# à propos de i
# il va garder sa valeur après la boucle
for i in range(3):
    print(i, end=" ")
print(i)
# 0 1 2 2

for j in range(5):
    pass
print(j)
# 4    car c'est la dernière valeur de la boucle

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