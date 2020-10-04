from shutil import copyfile
from pathlib import Path
import sqlite3

domain = '...'

profiles = Path('~/.mozilla/firefox').expanduser().glob('*.default*')
profile = sorted(profiles, key=lambda p: not str(p).endswith('-release'))[0]
copyfile(profile / 'cookies.sqlite', '/tmp/db.sqlite')
with sqlite3.connect('/tmp/db.sqlite') as c:
    cookies = c.execute('select * from moz_cookies where host like ?', [f'%{domain}']).fetchall()
COOKIES = {c[2]: c[3] for c in cookies}

