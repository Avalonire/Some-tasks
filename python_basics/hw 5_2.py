def odd_nums(arg):
    return (num for num in range(1, arg + 1, 2))


print(next(odd_nums(15)))
