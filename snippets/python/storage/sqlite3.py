import sqlite3

with sqlite3.connect('...') as connection:
    cursor = connection.execute('select 1;')
    # cursor = connection.execute("SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';")
    # cursor = connection.execute('select ?', [...])
    records = cursor.fetchall()
#cursor.description
