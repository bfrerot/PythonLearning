import csv
import time

def lire_lignes_csv(fichier):
    with open(fichier, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row

# Traitement avec générateur
start_time = time.time()

compteur = 0
for row in lire_lignes_csv('C:\PythonLearning\projects\LIST_vs_GENERATOR_for_file_anlalysis\\test_large.csv'):
    if int(row['id']) % 2 == 0:
        compteur += 1

print(f"Générateur : {compteur} lignes avec 'id' pair")
print(f"Temps écoulé : {time.time() - start_time:.2f} secondes")
