def ctz(name, age, city):
    return print(f'{name}, {age} год(а), проживает в городе {city}')


ctz('Alex', 30, 'Москва')
print('-' * 100)

numbers = [1, 2, 44, 545, 2, 45]
numbers_2 = [23, 12, 33, 1, 56, 77]

def num(list):
    return max(list)


print(num(numbers))
