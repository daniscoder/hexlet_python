# 11. Вложенные списки
def get_super_series_winner(scores):
    result = 0
    for canada, ussr in scores:
        if canada > ussr:
            result += 1
        elif canada < ussr:
            result += -1
    if result > 0:
        return 'canada'
    elif result < 0:
        return 'ussr'
    return None

scores = [
    [3, 7],  # Первая игра
    [4, 1],  # Вторая игра
    [4, 4],
    [3, 5],
    [4, 5],
    [3, 2],
    [4, 3],
    [6, 5],
]

print(get_super_series_winner(scores))  # 'canada'