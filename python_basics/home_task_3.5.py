import random


def get_jokes(joke_count=1.0, rep_words=None):
    """Return list with random generated jokes from local sequences INSIDE function.

    Keyword arguments:
    joke_count -- count jokes at result list (default 1.0)
    rep_words -- optional, unique words (default None)

    Limits:
    unique jokes are limited by the length of local sequences;
    local sequences must be equal length;

    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    result = []
    if rep_words == 'yes' or rep_words == 'y':
        limit_len = len(nouns)
        for i in range(len(nouns)):
            noun = random.choice(nouns)
            adv = random.choice(adverbs)
            adj = random.choice(adjectives)
            nouns.remove(noun)
            adverbs.remove(adv)
            adjectives.remove(adj)
            result.append(f'{noun} {adv} {adj}')
        print(f'You have only {limit_len} unique joke!')
    else:
        for joke in range(int(joke_count)):
            result.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
    return result


print(get_jokes(int(input('How many jokes do you want? ')), input('Do you want unique words in jokes? yes/no: ')))
