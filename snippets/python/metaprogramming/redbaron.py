from redbaron import RedBaron

with open('____', 'r') as f: red = RedBaron(f.read())

with open('____', 'w') as f: f.write(red.dumps())
