import xml.etree.ElementTree as ET  # Import avec alias pour simplicité

# Parsing du fichier XML d'entrée
tree = ET.parse('C:/PythonLearning/cars.xml')
cars_for_sale = tree.getroot()

# Suppression de la Ford Mustang
removed = False
for car in cars_for_sale.findall('car'):
    brand = car.find('brand')
    model = car.find('model')
    if brand is not None and brand.text == 'Ford' and model is not None and model.text == 'Mustang':
        cars_for_sale.remove(car)
        removed = True
        break

if removed:
    print("Ford Mustang supprimée avec succès.")
else:
    print("Aucune Ford Mustang trouvée.")

# Création du nouvel élément <car>
new_car = ET.Element('car')
ET.SubElement(new_car, 'id').text = '4'
ET.SubElement(new_car, 'brand').text = 'Maserati'
ET.SubElement(new_car, 'model').text = 'Mexico'
ET.SubElement(new_car, 'production_year').text = '1970'
ET.SubElement(new_car, 'price', {'currency': 'EUR'}).text = '61800'

# Ajout à la racine
cars_for_sale.append(new_car)

# Écriture dans le fichier de sortie (corrigé)
tree.write('newcars.xml', encoding='utf-8', xml_declaration=True, method='xml')
print("Fichier newcars.xml créé avec modifications.")
