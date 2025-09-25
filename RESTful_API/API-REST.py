########## REST ##########


### REST = REpresentational State Transfer

## Representational
# REST uses plain text for representing its data

## State
# Knowledge of classes and objects is useful here:
#   An object contains a set (the most preferable set is a non-empty one) of properties
#   We can say that the values of all the object's properties constitute its state
#   If any of the properties changes its value, it changes the whole object's state
#   Such a change is often called a transition

## Transfer
# The network (not only the Internet) is able to act as a carrier allowing you to transmit states' representations to and from the server.
# Note: not the object, but its states, or actions able to change the states, are subject to the transfer
# We can say that transferring the states enables us to achieve results similar to those caused by method invocations



### BSD (Berkeley Software Distribution) sockets

# BSD = name of a Unix-class operating system, where the sockets were deployed for the very first time
# Standard was adopted by POSIX (a standard of contemporary Unix-class operating systems) as POSIX sockets

# A socket is a kind of end-point
# An end-point is a point where:
#   the data is available to get it from 
#   the data may be sent to
# A Python program can connect to the end-point and use it to interchange messages between itself and another program working somewhere far away on the Internet


## Socket domains
# Initially, BSD sockets were designed to organize communication in two different domains :
#   Unix domain (Unix for short) - a part of BSD sockets used to communicate programs working within one operating system (i.e., simultaneously present in the same computer system)
#   Internet domain (INET in short) - a part of BSD socket API used to communicate programs working within different computer systems, connected together using a TCP/IP network


## Socket address
# The two programs wanting to exchange their data must be able to identify each other - to be precise, they must have the ability to clearly indicate the socket they want to connect through.
# INET domain sockets are identified (addressed) by pairs of values:
#   the IP address of the computer system inside which the socked is located, ex: 10.2.3.200
#   the port number (more often referred to as service number), ex: ssh 22, http 80
#        ==> The socket/service number is a 16-bit long integer number identifying a socket within a particular system
#            there are 65,536 (2 ** 16) possible socket/service numbers



### Protocol
# A protocol is a standardized set of rules allowing processes to communicate with each other
# A protocol stack is a multilayer set of cooperating protocols providing a unified repertoire of services
#   ex: TCP/IP protocol stack is designed to cooperate with networks based on the IP protocol


## IP - Internet Protocol
# able to send a packet of data (a datagram) between two network nodes


## TCP - Transmission Control Protocol
# TCP uses datagrams and handshakes (an automated process of synchronizing the flow of data) to construct a reliable communication channel 
# able to transmit and receive single characters
# TCP is a first-choice protocol for applications where data safety is more important that efficiency (e.g., WWW, REST, mail transfer, etc.)

# Its functionality guarantees that:
#   a stream of data reaches the target, or the sender is informed that communication has failed =>  RELIABILITY
#   data reaches the target intact => INTEGRITY


## UDP - User Datagram Protocol
# UDP doesn't use handshakes, which has two serious consequences:
#   it is faster than TCP (due to fewer overheads)
#   it is less reliable than TCP
# UDP is more adequate for applications where response time is crucial (DNS, DHCP, Voice,)



### Connection-oriented vs Connectionless communication

## ==> Connection-oriented
# A form of communication which demands some preliminary steps to establish the connection and other steps to finish it
# Both sides of the communication are aware that the other party is connected
# ex: phone call
#   the roles are strictly defined: there is a caller (=client) and there is a callee(=server)
#   the caller must dial the callee's number and wait till the network routes the connection
#   the caller must wait for the callee to answer the call (the callee may reject the connection, or just not answer the call)
#       the actual communication won't start until all the previous steps are completed successfully
#   the communication ends when either of the parties hangs-up
#   Connection-oriented communications are usually built on top of TCP

## ==> Connectionless
# A communication which can be established ad-hoc (snap - just like that) is connectionless communication
# Both parties usually have equal rights, but neither of the parties is aware of the other side's state
# ex: Using walkie-talkies 
#   either of the parties of communication may initiate the communication at any time
#   talking to the mic doesn't guarantee that anybody will hear
#   Connectionless communications are usually built on top of UDP