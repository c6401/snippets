import pandas as pd

table = pd.read_html(___)[0]

for record in table.to_records():
    ___ = record[0]
