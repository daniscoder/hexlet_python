# 9. Удаление элементов списка
def get_same_parity(arr):
    if not arr:
        return []
    charges = arr[0] % 2
    return [elem for elem in arr if elem % 2 == charges]

print(get_same_parity([]))     # []
print(get_same_parity([1, 2, 3])) # [1, 3]
print(get_same_parity([1, 2, 8])) # [1]
print(get_same_parity([2, 2, 8])) # [2, 2, 8]