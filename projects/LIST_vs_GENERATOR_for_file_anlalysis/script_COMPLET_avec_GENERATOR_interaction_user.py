import csv

def lire_lignes_csv(fichier):
    with open(fichier, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row

# Lecture et affichage interactif
for row in lire_lignes_csv('test_large.csv'):
    input("Appuyez sur Entrée pour voir la ligne suivante...")
    print(row)

