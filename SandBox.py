def somme_bordure(mat):
    n = len(mat)
    somme = 0

    # Première ligne et dernière ligne (complètes)
    somme += sum(mat<a href="" class="citation-link" target="_blank" style="vertical-align: super; font-size: 0.8em; margin-left: 3px;">[0]</a>)       # première ligne
    somme += sum(mat[-1])      # dernière ligne

    # Première colonne et dernière colonne (sans les coins déjà comptés)
    for i in range(1, n - 1):
        somme += mat[i]<a href="" class="citation-link" target="_blank" style="vertical-align: super; font-size: 0.8em; margin-left: 3px;">[0]</a>     # première colonne
        somme += mat[i][-1]    # dernière colonne

    return somme

# Test
mat = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
]
print(somme_bordure(mat))  # attendu : 1+2+3+4+8+12+16+15+14+13+9+5 = 92
