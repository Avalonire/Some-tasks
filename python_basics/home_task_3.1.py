def num_translate_adv(i_name):
    if i_name[0].isupper() == True:
        i_name = i_name.lower()
        print(numbers.get(i_name).capitalize())
    else:
        print(numbers.get(i_name))

numbers = {'zero': 'ноль',
           'one': 'один',
           'two': 'два',
           'three': 'три',
           'four': 'четыре',
           'five': 'пять',
           'six': 'шесть',
           'seven': 'семь',
           'eight': 'восемь',
           'nine': 'девять',
           'ten': 'десять'
           }
num_translate_adv(input('Write your number: '))
