with open('nginx_logs.txt', 'r+', encoding='utf-8') as log_file:
    for line in log_file:
        line_1 = log_file.readline().strip()
        print((line_1.split(' ')[0], line_1.split(' ')[5][1:], line_1.split(' ')[6]))
