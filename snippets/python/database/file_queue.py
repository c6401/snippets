from contextlib import contextmanager
import re


@contextmanager
def file_queue(
    filename: str, config: dict, regex = '', subscriber = '', infinite = False
):
    conf = config.setdefault('file_queue', {})
    subscription = f'{filename}:{subscriber}'
    position = conf.setdefault(subscription, 0)
    with open(filename, 'r') as file:
        file.seek(position)

        def messages():
            result = []
            while True:
                line = file.readline()
                if not infinite and not line:
                    break
                conf[subscription] = file.tell()
                result.append(line)
                if re.match(regex, line):
                    yield ''.join(result)
                    result = []

        yield messages()
