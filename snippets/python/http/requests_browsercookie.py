import requests
import browsercookie

_COOKIES = browsercookie.firefox()

requests.get('https://', cookies=_COOKIES)
