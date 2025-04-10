# 8. Слияние словарей
from collections import defaultdict


def merged(arr):
    result = defaultdict(set)
    for item in arr:
        for k, v in item.items():
            result[k].add(v)
    return result

print(merged([{}, {}]) == {})
# True
print(merged([
    {'a': 1, 'b': 2},
    {'b': 10, 'c': 100},
]) == {'a': {1}, 'b': {2, 10}, 'c': {100}})
# True