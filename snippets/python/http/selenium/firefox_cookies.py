import sqlite3
from pathlib import Path
from shutil import copyfile

import geckodriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

geckodriver_autoinstaller.install()


domain = 'example.com'
profiles = Path('~/.mozilla/firefox').expanduser().glob('*.default*')
profile = sorted(profiles, key=lambda p: not str(p).endswith('-release'))[0]
copyfile(profile / 'cookies.sqlite', '/tmp/ff.sqlite')

with sqlite3.connect('/tmp/ff.sqlite') as c:
    cookies = c.execute('select * from moz_cookies where host like ?', [f'%{url}']).fetchall()


options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

driver.get(f'https://{domain}')

for cookie in cookies:
    driver.add_cookie({
        'domain': domain, 'name': cookie[2], 'value': cookie[3],
        'path': cookie[5], 'secure': bool(cookie[9]), 'expiry': cookie[6],
    })

driver.get(f'https://{domain}')
