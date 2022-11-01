# 1: Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.

my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

# множества
my_list_1_correct = set(my_list_1) - set(my_list_2)
print(list(my_list_1_correct))

# цикл for
# циклом необходимо проходить по копии списка
for num in my_list_1[:]:
    if num in my_list_2:
        my_list_1.remove(num)
print(my_list_1)

