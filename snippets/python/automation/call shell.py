import subprocess

def cmd(command, input=None):
    return subprocess.run(
        command, input=input, capture_output=True, shell=True, text=True,
    ).stdout.strip()
