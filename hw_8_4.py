from functools import wraps


def val_checker(callback=None):
    def _val_checker(func):
        @wraps(func)
        def wrapper(x):
            if not callback(x):
                raise ValueError(f'WRONG VALUE: "{x}"!')
            return func(x)

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(3))
print(calc_cube(41))
print(calc_cube(-2))
