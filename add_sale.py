from sys import argv

with open('bakery.csv', 'a', encoding='utf-8') as f:
    if len(argv) > 1:
        for i in argv[1:]:
            f.write(f'{i:<13}\n')
    else:
        print('Need value')
