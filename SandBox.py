def somme_bordure(mat):
    n = len(mat)
    somme = 0

    # Je choisis de prendre l'entièreté des 1ére et dernière lignes,pas des colonnes
    somme += sum(mat[0])       # pour calculer la somme des éléments de la 1ère ligne
    somme += sum(mat[-1])      # pour calculer la somme des éléments de la dernière ligne

    # Puis je comptabilise les 1er et dernier éléments des autres lignes
    # Ici n est égal à la "longueur" de la liste de départ, une liste de n elements, eux-memes des listes de n éléments,
    # ce qui donne bien !!!!!!!!!!!!!!!!!une matrice carrée
    for i in range( 1, n - 1): # range exclut le n-1, donc prend en compte de 1 à n-2
        somme += mat[i][0]    # pour chaque ligne, on prend le 1er élément
        somme += mat[i][-1]   # pour chaque ligne, on prend le dernier élément

    return somme


# Test avec une matrice carrée de 4 éléments (4*4)
mat = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
]
print(somme_bordure(mat)) 
102  # le résultat de l'énoncé est faux, ça n'est pas 92 mais 102

print(1+2+3+4+13+14+15+16+5+9+8+12)
