import os

def cmd(command):
    with os.popen(command) as io: return io.read().strip()
