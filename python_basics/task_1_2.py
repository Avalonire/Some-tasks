# 2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача — вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

# date = input('введите дату в формате dd.mm.yyyy: ')
date = '02.11.2013'
date = date.split('.')

# print(date)
# result = []
# item = result[0]
# if int(item) == 1:
#     result.append('первое')
# elif int(item) == 2:
#     result.append('второе')
# elif int(item) == 3:
#     result.append('третье')
# elif int(item) == 4:
#     result.append('четвертое')
#     if int(month) == 1:
#         result.append('января')
#     elif int(month) == 2:
#         result.append('февраля')
# result.append(date[2])
#
# print(str(result), 'года')