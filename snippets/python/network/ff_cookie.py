import sqlite3
from pathlib import Path
from shutil import copyfile

domain = ...
profiles = Path('~/.mozilla/firefox').expanduser().glob('*.default*')
profile = sorted(profiles, key=lambda p: not str(p).endswith('-release'))[0]
copyfile(profile / 'cookies.sqlite', '/tmp/db.sqlite')
# id originAttributes name value host path expiry lastAccessed creationTime isSecure isHttpOnly inBrowserElement sameSite rawSameSite schemeMap
with sqlite3.connect('/tmp/db.sqlite') as c:
    result = c.execute('select * from moz_cookies where host like ?', [f'%{domain}']).fetchall()
cookies = {c[2]: c[3] for c in result}
