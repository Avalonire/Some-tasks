# Получите новый список, элементами которого будут только уникальные элементы исходного.

    # Примечание. Списки создайте вручную, например так:

my_list = [2, 2, 5, 12, 8, 2, 12]
result = []
for number in my_list:
    if my_list.count(number) == 1:
        result.append(number)

print(result)
