from pathlib import Path

append_text = '''
'''

with Path('~/???').expanduser().open('a') as f:
    f.write(append_text)
    # f.flush()
