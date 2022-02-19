class ListOfNumbers(Exception):
    pass


result = []
print('Занесение чисел в список.\nДля остановки программы введите "stop"')
while True:
    user_input = input('Введите число для занесения в список: ')
    if user_input == 'stop':
        break
    try:
        if not user_input.isdigit():
            raise ListOfNumbers(f'"{user_input}" не является числом! Список не обновлен.')
    except ListOfNumbers as error:
        print(error)
        continue
    result.append(int(user_input))

print(f'Финальный список:\n{result}')
