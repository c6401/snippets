import atoma
import requests

response = requests.get('???')
feed = atoma.parse_rss_bytes(response.content)
feed.items
