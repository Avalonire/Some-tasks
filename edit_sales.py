from sys import argv

with open('bakery.csv', 'r+', encoding='utf-8') as f:
    if len(argv) == 3:
        program, *args = argv
        f.seek(15 * (int(argv[1]) - 1))
        if not f.readline():
            print("Value doesn't exist")
        else:
            f.write(f'{argv[2]:<13}\n')
    else:
        print('Need 2 arguments:\n- value number \n- update value')
