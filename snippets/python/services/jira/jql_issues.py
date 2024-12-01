import requests
import browsercookie

cookies = browsercookie.firefox()  # chrome ?

API = ''

response = requests.get(f'{API}/rest/api/3/search?jql=...', cookies=cookies)
