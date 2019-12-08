from pathlib import Path

paths = Path('some dir').glob('**/*.txt')
for path in paths:
     path
