import requests
import browsercookie

_COOKIES = browsercookie.firefox()

response = requests.get('https://', cookies=_COOKIES)

response.text
