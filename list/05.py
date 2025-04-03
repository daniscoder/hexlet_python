# 5. Цикл for и списки
def calculate_average(arr):
    if not arr:
        return None
    sum_elem = 0
    for elem in arr:
        sum_elem += elem
    return sum_elem / len(arr)

temperatures1 = [37.5, 34, 39.3, 40, 38.7, 41.5]
print(calculate_average(temperatures1)) # 38.5

temperatures2 = [36, 37.4, 39, 41, 36.6]
print(calculate_average(temperatures2)) # 38