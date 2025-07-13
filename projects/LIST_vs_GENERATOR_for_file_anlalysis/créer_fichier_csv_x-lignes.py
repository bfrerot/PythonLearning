import csv

# Créer un fichier CSV avec 10 000 lignes
with open('C:\PythonLearning\projects\LIST_vs_GENERATOR_for_file_anlalysis\\test_large.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    # Écrire l’en-tête
    writer.writerow(['id', 'valeur'])
    # Écrire les données
    for i in range(10000):
        writer.writerow([i, f"valeur_{i}"])
print("Fichier 'test_large.csv' créé avec 10 000 lignes.")
