tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Андрей', 'Карл', 'Вадим']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def seq_len_equal(long, short):
    short.extend([None for i in range(len(long) - len(short))])
    return range(len(long))


tutors_gen = ((tutors[i], klasses[i]) for i in seq_len_equal(tutors, klasses))

print(type(tutors_gen))
for ind in range(len(tutors)):
    print(next(tutors_gen))
print(dict(tutors_gen))
