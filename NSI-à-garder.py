def voisins_entrants(adj, x):
    voisins = []
    for i in range(len(adj)): # 
        if x in adj[i]:
            voisins.append(i)
    return voisins
adj = [[1, 2], [], [4], [2], [3]]
x=0
print(voisins_entrants(adj, 4))
print(voisins_entrants(adj, 6))


def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]  #  122311 #chiffre = 1
    compte = 1 
    
    for i in range(1, len(s)):  # On commence à 2 car s[0] est déjà dans chiffre
        if s[i] == chiffre:
            compte += 1  # On incrémente le compteur
        else:
            resultat += str(compte) + chiffre  # On ajoute "compte + chiffre"
            chiffre = s[i]  # Nouveau chiffre
            compte = 1      # Reset du compteur
    
    # Ne pas oublier le dernier groupe !
    lecture_chiffre = str(compte) + chiffre
    resultat += lecture_chiffre
    return resultat


def max_et_indice(x):
   max = 0
   index_max = 0
   for i in range(len(x)):
      if x[i] > max:
         max = x[i]
         index_max = i
      
      else:
         pass
   print(index_max, max)

 
imane=[1,4,10,100,22]
max_et_indice(imane)



def ecriture_binaire_entier_positif(n):  # 3
    if n == 0:
        return '0'
    resultat = ''
    while n > 0:
        resultat = str(n % 2) + resultat
        n = n // 2
    return resultat
print(ecriture_binaire_entier_positif(1234567))