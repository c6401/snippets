from pyquery import PyQuery as PQ

pq = PQ('https://...')
for i in pq.find('script'):
    i.text = ''

pq.text()
