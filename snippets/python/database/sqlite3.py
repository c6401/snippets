import sqlite3

connection = sqlite3.connect('...')
c = connection.cursor()
c.execute("select * from ...")
cookies = c.fetchall()
c.close()
