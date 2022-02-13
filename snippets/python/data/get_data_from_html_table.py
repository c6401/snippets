from bs4 import BeautifulSoup


soup = BeautifulSoup(response, "html.parser")
table = soup.find_all('table')[0]

rows = [
    [col.text.strip() for col in row.find_all('td')]
    for row in table.find_all('tr')
]
