from sys import argv

with open('bakery.csv', 'r', encoding='utf-8') as f:
    if len(argv) == 1:
        for line in f:
            print(line.strip())
    elif len(argv) == 2:
        f.seek(15 * (int(argv[1]) - 1))
        for line in f:
            print(line.strip())
    elif len(argv) == 3:
        f.seek(15 * (int(argv[1]) - 1))
        for i in range((int(argv[2]) + 1) - (int(argv[1]))):
            line = f.readline()
            if not line:
                print('end of values')
                exit(1)
            else:
                print(line.strip())
    else:
        print('Need only 2 arguments:\n- start\n- end')
