from django.db import connection; 'postgresql://{user}:{password}@localhost:5432/{database}'.format(**connection.get_connection_params()) 
