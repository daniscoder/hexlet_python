# 15. Вложенные циклы
def unique(collection):
    seen = set()
    unique_items = []
    for item in collection:
        if item not in seen:
            seen.add(item)
            unique_items.append(item)
    return unique_items

def get_same_count(arr1, arr2):
    result = 0
    unique_arr2 = unique(arr2)
    for elem in unique(arr1):
        if elem in unique_arr2:
            result += 1
    return result

# Общие уникальные элементы: 1, 3, 2
print(get_same_count([1, 3, 2, 2], [3, 1, 1, 2, 5])) # 3

# Общие уникальные элементы: 4
print(get_same_count([1, 4, 4], [4, 8, 4])) # 1

# Общие уникальные элементы: 1, 10
print(get_same_count([1, 10, 3], [10, 100, 35, 1])) # 2

# Нет элементов
print(get_same_count([], [])) # 0