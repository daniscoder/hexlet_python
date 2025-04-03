# 16. Сортировка списков
def bubble_sort(arr):
    last = len(arr) - 1
    while last > 0:
        change = False
        for i in range(last):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                last = i
                change = True
        if not change:
            break
    return arr

print(bubble_sort([])) # []
print(bubble_sort([3, 10, 4, 3])) # [3, 3, 4, 10]