import subprocess


def sh(command, capture=True, **kwargs):
    if capture: kwargs.update(stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process = subprocess.Popen(command, shell=True, **kwargs)
    (stdout, stderr) = process.communicate()
    if process.returncode: exit((stderr or b'').decode('utf-8'))
    return (stdout or b'').decode('utf-8').strip()
