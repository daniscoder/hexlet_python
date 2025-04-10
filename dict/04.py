# 4. Инициализация новых значений и defaultdicts
from collections import defaultdict


def collect_indexes(iterable):
    result = defaultdict(list)
    for i, item in enumerate(iterable):
        result[item].append(i)
    return result

d = collect_indexes("hello")
print(d["h"])  # [0]
print(d["e"])  # [1]
print(d["l"])  # [2, 3]