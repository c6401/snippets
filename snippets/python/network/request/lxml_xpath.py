import requests
from lxml import html

response = requests.get('???')

tree = html.fromstring(response.content)
el = tree.xpath('//*')[0]
