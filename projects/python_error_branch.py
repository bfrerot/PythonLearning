def print_exception_tree(thisclass, nest = 0): 
# Paramètre thisclass : la classe dont on veut afficher les sous-classes.
# Paramètre nest : indique le niveau d'imbrication pour le rendu graphique (initialement 0)
    if nest > 1:
        print("   |" * (nest - 1), end="") # si plus de 1 sous-class, on met tab "   |" (n-1) fois
    if nest > 0:
        print("   +---", end="") # dès lors qu'on est dans une sous class de la class visée, on ajoute "   +---"

    print(thisclass.__name__) # imprime le nom de la class, sans le .__name__ on aurait "<class 'ImportError'>"

    for s in thisclass.__subclasses__(): # RECURSION, pour chaque subclass de la class visée
        print_exception_tree(s, nest + 1) # la fonction s'appelle elle-même en augmentant nest de 1, cela permet de parcourir toute la hiérarchie

print_exception_tree()