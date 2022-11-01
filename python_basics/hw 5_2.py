def odd_nums(arg):
    return (num for num in range(1, arg + 1, 2))


odd_nums_15 = odd_nums(15)
print(next(odd_nums_15))
print(next(odd_nums_15))
print(next(odd_nums_15))
print(next(odd_nums_15))
