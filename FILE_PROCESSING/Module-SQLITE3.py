########## SQLITE3 MODULE ##########


# The sqlite3 module is a built-in Python library that allows you to work with SQLite databases
# It provides an interface compliant with the DB-API 2.0 specification described by PEP 249
# The purpose of the DB-API 2.0 specification is to define a common standard for creating modules to work with databases in Python
# sqlite3 module has been available in Python since version 2.5

# Following SQL standards have been created: SQL-86, SQL-89, SQL-92, SQL:1999, SQL:2003, SQL:2006, SQL:2008, SQL:2011, SQL:2016, SQL:2019
# Detailed information on each of the standards can be found in the Internet resources
# SQLite generally implements the SQL-92 standard, with some exceptions
# ==> https://www.sqlite.org/lang.html


## importing the sqlite3 module  

import sqlite3


## creating a connection to a database

import sqlite3

conn = sqlite3.connect('hello.db') # creates or opens a database file named 'hello.db' in the current directory
conn = sqlite3.connect('C:\PythonLearning\FILE_PROCESSING\\navet.db')


## creating a database in RAM

import sqlite3

conn = sqlite3.connect(':memory:') # creates a database in RAM


## inserting data into a table ==> INSERT INTO

'''
INSERT INTO table_name (column1, column2, column3, ..., columnN)
VALUES (value1, value2, value3, ..., value4);
'''

# INSERT INTO tasks (id, name, priority) VALUES (1, 'My first task', 1);
# if we omit the id column, it will be automatically incremented if it is defined as INTEGER PRIMARY KEY


# simple add

import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()

# executes the CREATE TABLE statement in our database
c.execute('''CREATE TABLE IF NOT EXISTS tasks ( 
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
);''')
c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', ('My first task', 1))
conn.commit() # mandatory to save the changes
conn.close() # close the connection


# multiple add ==> executemany()

import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
);''')
tasks = [
    ('My first task', 1),
    ('My second task', 5),
    ('My third task', 10),
]
c.executemany('INSERT INTO tasks (name, priority) VALUES (?,?)', tasks)
conn.commit()
conn.close()



## application refactoring  

# consists of creating a function containing repetitive fragments. As a result, the code’s volume is reduced, and it becomes more readable

import sqlite3

class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db') # connect to the database
        self.c = self.conn.cursor() # create a cursor object
        self.create_task_table() # create the table when initializing the class
        
    def create_task_table(self): # method to create the tasks table
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     priority INTEGER NOT NULL
                     );''')
    
    def add_task(self): # method to add a new task
        name = input('Enter task name: ')
        priority = int(input('Enter priority: '))
        
        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
        self.conn.commit()

app = Todo()
app.add_task() # call the add_task method to add a new task



## reading data

# iterator
import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()
for row in c.execute('SELECT * FROM tasks'):
    print(row)
conn.close()
'''
(1, 'My first task', 1)
(2, 'My second task', 5)
(3, 'My third task', 10)
(4, 'python chap 1', 1)
(5, 'kubernetes 4', 2)
(6, 'faire travailler les gosses', 3)
'''

# fetchall()
import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('SELECT * FROM tasks')
rows = c.fetchall()
for row in rows:
    print(row)
conn.close()
'''
(1, 'My first task', 1)
(2, 'My second task', 5)
(3, 'My third task', 10)
(4, 'python chap 1', 1)
(5, 'kubernetes 4', 2)
(6, 'faire travailler les gosses', 3)
'''

# fetchone()
import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('SELECT * FROM tasks')
row = c.fetchone()
print(row)
# (1, 'My first task', 1)
row = c.fetchone()
print(row)
# (2, 'My second task', 5)
conn.close()