from functools import wraps
from typing import Awaitable, Callable, Concatenate, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def decorator(
    func: Callable[Concatenate["MyClass", P], Awaitable[R]],
) -> Callable[P, Awaitable[R]]:
    @wraps(func)
    async def wrapper(self: "MyClass", *args: P.args, **kwargs: P.kwargs) -> R:
        return await func(self, *args, **kwargs)

    return wrapper
