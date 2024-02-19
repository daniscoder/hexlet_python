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
# def find_index(value, items):
#     for i, item in enumerate(items):
#         if value == item:
#             return i
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


# Испытания


# 12. Копилка
# from collections import Counter
#
#
# def visualize(coins, bar_char='₽'):
#     bar_char = bar_char * 2
#     cnt = Counter(coins)
#     max_coins = max(cnt.values())
#     coins_arr = []
#     visualize_coin = []
#     for coin in sorted(cnt):
#         coins_arr.append([''] * (max_coins - cnt[coin]) + [cnt[coin]] + [bar_char] * cnt[coin])
#         visualize_coin.append('{:<2}'.format(coin))
#     visualize_arr = []
#     coins_count = len(coins_arr)
#     for j in range(max_coins + 1):
#         visualize_line = []
#         for i in range(coins_count):
#             visualize_line.append('{:<2}'.format(coins_arr[i][j]))
#         visualize_arr.append(' '.join(visualize_line))
#     visualize_arr.append('-'.join(['--'] * coins_count))
#     visualize_arr.append(' '.join(visualize_coin))
#     return '\n'.join(visualize_arr)
#
#
# print(visualize((10, 1, 1, 1, 1, 1, 20, 20, 20, 2, 2, 2, 2, 3, 3, 3, 3)))
# MONEY = (
#     1, 20, 2, 5, 20,
#     3, 5, 2, 10, 2,
#     20, 2, 20, 1, 2,
#     1, 1, 2, 10, 20, 3,
# )
# print(visualize(MONEY))


