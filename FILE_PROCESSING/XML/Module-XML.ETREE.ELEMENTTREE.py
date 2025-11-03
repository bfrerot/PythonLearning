########## XML.ETREE.ELEMENTTREE MODULE ##########

## xml.etree.ElementTree has a very simple API for analyzing and creating XML data
# It's an excellent choice for people who have never worked with the Document Object Model (DOM) before

# Extensible Markup Language (XML) is a markup language intended for storing and transporting data
# One of its main advantages is the ability to define our own tags that make the document more readable to humans
# XML is a standard recommended by the W3C organization


## prolog 
# first (optional) line of the document
# We can specify character encoding, e.g., <?xml version="1.0" encoding="ISO-8859-2"?> changes the default character encoding (UTF-8) to ISO-8859-2

## root element 
# XML document must have one root element that contains all other elements

## elements 
# consist of opening and closing tags
# Elements include text, attributes, and other child elements

## attributes 
# placed in the opening tags
# consist of key-value pairs, ex: title = "The Little Prince"

'''
<?xml version="1.0"?>                # prolog 
<data>                               # root element OPENING TAG
<book title="The Little Prince">     # element n with attribute
<author>Antoine de Saint-Exupéry</author>
<year>1943</year>
</book>                              # element n CLOSING TAG
<book title="Hamlet">
<author>William Shakespeare</author>
<year>1603</year>
</book>
</data>                              # root element CLOSING TAG
'''


## parse()

import xml.etree.ElementTree as ET

tree = ET.parse('books.xml') # parses the XML file and returns an ElementTree object
root = tree.getroot() # retrieves the root element of the XML document
print('The root tag is:', root.tag) # The root tag is: data
# The root tag is: data
print('The root has the following children:') 
# The root has the following children:
for child in root:
    print(child.tag, child.attrib)
# book {'title': 'The Little Prince'}
# book {'title': 'Hamlet'}
    print(child)
# <Element 'book' at 0x000001DA32D474C0>
# <Element 'book' at 0x000001DA32D475B0>



## fromstring()

# option 1: all xml code in 1 line

import xml.etree.ElementTree as ET

root = ET.fromstring('<?xml version="1.0" encoding="UTF-8"?><data><book title="The Little Prince"><author>Antoine de Saint-Exupéry</author><year>1943</year></book><book title="Hamlet"><author>William Shakespeare</author><year>1603</year></book></data>')
print('The root tag is:', root.tag)
# The root tag is: data
print('The root has the following children:')
# The root has the following children:
for child in root:
    print(child.tag, child.attrib)
# book {'title': 'The Little Prince'}
# book {'title': 'Hamlet'}


# option 2: using triple quotes for multi-line string

import xml.etree.ElementTree as ET

xml_string = '''<?xml version="1.0" encoding="UTF-8"?>
<data>
    <book title="The Little Prince">
        <author>Antoine de Saint-Exupéry</author>
        <year>1943</year>
    </book>
    <book title="Hamlet">
        <author>William Shakespeare</author>
        <year>1603</year>
    </book>
</data>'''

root = ET.fromstring(xml_string)
print('The root tag is:', root.tag)
print('The root has the following children:')
for child in root:
    print(child.tag, child.attrib)
    

# option 3: parentheses for multi-line string

import xml.etree.ElementTree as ET

xml_string = (
    '<?xml version="1.0" encoding="UTF-8"?>'
    '<data>'
        '<book title="The Little Prince">'
            '<author>Antoine de Saint-Exupéry</author>'
            '<year>1943</year>'
        '</book>'
        '<book title="Hamlet">'
            '<author>William Shakespeare</author>'
            '<year>1603</year>'
        '</book>'
    '</data>'
)


# Option 4: backslash

xml_string = '<?xml version="1.0" encoding="UTF-8"?>' \
             '<data>' \
             '<book title="The Little Prince">' \
             '<author>Antoine de Saint-Exupéry</author>' \
             '</book>' \
             '</data>'


## iteration

# we can access elements directly using indexes
# if index does not exist ==> IndexError: child index out of range

import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()
print("My books:\n")
for book in root:
    print('Title: ', book.attrib['title'])
    print('Author:', book[0].text)
    print('Year: ', book[1].text, '\n')
'''
My books:

Title:  The Little Prince
Author: Antoine de Saint-Exupéry
Year:  1943

Title:  Hamlet
Author: William Shakespeare
Year:  1603

'''


# iter()

import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()
for author in root.iter('author'):
    print(author.text)
# Antoine de Saint-Exupéry
# William Shakespeare


# findall()
# only searches the children at the first nesting level
# also accepts an XPath expression

import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()
for x in root.findall('book'):
    print(x.get('title'))
# The Little Prince
# Hamlet

import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()
for x in root.findall('author'):
    print(x.text)
# ==> finds nothing


# find()
# returns the first matching element    

import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()
print(root.find('book').get('title'))
# The Little Prince