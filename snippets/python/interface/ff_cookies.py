from shutil import copyfile
from pathlib import Path
import sqlite3

domain = '...'

profile = next(Path('~/.mozilla/firefox').expanduser().glob('*.default*'))
copyfile(profile / 'cookies.sqlite', '/tmp/db.sqlite')
with sqlite3.connect('/tmp/db.sqlite') as c:
    items = c.execute('select * from moz_cookies where host like ?', [f'%{domain}']).fetchall()
cookies = {i[2]: i[3] for i in items}

