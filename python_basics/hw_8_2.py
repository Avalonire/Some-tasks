raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'

import re

parsed_raw = re.compile(r'((?:\d+\.\d+){3}).*\[(.*)]\s"(\w+)\s([/\w+]*).*(\s\d+)\s(\d+)')
print(parsed_raw.findall(raw))


