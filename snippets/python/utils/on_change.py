import os
from time import sleep

def on_change(filename, interval=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            stamp = None
            while True:
                new_stamp = os.stat(filename).st_mtime
                if stamp != new_stamp:
                    stamp = new_stamp
                    func(*args, **kwargs)
                sleep(interval)
        return wrapper
    return decorator
