import re

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        parsed_raw = re.compile(r'(^.*)\s-\s-\s\[(.*)]\s"(\w+)\s([/\w+]*).*(\s\d+)\s(\d+)')
        print(parsed_raw.findall(line))
