########## METHOD FILES ##########



### close()
# close the file

f = open('example.txt', 'w')
f.write('Hello')
f.close() 



### detach()
# Split the stream from the buffer

import io
buffer = io.BytesIO(b"binary data")
raw_stream = buffer.detach()



### fileno()
# Gives the file number attributed by the OS

f = open('example.txt', 'r')
print(f.fileno()) 
# 3
f.close()



### flush()
# Checks that all is written in the file, forces the write

f = open('example.txt', 'w')
f.write('Text')
f.flush()
f.close()



### isatty()
# Check if the stream is interactive

import sys
print(sys.stdin.isatty())
# True



### read()
# Reads all the file

f = open('example.txt', 'r')
contenu = f.read()
print(contenu)
# Text
f.close()



### readable()
# Check if the file is readable

f = open('example.txt', 'r')
print(f.readable())  
# True
f.close()



### readline()
# Reads one line at once

f = open('example.txt', 'r')
ligne = f.readline()
print(ligne)
# Ligne1
#
f.close()



### readlines()
# Reaeds all lines in a list

f = open('example.txt', 'r')
lignes = f.readlines()
print(lignes)
# ['Ligne1\n', 'Ligne2\n', 'Ligne3\n', 'Ligne4']
f.close()



### seek(INT)
# Change the read/writing position in the file

# example.txt BEFORE
'''Ligne1
Ligne2
Ligne3
Ligne4'''

f = open('exemple.txt', 'r+')
f.seek(0)  # Return to the first character
f.write('Bonjour Madame') # replace existing text
f.close()

# example.txt AFTER
'''Bonjour Madame
Ligne3
Ligne4'''



### seekable()
# Checks if the file permits a position change

f = open('example.txt', 'r')
print(f.seekable())  
# True
f.close()



### tell()
# Gives the current position in the file

f = open('example.txt', 'r')
print(f.tell())  
# 0
f.read(5)
print(f.tell())  
# 5 == > Position after reading
f.close()



### truncate()
# Resizes the file to the given size

# example.txt BEFORE
'''Ligne1
Ligne2
Ligne3
Ligne4'''

f = open('exemple.txt', 'w')
f.write('12345678') # replaces and writes '12345678'

# example.txt
'''12345678'''

f.truncate(5)  # keeps only '12345'
f.close()

# example.txt AFTER
'''12345'''



### writable()
# Checks i the file is writable

f = open('example.txt', 'w')
print(f.writable())  
# True
f.close()



### write()
# Writes in the file
f = open('example.txt', 'w')
f.write('Bonjour')
f.close()



### writelines()
# Writes lines in the file

f = open('example.txt', 'w')
f.writelines(['Line 1\n', 'Line 2\n', 'Line 3\n'])
f.close()

# example.txt AFTER
'''Line 1
Line 2
Line 3'''