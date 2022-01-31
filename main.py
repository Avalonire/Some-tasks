with open('config.yaml', 'r', encoding='utf-8') as f:
    for line in f:
        print(len(line.split('|--')[0]))
        print(line.strip().split('|--').pop())