##########  XML in Python ##########


# XML is – like JSON – a universal and transparent carrier of any type of data
# We can use it to store and transfer documents of virtually any type

'''
<?xml version = "1.0" encoding = "utf-8"?>           # declares that the document contains XML text
<!-- cars.xml - List of cars ready to sell -->       # it is a comment: between <!--  AND  --> 
<!DOCTYPE cars_for_sale SYSTEM "cars.dtd">           # contains document being defined + SYSTEM/PUBLIC + DTD URI (Document Type Definition URI)
<cars_for_sale>                                      # ROOT element
   <car>                                              # car id 1 begin tag
      <id>1</id>                                       # element = value
      <brand>Ford</brand>                                 # element = value
      <model>Mustang</model>                              # element = value
      <production_year>1972</production_year>             # element = value
      <price currency="USD">35900</price>                 # element + attribute  = value
   </car>                                              # car id 1 ending tag
   <car>
      <id>2</id>
      <brand>Aston Martin</brand>
      <model>Rapide</model>
      <production_year>2010</production_year>
      <price currency="GBP">32000</price>
   </car>
</cars_for_sale>
'''

'''
cars_for_sale
|
|____ car
|     |_ id:1
|	 |_ brand: Ford
|	 |_ model: Mustang
|	 |_ production_year: 1972
|	 |_ price(USD): 35900
|
|____ car
	|_ id:2
	   |_ brand: Aston Martin
	   |_ model: Rapide
	   |_ production_year: 2010
	   |_ price(GPB): 32500
'''


### import xml

import xml.etree.ElementTree

cars_for_sale = xml.etree.ElementTree.parse('C:/PythonLearning/RESTful_API/cars.xml').getroot()
# xml.etree.ElementTree.parse() == reads the XML document, builds the tree, and returns it
# .getroot() == return root element
print(cars_for_sale.tag)
for car in cars_for_sale.findall('car'):
    print('\t', car.tag)
    for prop in car:
        print('\t\t', prop.tag)
        if prop.tag == 'price':
            print(prop.attrib, end='')
    print(' =', prop.text)
'''
cars_for_sale
         car
                 id
                 brand
                 model
                 production_year
                 price
{'currency': 'USD'} = 35900
         car
                 id
                 brand
                 model
                 production_year
                 price
{'currency': 'GBP'} = 32000
'''


import xml.etree.ElementTree

tree = xml.etree.ElementTree.parse('C:/PythonLearning/RESTful_API/cars.xml')
cars_for_sale = tree.getroot()
for car in cars_for_sale.findall('car'):
    if car.find('brand').text == 'Ford' and car.find('model').text == 'Mustang':
        cars_for_sale.remove(car)
        break

new_car = xml.etree.ElementTree.Element('car')
xml.etree.ElementTree.SubElement(new_car, 'id').text = '4'
xml.etree.ElementTree.SubElement(new_car, 'brand').text = 'Maserati'
xml.etree.ElementTree.SubElement(new_car, 'model').text = 'Mexico'
xml.etree.ElementTree.SubElement(new_car, 'production_year').text = '1970'
xml.etree.ElementTree.SubElement(new_car, 'price', {'currency': 'EUR'}).text = '61800'
cars_for_sale.append(new_car)
tree.write('newcars.xml', method='') # rewrite the result in a new file: newcars.xml
'''
<?xml version='1.0' encoding='utf-8'?>
<cars_for_sale>                                     
   <car>
      <id>2</id>
      <brand>Aston Martin</brand>
      <model>Rapide</model>
      <production_year>2010</production_year>
      <price currency="GBP">32000</price>
   </car>
<car><id>4</id><brand>Maserati</brand><model>Mexico</model><production_year>1970</production_year><price currency="EUR">61800</price></car></cars_for_sale>
'''