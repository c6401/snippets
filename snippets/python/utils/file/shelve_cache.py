import shelve
from datetime import datetime, timedelta
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
            result, expiration = decorator.shelve.get(key, (..., None))
            if result == ... or datetime.now() >= expiration:
                result = func(*args, **kwargs)
                expiration = datetime.now() + timedelta(days=1) 
                decorator.shelve[key] = result, expiration
            return result
        return wrapper

    decorator.shelve = shelve.open(path)
    return decorator

cache = shelve_cache()
