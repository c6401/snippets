import csv

with open('file.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
