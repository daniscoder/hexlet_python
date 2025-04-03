# 3. Модификация
def swap(arr):
    if len(arr) > 1:
        elem = arr[0]
        arr[0] = arr[-1]
        arr[-1] = elem
    return arr

print(swap([])) # []
print(swap([1])) # [1]
print(swap([1, 2])) # [2, 1]
print(swap(['one', 'two', 'three'])) # ['three', 'two', 'one']