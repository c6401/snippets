import sqlsoup

db = sqlsoup.SQLSoup('postgresql://...')
db._metadata.reflect()
db._metadata.tables.keys()
