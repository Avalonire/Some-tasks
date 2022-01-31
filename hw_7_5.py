import os
import sys
import json

script_dir = os.path.join(os.path.dirname(__file__), str(sys.argv[1]))
root_dir = os.path.dirname(__file__)

result_dict = {10: [0, []]}
for root, dirs, files in os.walk(script_dir):
    for _file in files:
        ext = os.path.splitext(_file)[1]
        size = os.stat(os.path.join(root, _file)).st_size
        degree = 10 ** len(str(size))
        if result_dict.get(degree):
            if ext not in result_dict[degree][1]:
                result_dict[degree][1].append(ext)
                result_dict[degree][0] += 1
            else:
                result_dict[degree][0] += 1
        else:
            result_dict[degree] = [1, [ext]]

result_dict = {key: tuple(result_dict[key]) for key in sorted(result_dict)}
try:
    with open(f'{str(sys.argv[1])}_summary.json', 'x', encoding='utf-8') as f:
        json.dump(result_dict, f)
except FileExistsError:
    print('Summary file already exists!')
    exit(1)
