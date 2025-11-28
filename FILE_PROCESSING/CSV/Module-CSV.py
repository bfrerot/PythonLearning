########## CSV MODULE ##########


# Provides functions for reading and writing data in CSV format
# Reading data is done using the reader object
# Writing is done using the writer object



## .reader()
# returns an object that allows us to iterate over each line in the CSV file
# we need to pass a file object to the reader function. For this purpose, we can use a built-in function called open. Look at the code in the editor and run it.

import csv

with open('contacts.csv', newline='') as csvfile: # Open the CSV file
    reader = csv.reader(csvfile) # Create a CSV reader object
print(reader)
# <_csv.reader object at 0x0000018332537EE0>

# The output shows that the reader object has been created successfully
# However, to see the actual data in the CSV file, we need to iterate over the reader object

#=> Iterating over the reader object
import csv

with open('contacts.csv', newline='') as csvfile: # Open the CSV file
    reader = csv.reader(csvfile, delimiter=',') # Create a CSV reader object, delimiter=',' is the default
    for row in reader:
        print(row) # Iterate over each row in the CSV file and print it
'''
['Name', 'Phone']
['mother', '222-555-101']
['father', '222-555-102']
['wife', '222-555-103']
['mother-in-law', '222-555-104']
'''

#=> Joining the elements of each row
import csv

with open('contacts.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(','.join(row)) # Join the elements of each row with a comma and print
'''
Name,Phone
mother,222-555-101
father,222-555-102
wife,222-555-103
mother-in-law,222-555-104
'''

#=> Using the DictReader class
import csv

with open('contacts.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile) # Create a CSV DictReader object
    for row in reader:
        print(row['Name'], ':', row['Phone'])
'''
mother : 222-555-101
father : 222-555-102
wife : 222-555-103
mother-in-law : 222-555-104
'''

import csv

with open('contacts.csv', newline='') as csvfile:
    fieldnames = ['Name', 'Phone'] # Define the field names
    reader = csv.DictReader(csvfile, fieldnames=fieldnames) # Create a CSV DictReader object with field names
    for row in reader:
        print(row['Name'], row['Phone']) # Print the values associated with 'Name' and 'Phone'
'''
Name Phone
mother 222-555-101
father 222-555-102
wife 222-555-103
mother-in-law 222-555-104
'''


## writer()
# Saving data to a CSV file is done using the writer object provided by the csv module
# Takes the same set of arguments as the reader function

import csv

with open('exported_contacts.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) # quotechar and quoting to handle special characters
# Due to csv.QUOTE_MINIMAL, this field will be automatically quoted to preserve the comma as part of the data, not as a delimiter    
    writer.writerow(['Name', 'Phone'])
    writer.writerow(['mother', '222-555-101'])
    writer.writerow(['father', '222-555-102'])
    writer.writerow(['wife', '222-555-103'])
    writer.writerow(['mother-in-law', '222-555-104'])
    writer.writerow(['grandmother, grandfather', '222-555-105']) # Comma in the name
# The above code creates a CSV file named exported_contacts.csv and writes the data to it
# The quotechar and quoting parameters can be used to handle special characters in the data
# ==> csv file
'''
Name,Phone
mother,222-555-101
father,222-555-102
wife,222-555-103
mother-in-law,222-555-104
"grandmother, grandfather",222-555-105"
'''

#=> quoting
# specifies what values should be quoted
# csv.QUOTE_MINIMAL == only values with special characters (such as delimiter or quotechar) will be quoted (default)
# csv.QUOTE_ALL == quotes all values
# csv.QUOTE_NONNUMERIC == quotes only non-numeric values
# csv.QUOTE_NONE == doesn't quote any values. It's not a good idea to set this value if we have special characters that require quoting, because this will raise an error

# NOTE: The quotechar and quoting parameters can also be used in the reader function. See the documentation for more information.


#=> fieldnames and DictWriter

import csv

with open('exported_contacts.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Phone']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader() # Write the header row = field names
    writer.writerow({'Name': 'mother', 'Phone': '222-555-101'})
    writer.writerow({'Name': 'father', 'Phone': '222-555-102'})
    writer.writerow({'Name': 'wife', 'Phone': '222-555-103'})
    writer.writerow({'Name': 'mother-in-law', 'Phone': '222-555-104'})
    writer.writerow({'Name': 'grandmother, grandfather and auntie', 'Phone': '222-555-105'})
    '''
Name,Phone
mother,222-555-101
father,222-555-102
wife,222-555-103
mother-in-law,222-555-104
"grandmother, grandfather",222-555-105"
'''