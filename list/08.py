# 8. Агрегация
def calculate_sum(arr):
    summ = 0
    for elem in arr:
        if elem % 3 == 0:
            summ += elem
    return summ

coll1 = [8, 9, 21, 19, 18, 22, 7]
print(calculate_sum(coll1)) # 48

coll2 = [2, 0, 17, 3, 9, 15, 4]
print(calculate_sum(coll2)) # 27