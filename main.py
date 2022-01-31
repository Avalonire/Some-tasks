def getley(size):
    num = 1
    while True:
        if size // 10:
            num += 1
        else:
            break
        size //= 10
    return 10 ** num

print(getley(7568))
print(getley(12))
print(getley(222))
