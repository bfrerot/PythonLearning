class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v


for x in I(): # va executer chaque method de la fonction
    print(x,end='') # print le return final snas aller à la ligne, sans espace  
# abc


#  Étape | Action                                   | Résultat / Variable                                   | Affichage            |
# |---------|------------------------------------------|--------------------------------------------------------|----------------------|
# | 1       | Crée instance `I()`                      | `self.i=0`, `self.s='abc'`                              |                      |
# | 2       | Appel `__iter__()`                       | Retourne l'objet lui-même                              |                      |
# | 3       | Appel `__next__()`                       | `i=0`, retourne `'a'`, `i=1`                          | Affiche `'a'`        |
# | 4       | Appel `__next__()`                       | `i=1`, retourne `'b'`, `i=2`                          | Affiche `'b'`        |
# | 5       | Appel `__next__()`                       | `i=2`, retourne `'c'`, `i=3`                          | Affiche `'c'`        |
# | 6       | Appel `__next__()`                       | `i=3`, levée `StopIteration`                          | Fin de la boucle     |
