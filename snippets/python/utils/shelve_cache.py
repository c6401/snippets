import shelve
from functools import wraps

def shelve_cache(path=None, keyfunc=None):
    if not path:
        path = '/tmp/' + __file__.rsplit("/", 1)[-1] + '.shelve'
    if not keyfunc:
        keyfunc = lambda f, *a, **kw: str((f.__name__, a, kw))

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = keyfunc(func, args, kwargs)
            result = decorator.shelve.get(key, ...)
            if result == ...:
                result = decorator.shelve[key] = func(*args, **kwargs)
            return result
        return wrapper

    decorator.shelve = shelve.open(path)
    return decorator

cache = shelve_cache()
