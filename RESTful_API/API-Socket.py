########## SOCKET ##########



### Connexion steps
# 1- create a new socket able to handle connection-oriented transmissions based on TCP
# 2- connect the socket to the HTTP server of a given address
# 3- send a request to the server
# 4- receive the server's response
# 5- close the socket



### Importing a socket
# We need a specialized module
# Python offers such a module

import socket



### Obtaining user input
# We need the name of the HTTP server we're going to connect to

server_addr = input("What server do you want to connect to? ")

# user input may can take two different forms:
#   domain name of the server: www.pythoninstitute.org, without the leading http://
#   IP address of the server: 87.98.235.184 + port



### creating a socket
# "socket" module contains all the tools we need to deal with sockets
# It provides a class named socket which encapsulates a bundle of properties and activities related to the actual sockets' behaviour
# This means that the first step is to create an object of the class - this is how we carry out the creation:

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# constructor takes 2*arguments, both declared within the module
# 1st arg is a domain code: AF_INET specifies the Internet socket domain
# 2nd arg is a socket type code: SOCK_STREAM symbol here to specifies a high-level socket able to act as a character device - a device that can handle single characters, 
#   as we are interested in transferring data byte by byte, not as fixed sized blocks 
#   ex: a terminal is a character device, while a disk isn't

# Such a socket is prepared to work on top of TCP protocol - it's the default socket configuration
# If we want to create a socket to cooperate with another protocol, like UDP, we will need to use a different constructor syntax



### Connecting to a server

# we use a socket on the client's side

# The server has a few more steps to take
# Servers are usually more complex than clients as one server serves many clients simultaneously

# The configured socket is able to be connected to its counterpart on the server's side
sock.connect((server_addr, 80))


## .connect()
# it tries to connect your socket to the service of the specified address and port (service) number
# the 2*values are passed to the method as elements of a tuple

# /!\ a pair consisting of the actual address and port number is specific for the INET domain



### GET

# A conversation with the HTTP server consists of:
#   - requests sent by the client 
#   - responses sent by the server
# HTTP defines a set of acceptable requests ==> the request methods or HTTP words
# The method asking the server to send a particular document of a given name is called GET

# ex: to get a root document from a site named www.site.com the client should send the request containing a correctly formed GET method description:
'''
GET / HTTP/1.1\r\n
Host: www.site.com\r\n
Connection: close\r\n
\r\n
'''

# GET method requires:

#   - a line containing the method name (GET) 
#     followed by the name of the resource the client wants to receive
#     => the root document is specified as a single slash (GET /)
#        the line must also include the HTTP protocol version (HTTP/1.1) and must end with the characters \r\n
#                                                                            /!\ note: all lines must end the same way == \r\n

#   - a line containing the name of the site (www.site.com:port) preceded by the parameter name (Host:)

#   - a line containing a parameter named Connection: along with its value close, which forces the server to close the connection after the first request is served
#     an empty line is a request terminator


## .send() + b  AND  .bytes()

sock.send(b"GET / HTTP/1.1\r\nHost: " +
          bytes(server_addr, "utf8") +
          b"\r\nConnection: close\r\n\r\n")


# send() method doesn't natively accept strings 
# this is why we have to use the "b" prefix before the literal parts of the request string 
# it silently translates the string into bytes == immutable vector consisting of values from the range 0..255

# bytes() is used to translate the string variable in the same manner
# second argument specifies the encoding used to store the server's name
# UTF8 seems to be the best choice for most modern OSs


## .recv()

reply = sock.recv(10000)

# recv() method waits for the server's response, gets it, and puts it inside a newly created object of type bytes
#   arg specifies the maximal acceptable length of the data to be received
#       If the server's response is longer than this limit, it will remain unreceived
#       We will need to invoke recv() again as mmany times as needed to get the remaining part of the data


## .shutdown()  AND  .close()

sock.shutdown(socket.SHUT_RDWR)
sock.close()

# Invoking shutdown() is like telling the server we don't need it anymore

# socket.SHUT_RD   == we aren't going to read the server's messages anymore
# socket.SHUT_WR   == we won't say a word anymore
# socket.SHUT_RDWR == specifies the conjunction of the two previous options

# Best practice is to close the connection by expressing it literally with close() method


## .repr()

print(repr(reply))

# takes care of the clear textual presentation of any object



### Server answer

# two separate parts:
#   1st = response header
#       the topmost line is the most important, as is says whether the server sent back the requested document or not
#       there is a very significant three-digit number: 200 == OK

#   2nd = many important details



### socket.gaierror ==> Entering a non-existing/malformed address

# The user has entered a non-existent or malformed address

# ex: address is syntactically correct but doesn't correspond to any existing server
#     address is syntactically INcorrect
'''
What server do you want to connect to? # ==> a.non.existent.name OU anonexistentname
Traceback (most recent call last):
  File "cli.py", line 5, in <module>
    sock.connect((srvaddr, 80))
socket.gaierror: [Errno -2] Name or service not known
'''

# ex: connection refused by the server
'''
What server do you want to connect to? dedicated.server
Traceback (most recent call last):
  File "cli2.py", line 6, in <module>
    sock.connect((srvaddr, 11111))
ConnectionRefusedError: [Errno 111] Connection refused
'''

# The connect function throws an exception named socket.gaierror 
# Its name comes from the name of a low-level function (usually provided not by Python but by the OS kernel) named getaddrinfo()
# The function tries - among others - to find the full address information regarding the received argument


## socket.timeout exception
# This exception is raised when the server's reaction doesn't occur in a reasonable time 
# Reasonable time can be set using a method named settimeout()