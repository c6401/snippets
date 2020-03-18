import subprocess
import sys


def cmd(command, capture=True, pipe=None, detached=False, cwd=None, **kwargs):
    if capture:
        kwargs.update(stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if not sys.stdin.isatty():
        kwargs.update(stdin=sys.stdin)
    if pipe:
        kwargs.update(stdin=subprocess.PIPE)
        pipe = pipe.encode('utf-8')

    process = subprocess.Popen(command, shell=True, cwd=cwd, **kwargs)
    if detached:
        return process
    (stdout, stderr) = process.communicate(input=pipe)
    if process.returncode:
        exit((stderr or b'').decode('utf-8'))
    return (stdout or b'').decode('utf-8').strip()
