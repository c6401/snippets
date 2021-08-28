import requests
import browsercookie

cookies = browsercookie.firefox()

response = requests.get('https://', cookies=cookies)

response.text
