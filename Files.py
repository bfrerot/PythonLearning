########## FILEs ##########




#### File NAMES

# Windows uses a different naming convention than the one adopted in Unix/Linux systems
#   Win  ==> name = "\dir\file.ext"
#   Unix ==> name = "/dir/file.ext"

# Python uses the \ as an escape character (like \n)
# Windows file names must be written as follows : name = "\\dir\\file"

# canonical ex = C:\PythonLearning\projects\LIST_vs_GENERATOR_for_file_anlalysis\\test_large.csv

# Unix/Linux system file names are case-sensitive

# two different separators for the directory names: 
#   ==> \ in Windows
#   ==> / in Unix/Linux

# Fortunately, there is also one more solution
# Python is smart enough to be able to convert slashes into backslashes each time it discovers that it's required by the OS
# This means that the following assignments will work with Windows:
# name = "/dir/file"
# name = "c:/dir/file"

# connecting the stream with a file is called opening the file
# disconnecting this link is named closing the file

# the opening of the stream can fail, and it may happen due to several reasons
#   - most common is the lack of a file with a specified name
#   - the program is not allowed to open it
#   - the program has opened too many streams and the specific operating system may not allow 
#     simultaneous opening of more than n files




#### File STREAMs

# open mode = declare the manner in which the stream will be processed
# ==> successful ?
# program will be allowed to perform only the operations which are consistent with the declared open mode

# two basic operations performed on the stream:
#   - read from the stream: the portions of the data are retrieved from the file and placed in a memory area managed by the program (ex:into a variable)
#   - write to the stream: the portions of the data from the memory (ex: a variable) are transferred to the file

# three basic modes used to open the stream:
#   - read mode: a stream opened in this mode allows read operations only; trying to write to the stream will cause an exception UnsupportedOperation
#   - write mode: a stream opened in this mode allows write operations only; attempting to read the stream will cause UnsupportedOperation again
#   - update mode: a stream opened in this mode allows both writes and reads

# The stream behaves almost like a tape recorder
# ==> read something from a stream? a virtual head moves over the stream according to the number of bytes transferred from the stream
# ==> write something to the stream? the same head moves along the stream recording the data from the memory




#### Files HANDLES

# Python assumes that every file is hidden behind an object of an adequate class
# An object of an adequate class is created when you open the file and annihilate it at the time of closing
# Between these two events we can use the object to specify what operations should be performed on a particular stream
# The operations you're allowed to use are imposed by the way in which you've opened the file
# The object comes from IOBase\[RawIOBase ; BufferedIOBase ; TextIOBase]




#### OPEN()

### to invoke the object (the file)

stream = open(file, mode = 'r', encoding = None)


### open()
#   - very first operation performed on the stream
#   - successful, the function returns a stream object
#   - otherwise, an exception is raised, ex:FileNotFoundError


### file = specifies the name of the file to be associated with the stream


### mode = specifies the open mode used for the stream
#   - default opening mode is read in text mode
#   - string filled with a sequence of characters, and each of them has its own special meaning:

## ==> r = open mode: read
#     the stream will be opened in read mode
#     the file associated with the stream must exist and has to be readable, otherwise exception raised

## ==> w = open mode: write
#     the stream will be opened in write mode
#     the file associated with the stream doesn't need to exist
#     if it doesn't exist it will be created
#     if it exists, it will be truncated to the length of zero (erased)
#     if the creation isn't possible (ex: due to system permissions), exception

## ==>a = open mode: append
#     the stream will be opened in append mode
#     the file associated with the stream doesn't need to exist
#     if it doesn't exist, it will be created
#     if it exists the virtual recording head will be set at the end of the file, the previous content of the file remains UNTOUCHED !

## ==> r+ = open mode: read and update
#     the stream will be opened in read and update mode
#     the file associated with the stream MUST EXIST and has to be WRITEABLE, otherwise exception
#     both read and write operations are allowed for the stream

## ==> w+ open mode: write and update
#     the stream will be opened in write and update mode
#     the file associated with the stream doesn't need to exist
#     if it doesn't exist, it will be created
#     the previous content of the file remains UNTOUCHED
#     both read and write operations are allowed for the stream.

# If there is a letter b at the end of the mode string it means that the stream is to be opened in binary mode
# If the mode string ends with a letter t the stream is opened in text mode
# TEXT MODE is the DEFAULT behaviour assumed when no binary/text mode specifier is used
# the successful opening of a file will set the current file position (the virtual reading/writing head) before 
#   the first byte of the file if the mode is not a and after the last byte of the file if the mode is set to a

## encoding = specifies the encoding type, ex:UTF-8 when working with text files
#   - default encoding depends on the platform used
# all the streams are divided into text and binary streams:
#   - TEXT streams are structured in lines, they contain typographical characters (letters, digits, punctuation, etc),
#   arranged in rows (lines), as seen with the naked eye when you look at the contents of the file in the editor
#   - BINARY streams don't contain text but a sequence of bytes of any value, ex: an executable program, an image, 
#   an audio or a video clip, a database file, etc.
#   Because these files don't contain lines, the reads and writes relate to portions of data of any size. 
#   Hence the data is read/written byte by byte, or block by block, where the size of the block usually ranges from one to an arbitrarily chosen value


# ! In Unix/Linux systems, the line ends are marked by a single character named LF (ASCII code 10) designated in Python programs as \n.
# Other operating systems, especially these derived from the prehistoric CP/M system (which applies to Windows family systems, too)
# use a different convention: the end of line is marked by a pair of characters, CR and LF (ASCII codes 13 and 10) which can be encoded as \r\n.

# This ambiguity can cause various unpleasant consequences
# a program responsible for processing a text file, written for Windows, you can recognize the ends of the lines by finding the \r\n characters,
# but the same program running in a Unix/Linux environment can be completely useless, and vice versa
# ==> non-portability
# a program allowing execution in different environments is called portability
# A program endowed with such a trait is called a portable program

# A decision was made to definitely resolve the issue in a way that doesn't engage the developer's attention
# It was done at the level of classes, which are responsible for reading and writing characters to and from the stream. It works in the following way:
# 
# when the stream is open and it's advised that the data in the associated file will be processed as text (or there is no such advisory at all)
# ==> it is switched into text mode
#     during reading/writing of lines from/to the associated file
#       - nothing special occurs in Unix
#       - in Windows a process called a translation of newline characters occurs
#         * when we read a line from the file, every pair of \r\n characters is replaced with a single \n character
#         * during write operations, every \n character is replaced with a pair of \r\n characters
# the mechanism is completely transparent to the program, which can be written as if it was intended for processing Unix/Linux text files only
# the source code run in a Windows environment will work properly


### 3 Exceptions where open() is not needed
import sys # 3 processes included int he sys module

## ==> sys.stdin = standard input
# stdin stream is normally associated with the keyboard, pre-open for reading and regarded as the primary data source for the running programs
# the well-known input() function reads data from stdin by default


## ==> sys.stdout = standard output
# stdout stream is normally associated with the screen, pre-open for writing, regarded as the primary target for outputting data by the running program
# the well-known print() function outputs the data to the stdout stream


# #==> sys.stderr = standard error output
# stderr stream is normally associated with the screen, pre-open for writing, regarded as the primary place 
#   where the running program should send information on the errors encountered during its work



try:
    stream = open("C:\\Users\\User\\Desktop\\File.txt", "rt")
    # Processing goes here.
    stream.close()
except Exception as exc:
    print("Cannot open the file:", exc)
# Cannot open the file: [Errno 2] No such file or directory: 'C:\\Users\\User\\Desktop\\File.txt'

    
try:
    stream = open("C:\\PythonLearning\\data_engineer_skills.txt", "rt", encoding="utf-8")
    # Lire le contenu du fichier
    content = stream.read()
    print(content)
    stream.close()
except Exception as exc:
    print("Cannot open the file:", exc)
# ---

### 1. **Airbyte**
# - **Ressources en ligne** :
#   - [Site officiel](https://airbyte.com/) — Documentation, guides d’utilisation.
#   - [Tutoriel YouTube](https://www.youtube.com/watch?v=H6D3pWwX1JA) — Introduction à Airbyte.
#   - [Blog Airbyte](https://airbyte.com/blog) — Cas d’usage, nouveautés.
# - **Ouvrages** : Aucun ouvrage dédié, mais la documentation est très complète.
# ...
#etc
# ==> OK



#### CLOSE()
stream.close()
# to get rid of the object
# last operation performed on a stream should be closing
# method invoked from within the open stream object: stream.close()
# expects exactly no arguments as the stream doesn't need to be opened
# returns nothing, but raises an IOError exception in case of error

# most developers believe that the close() function always succeeds and thus there is no need to check if it's done its task properly
# This belief is only partly justified:
#   - If the stream was opened for writing and then a series of write operations were performed, it may happen that the data sent 
#     to the stream has not been transferred to the physical device yet due to a mechanism called caching or buffering
#   - Since the closing of the stream forces the buffers to flush them, it may be that the flushes fail and therefore the close() fails too



#### DIAGNOSIS

# IOError object is equipped with a property named errno = error number
try:
    with open("fichier_inexistant.txt", "r") as f:
        content = f.read()
except IOError as exc:
    print(f"Erreur IOError : errno={exc.errno}, message={exc}")
# Erreur IOError : errno=2, message=[Errno 2] No such file or directory: 'fichier_inexistant.txt'

### ==> some classic errors below:

## errno.EACCES 
# → Permission denied
# ex: tryin to open a file with the read only attribute for writing

## errno.EPERM
# → Operation non permise (permissions insuffisantes) 

## errno.EBADF 
# → Bad file number
# ex; trying to operate with an unopened stream

## errno.EEXIST 
# → File exists
# ex: trying to rename a file with its previous name

## errno.EFBIG 
# → File too large
# ex: trying to create a file that is larger than the maximum allowed by the operating system

## errno.EISDIR 
# → Is a directory
# ex: trying to treat a directory name as the name of an ordinary file.

## errno.EMFILE 
# → Too many open files
# ex: trying to simultaneously open more streams than acceptable for your operating system

## errno.ENOENT 
# → No such file or directory
# ex: trying to access a non-existent file/directory

## errno.ESRCH
# → Processus ou objet non trouvé  

## errno.ENOSPC 
# → No space left on device
# no free space on the media

## errno.EIO
# → Erreur d'entrée/sortie

## errno.EINTR
# → Appel système interrompu 



#### Gestion de l'erreur

### try/exept + errno
# errno fournit des constantes pour représenter différents codes d'erreur
# Quand une erreur survient lors de l'ouverture d'un fichier, une exception IOError (ou OSError dans Python 3) est levée
# cette exception possède un attribut errno qui indique le type précis d'erreur

import errno
 
try:
    stream = open("file", "rb")
    print("exists")
    stream.close()
except IOError as e:
    if e.errno == errno.ENOENT:
        print("absent")
    else:
        print("unknown")
# absent


import errno

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        print("The error number is:", exc.errno)
# The file doesn't exist.


### strerror()
# comes from the os module 
# 1 * argument = error number
# returns a string describing the meaning of the error 
    
from os import strerror

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))
# The file could not be opened: No such file or directory



#### Processing files


### Text file - READ()

# ==> text.txt:

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

## avec while
from os import strerror
try:
    counter = 0
    stream = open('text.txt', "rt")
    char = stream.read(1) # char = 1er caractere seulement car 1, les 10 premiers on aurait mis 10
#    print(char) # perso pour m'assurer du premier caractere
    while char != '': # boucle
        print(char, end='') # B
        counter += 1 # counter = 1
        char = stream.read(1) # char = le caractere suivant car read(1), etc jusue la fin de la boucle
    stream.close() # fin du stream
    print("\n\nCharacters in file:", counter) # saute 2 lignes + imprime "Characters in file: valeur de counter"
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno)) # gestion de l'erreur si besoin
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# 
# Characters in file: 131


## avec for
from os import strerror
try:
    counter = 0
    stream = open('text.txt', "rt")
    content = stream.read()
    for char in content:
        print(char, end='')
        counter += 1
    stream.close()
    print("\n\nCharacters in file:", counter)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# 
# Characters in file: 131

#!! reading a terabyte-long file using this method may corrupt your OS



### Text file - READLINE()

# treat the file's contents as a set of lines, not a bunch of characters

from os import strerror

try:
    character_counter = line_counter = 0
    stream = open('text.txt', 'rt')
    line = stream.readline()
    while line != '':
        line_counter += 1
        for char in line:
            print(char, end='')
            character_counter += 1
        line = stream.readline()
    stream.close()
    print("\n\nCharacters in file:", character_counter)
    print("Lines in file:     ", line_counter)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
#
# Characters in file: 131
# Lines in file:      4



### Text file - READLINES()

# tries to read all the file contents, and returns a list of strings, one element per file line


## sans argument
stream = open("text.txt")
print(stream.readlines()) # crée une list de lines
stream.close()
# ['Beautiful is better than ugly.\n', 'Explicit is better than implicit.\n', 'Simple is better than complex.\n', 'Complex is better than complicated.']


## avec argument
stream = open("text.txt")
print(stream.readlines(20))
print(stream.readlines(20))
print(stream.readlines(20))
print(stream.readlines(20))
stream.close()
# ['Beautiful is better than ugly.\n']
# ['Explicit is better than implicit.\n']
# ['Simple is better than complex.\n']
# ['Complex is better than complicated.']

stream = open("text.txt")
print(stream.readlines(1))
print(stream.readlines(1))
print(stream.readlines(1))
print(stream.readlines(1))
stream.close()
# ['Beautiful is better than ugly.\n']
# ['Explicit is better than implicit.\n']
# ['Simple is better than complex.\n']
# ['Complex is better than complicated.']

stream = open("text.txt")
print(stream.readlines(20))
stream.close()
# ['Beautiful is better than ugly.\n']
    
stream = open("text.txt")
print(stream.readlines(40))
stream.close()
# ['Beautiful is better than ugly.\n', 'Explicit is better than implicit.\n']

# un peu fastidieux à régler et ou est l'utilité réelle ?


## avec WHILE

from os import strerror

try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    lines = s.readlines(20) # 20 aléatoire un peu
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# 
# Characters in file: 131
# Lines in file:      4


## avec FOR
# no need of close()
# iteration works (thru for loop here)

from os import strerror

try:
	ccnt = lcnt = 0
	for line in open('text.txt', 'rt'):
		lcnt += 1
		for ch in line:
			print(ch, end='')
			ccnt += 1
	print("\n\nCharacters in file:", ccnt)
	print("Lines in file:     ", lcnt)
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# 
# Characters in file: 131
# Lines in file:      4



### Text file - WRITE()

from os import strerror
try:
	file = open('newtext.txt', 'wt') # A new file (newtext.txt) is created.
	for i in range(10):
		s = "line #" + str(i+1) + "\n"
		for char in s:
			file.write(char)
	file.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))
# ==> crée un fichier "newtext.txt" contenant:
line #1
line #2
line #3
line #4
line #5
line #6
line #7
line #8
line #9
line #10


# en plus simple sans indenter par caractère
from os import strerror
try:
    file = open('newtext.txt', 'wt')
    for i in range(10):
        file.write("line #" + str(i+1) + "\n")
    file.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
# ==> crée un fichier "newtext.txt" contenant:
line #1
line #2
line #3
line #4
line #5
line #6
line #7
line #8
line #9
line #10



### BYTEARRAY

# Amorphous data is data which have no specific shape or form – they are just a series of bytes
# Amorphous data cannot be stored using any of the previously presented means – they are neither strings nor lists
# There should be a special container able to handle such data
# ==> one of them is a specialized class name BYTEARRAY 
#     it's an array containing (amorphous) bytes

data = bytearray(10) # crée un bytearray de 10 bytes
print(data)
# bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00') # fills the whole array with zeros


## Resemble lists in many respects:
#   they are mutable
#   they're a subject of the len() function
#   we can access any of their elements using conventional indexing


## LIMITATIONS:
#   we MUST NOT set any byte array element with a value which is not an integer ==> TypeError exception
#   we are NOT ALLOWED to assign a value that doesn't come from the range 0 to 255 inclusive ==> ValueError exception


data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i
print(data)
# bytearray(b'\n\t\x08\x07\x06\x05\x04\x03\x02\x01')

# bytearray fonctionne principalement avec des valeurs ASCII
# c'est-à-dire des nombres de 0 à 127 qui représentent des caractères ASCII standard
# d'ou:
# \n = 10 ==> en ASCII code saut de ligne = 10
# \t = 9 ==> en ASCII code tabulation = 9

for b in data:
    print(hex(b))
# 0xa
# 0x9
# 0x8
# 0x7
# 0x6
# 0x5
# 0x4
# 0x3
# 0x2
# 0x1


from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

print(data.decode('latin1'))

# Contenu du fichier .bin
# 
# 
# 



### READINTO() - How to read bytes from a stream

# Reading from a binary file requires the use of a specialized method name readinto()
# the method:
#   doesn't create a new byte array object, but fills a previously created one with the values taken from the binary file
#   returns the number of successfully read bytes
#   tries to fill the whole space available inside its argument; 
#     if there are more data in the file than space in the argument, the read operation will stop before the end of the file
#     otherwise:
#           the method's result may indicate that the byte array has only been filled fragmentarily 
#           the result will show you that, too, and the part of the array not being used by the newly read contents remains untouched

