from typing import Callable


def strict(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        for need_type, arg in zip(func.__annotations__.values(), args):
            if type(arg) != need_type:
                raise TypeError('Несоответствие между типом параметра и типом аргумента')
        return func(*args, **kwargs)

    return wrapper
