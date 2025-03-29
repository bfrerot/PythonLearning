------- FILEs -------

>>> nomfichier = "test1.txt" --> crée le fichier à l'mpalcement par defaut C:\Python etc
Pour specifier le path, le faire à la création, ex: nomfichier2 = "H:/test2.txt"
>>> fichier = open(nomfichier,'w')
>>> fichier.write("Bonjour à tous!")
>>> fichier.close()
>>> fichier = open(nomfichier,'a')
>>> fichier.write("\nUne deuxieme ligne")
>>> fichier.close()
>>> 