import sqlite3

connection = sqlite3.connect('...')
c = connection.cursor()
c.execute("select * from ...")
records = c.fetchall()
c.close()
