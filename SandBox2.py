for i in range( 1, n - 1): # range exclut le n-1, donc prend en compte de 1 à n-2


    
    somme += mat[i][0]    # pour chaque ligne, on prend le 1er élément
    somme += mat[i][-1]   # pour chaque ligne, on prend le dernier élément