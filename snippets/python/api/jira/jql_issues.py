import requests
import browsercookie

_COOKIES = browsercookie.firefox()  # chrome ?

API = ''

response = requests.get(f'{API}/rest/api/3/search?jql=...', cookies=_COOKIES)
