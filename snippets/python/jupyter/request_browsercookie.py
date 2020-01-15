import requests
import browsercookie
from IPython.display import HTML

_COOKIES = browsercookie.firefox()

response = requests.get('https://', cookies=_COOKIES)

display(response.text)
