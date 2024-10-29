## -------- FOR -------- ##

animaux = ['girafe','tigre','singe','souris']
for i in animaux:   #  i pour itération, va lister toutes les itérations de la liste
	print (i)
#girafe
#tigre
#singe
#souris


exampleString = 'silly walks'
for ix in range(len(exampleString)):  #ix pour iteration et autant de fois qu'il y a d'itérations dans le string
  print(exampleString[ix], end=' ')
#s i l l y   w a l k s

animaux = ['girafe','tigre','singe','souris'] # par indexation
for i in animaux[1:3]: # inclut le premier//exclut le dernier
    print (i)
#tigre
#souris


animaux = ['girafe', 'tigre', 'singe', 'souris']
for i in range(4): # On peut melanger avec du range pour n'afficher qu'une partie ou tout
	print (animaux[i])
#girafe
#tigre
#singe
#souris
for i in range(2):
	print (animaux[i])
#girafe
#tigre


animaux = ['girafe','tigre','singe','souris']
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


lst = [i for i in range (-1,2)]
print (lst)
#[-1, 0, 1]


lst = [[0,1,2,3] for i in range (2)]
print (lst)
#[0,1,2,3], [0,1,2,3]


# with increment included in the range, default value of the increment is 1
for i in range(2, 8, 3): # increment 3 --> 2...3/4...5...6/7 END because 8 is excluded
    print("The value of i is currently", i)
#The value of i is currently 2
#The value of i is currently 5


# Pour afficher tous les couples key/value
device = {'hostname': 'router1', 'vendor': 'juniper', 'os': '12.1'}
device.pop('os') # on enlève "os" et sa valeur du dictionnaire --> device = {'hostname': 'router1', 'vendor': 'juniper'}
oper = dict(cpu='5%', memory='10%') # on créée un dictionnaire --> oper = {'cpu': '5%', 'memory': '10%'}
print(oper)
device.update(oper) # on ajoute des données au dictionnaire --> device = {'hostname': 'router1', 'vendor': 'juniper', 'cpu': '5%', 'memory': '10%'}
print(device)
for key, value in device.items():
    print(key + ': ' + value)
#{'cpu': '5%', 'memory': '10%'}
#{'hostname': 'router1', 'vendor': 'juniper', 'cpu': '5%', 'memory': '10%'}
#hostname: router1
#vendor: juniper
#cpu: 5%
#memory: 10%


# for/in
print('My name is')
for i in range(5):   
    print('Jimmy Five Times (' + str(i) + ')')
#My name is
#Jimmy Five Times (0)
#Jimmy Five Times (1)
#Jimmy Five Times (2)
#Jimmy Five Times (3)
#Jimmy Five Times (4)

# ATTENTION à l'indentation
total = 0
for num in range(4): 
    total = total + num 
print(total)
#6
total = 0
for num in range(4): 
    total = total + num
    print(total)
#0
#1
#3
#6    


n = range(4)
for num in n:
    print(num - 1)
else:
    print(num)
-1
0
1
2
3 # correspond au else car 4 n'est pas inclut, seulement de 0 à 3


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
        print(f"n = {n} and j = {j}")
#n = 1 and j = 4
#n = 1 and j = 5
#n = 1 and j = 6
#n = 2 and j = 4
#n = 2 and j = 5
#n = 2 and j = 6
#n = 3 and j = 4
#n = 3 and j = 5
#n = 3 and j = 6


# boucle dans la boucle
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