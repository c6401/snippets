import contextlib
import io
import sys


@contextlib.contextmanager
def capture_stdout():
    swap = sys.stdout
    stdout = io.StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = swap

with capture_stdout() as output:
    ...

output.getvalue()
output.close()

