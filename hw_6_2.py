ip_dict = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as log_file:
    for line in log_file:
        ip_num = line.strip().split()[0]
        if ip_num not in ip_dict:
            ip_dict[ip_num] = 1
        else:
            ip_dict[ip_num] += 1
spam_count = max(ip_dict.values())
inv_ip_dict = {value: key for key, value in ip_dict.items()}
print(f'Spam IP {inv_ip_dict[spam_count]}, GET count: {spam_count}')
