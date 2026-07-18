from typing import Callable


def cache(func: Callable) -> Callable:
    cache = {}

    def wrapper(*args, **kwargs) -> Callable:
        if args in cache.keys():
            print("Getting from cache")
        else:
            cache[args] = func(*args)
            print("Calculating new result")
        return cache[args]
    return wrapper
