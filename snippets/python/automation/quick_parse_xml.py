import xmltodict, requests
from ruamel import yaml
url = ''
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/86.0'})
data = xmltodict.parse(response.text)
yaml.dump(data, default_flow_style=False, version=(1,2))
