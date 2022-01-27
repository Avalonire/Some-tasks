from sys import argv

with open(argv[1], 'r+', encoding='utf-8') as f_1:
    with open(argv[2], 'r+', encoding='utf-8') as f_2:
        with open(argv[3], 'w', encoding='utf-8') as f_3:
            for line in f_1:
                hobby = f_2.readline().strip()
                if not hobby:
                    f_3.write(f'{line.strip()}: None\n')
                else:
                    f_3.write(f'{line.strip()}: {hobby}\n')
            if f_2.readline():
                exit(1)
