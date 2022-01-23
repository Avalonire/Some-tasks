def odd_nums(arg):
    odd_gen = (num for num in range(1, arg + 1, 2))
    for i in range(1, arg + 1, 2):
        print(next(odd_gen))


print(odd_nums(15))
