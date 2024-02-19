# 2. Концепция списков
# def is_list(value):
#     return isinstance(value, list)


# 3. Создание списков и добавление элементов
# import math
#
#
# def get_square_roots(value):
#     if value < 0:
#         return []
#     if value == 0:
#         return [0]
#     square_root = math.sqrt(value)
#     return [-square_root, square_root]


# 4. Ссылки
# def get_range(n):
#     return list(range(n))


# 5. Ссылки и изменяемость
# def duplicate(items):
#     items.extend(items)


# 6. Модификация списков поэлементно
# def rotate(items):
#     if items:
#         items.insert(0, items.pop(-1))
#
#
# items = [1, 2, 3]
# rotate(items)
# print(items)  # => [3, 1, 2]


# 7. Срезы
# def rotated_left(items):
#     return items[1:] + items[:1]
#
#
# def rotated_right(items):
#     return items[-1:] + items[:-1]
#
#
# print(rotated_left("ABCD"))
# print(rotated_right([1, 2, 3, 4]))


# 8. Цикл for
def find_index(value, items):
    for i, item in enumerate(items):
        if value == item:
            return i
#
#
# find_index('t', 'cat')  # 2
# find_index(5, [1, 2, 3, 4, 5, 6, 7])  # 4
# find_index(42, [])  # True
# find_index('!', 'abc')  # True


# 9. Итераторы
# def find_second_index(value, items):
#     it = iter(items)
#     first_index = find_index(value, it)
#     second_index = find_index(value, it)
#     if second_index is not None:
#         return first_index + second_index + 1
#
#
# print(find_second_index('b', 'bob'))
# print(find_second_index('n', 'cannon'))
