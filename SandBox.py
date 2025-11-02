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

