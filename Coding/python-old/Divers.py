### ------- Divers -------

# this is a comment
# on peut selectionner une ligne et taper CTRL + / pour aouter /enlever le  # 

''' 
for larger 
multilines 
comments
'''

/ a la fin de la ligne continue la commande la ligne suivante (longue commande)

; permet d aligner plusieurs commandes sur une meme ligne



------- Mots reservés par Python -------


and
 
del
 
from
 
None
value = None
if value == None:
   print("Sorry, you don't carry any value")
 
True
 

as
 
elif
 
global # sert à exporter la valeur d'une variable hors d'une function
def myFunction():
    global var
    var = 2
    print("Do I know that variable?", var)
var = 1 # 1 ecrase 2
myFunction() # 2 ecrase 1 (global feature)
Do I know that variable? 2
2
 
nonlocal
 
try
 

assert
 
else
 
if
 
not
 
while
 

break
 
except
 
import
 
or
 
with
 

class
 
False
type(False)
<type 'bool'>
 
in
 
pass
 
yield
 

continue
 
finally
 
is
 
raise
 
async
 

def
 
for
 
lambda
 
return
 
await
 


async et await a partir de version 3.5