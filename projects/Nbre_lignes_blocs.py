# Trouver le nombre de lignes sachant que chaque ligne a "x" brique de + que celle d'au-dessus (mur de briques) 
# et si manque de brique pour completer une rangée on arrete et on ne compte que les rangées pleines.
blocks = int(input("Enter the number of blocks: "))
height = 0
inlayer = 1
while inlayer <= blocks:
    height += 1
    blocks -= inlayer
    inlayer += 1 # 1 brique de plus
print("The height of the pyramid:", height)
#Enter the number of blocks: 28
#The height of the pyramid: 7

def pyramid_height(blocks):
    height = 0
    layer = 1  # Le premier rang nécessite 1 bloc
    while blocks >= layer:
        blocks -= layer  # Déduire les blocs nécessaires pour ce rang
        height += 1  # Incrémenter la hauteur puisque ce rang peut être construit
        layer += 2  # Le prochain rang nécessite 2 blocs de plus que le précédent
    return height
blocks = int(input("Entrez le nombre de blocs : "))
print("Hauteur de la pyramide :", pyramid_height(blocks))
#Entrez le nombre de blocs : 17
#Hauteur de la pyramide : 4