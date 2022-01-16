def thesaurus(*args):
    result = {}
    for name in args:
        result.update({name[0]: list(filter(lambda el: el.startswith(f'{name[0]}'), args))})
    return result


def thesaurus_adv(*args):
    result_adv = {}
    for people in args:
        surname = str.split(people, ' ')[1][0]
        result_adv.update({surname: list(filter(lambda el: el[el.index(' ') + 1:].startswith(f'{surname}'), args))})
    # print(result_adv)

    for item in result_adv:
        result_adv[item] = thesaurus(*result_adv[item])
    return result_adv


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
