import sqlite3

with sqlite3.connect('...') as connection:
    cursor = connection.execute('select * from ...')
    records = cursor.fetchall()
#cursor.description
