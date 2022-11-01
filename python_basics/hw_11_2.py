class ZeroFatalError(Exception):
    def __init__(self, text):
        self.txt = text


print('Для деления "a" на "b"')
div_a = input('введите "a": ')
div_b = input('введите "b": ')

try:
    if int(div_b) == 0:
        raise ZeroFatalError('Деление на 0 невозможно!')
    result = int(div_a) / int(div_b)
except ZeroFatalError as err:
    print(err)
except ValueError:
    print('Введите числа!')
else:
    print(result)
