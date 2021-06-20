import requests
import browsercookie
from IPython.display import HTML

cookies = browsercookie.firefox(cookie_file=[''])

response = requests.get('https://', cookies=cookies)

display(response.text)
