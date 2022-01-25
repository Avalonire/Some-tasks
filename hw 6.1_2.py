from sys import getsizeof

with open('nginx_logs.txt', 'r+', encoding='utf-8') as log_file:
    ip_set = list()
    for line in log_file:
        line_1 = log_file.readline().strip()
        ip_set.append(line_1.split(' ')[0])
    for i in range(len(ip_set)):
        if ip_set.count(i) >
    print(ip_set)
    print(getsizeof(ip_set))
