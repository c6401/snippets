from django.db import connection

with connection.cursor() as cursor:
    cursor.execute('... %s', [...])
    cursor.fetchall()
