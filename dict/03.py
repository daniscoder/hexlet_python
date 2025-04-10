# 3. Изменение данных в словаре
def count_all(iterable):
    result = {}
    for item in iterable:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result

print(count_all(["cat", "dog", "cat"]))  # {"cat": 2, "dog": 1}
print(count_all("hello"))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print(count_all("*" * 20))  # {'*': 20}