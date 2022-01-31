import os

with open('config.yaml', 'r', encoding='utf-8') as f:
    level = 0
    for line in f:
        new_level = len(line.split('|--')[0]) // 3
        el_name = line.strip().split('|--').pop()  # вырезаем имя файла или папки
        if level - new_level == 0:
            if '.' in line:
                try:
                    with open(el_name, 'x', encoding='utf-8'):
                        pass
                except FileExistsError:  # ловим ошибку, если файл уже создан
                    pass
            else:
                try:
                    os.mkdir(el_name)
                except FileExistsError:  # ловим ошибку, если папка уже создана
                    pass
                os.chdir(el_name)
                level += 1
        elif level - new_level > 0:
            for i in range(level - new_level):  # поднимаемся на уровень выше в структуре
                os.chdir('../')
                level -= 1
            if '.' in line:
                try:
                    with open(el_name, 'x', encoding='utf-8'):
                        pass
                except FileExistsError:
                    pass
            else:
                try:
                    os.mkdir(el_name)
                except FileExistsError:
                    pass
                os.chdir(el_name)
                level += 1
