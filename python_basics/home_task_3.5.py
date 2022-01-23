# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
#
#         Например:
#
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?

# вопрос: где оставлять списки? внутри функции или снаружи?
import random


def get_jokes(joke_count=1.0, rep_words=None):
    """Return list with random generated jokes from local sequences INSIDE function.

    Keyword arguments:
    joke_count -- count jokes at tutors_gen list (default 1.0)
    rep_words -- optional, unique words (default None)

    Limits:
    unique jokes are limited by the length of local sequences

    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    result = []
    if rep_words == 'yes' or rep_words == 'y':
        for i in range():
            noun = random.choice(nouns)
            adv = random.choice(adverbs)
            adj = random.choice(adjectives)
            nouns.remove(noun)
            adverbs.remove(adv)
            adjectives.remove(adj)
            result.append(f'{noun} {adv} {adj}')
        print('You have only 5 unique joke!')
    else:
        for joke in range(int(joke_count)):
            result.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
    return result


print(get_jokes(int(input('How many jokes do you want? ')), input('Do you want unique words in jokes? yes/no: ')))
