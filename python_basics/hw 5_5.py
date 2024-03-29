# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# result = [23, 1, 3, 10, 4, 11]
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.

unique_num = []
repeat_num = set()
for num in src:
    if num in repeat_num:
        continue
    if num in unique_num:
        unique_num.remove(num)
        repeat_num.add(num)
        continue
    unique_num.append(num)

print(unique_num)