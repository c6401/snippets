import shelve


with shelve.open('shelve') as db:
    db['key'] = 'val'
