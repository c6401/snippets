from pathlib import Path

for path in Path('.').walk():
    print(path)
