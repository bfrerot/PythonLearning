import csv
import time

# Lecture avec list comprehension
start_time = time.time()

with open('C:\PythonLearning\projects\LIST_vs_GENERATOR_for_file_anlalysis\\test_large.csv', 'r') as f:
    reader = csv.DictReader(f)
    lignes = [row for row in reader]  # tout charger en mémoire

# Exemple de traitement : compter combien de lignes ont 'id' pair
compteur = sum(1 for row in lignes if int(row['id']) % 2 == 0)

print(f"List comprehension : {compteur} lignes avec 'id' pair")
print(f"Temps écoulé : {time.time() - start_time:.2f} secondes")
