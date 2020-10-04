import shelve
from functools import wraps

def shelve_cache(
    path=f'/tmp/{__file__}.shelve',
    keyfunc=lambda func, *args, **kwargs: str((func.__name__, args, kwargs))
):
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
