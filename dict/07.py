# 7. Операции над множествами
def diff_keys(old_dict, new_dict):
    old_keys = set(old_dict.keys())
    new_keys = set(new_dict.keys())

    result = {
        'kept': old_keys & new_keys,
        'added': new_keys - old_keys,
        'removed': old_keys - new_keys,
    }

    return result

print(diff_keys({'name': 'Bob', 'age': 42}, {}))
# {'kept': set(), 'added': set(), 'removed': {'name', 'age'}}
print(diff_keys({}, {'name': 'Bob', 'age': 42}))
# {'kept': set(), 'added': {'name', 'age'}, 'removed': set()}
print(diff_keys({'a': 2}, {'a': 1}))
# {'kept': {'a'}, 'added': set(), 'removed': set()}