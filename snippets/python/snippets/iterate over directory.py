from pathlib import Path

paths = Path('.').glob('**/*.txt')
for path in paths:
     print(path)
