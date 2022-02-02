from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        print(f'call {func.__name__}({", ".join([(str(arg) + ": " + str(type(arg))) for arg in args])})')
        return result

    return wrapper


@type_logger
def calc_cube(*args):
    return [arg ** 3 for arg in args]


print(calc_cube(2, 4, 6))
