# 7. Ссылки
def reverse(arr):
    arr_copy = arr.copy()
    for i in range(len(arr)):
        arr[i] = arr_copy[-(i + 1)]

names = ['john', 'smith', 'karl']

reverse(names)
print(names)  # => ['karl', 'smith', 'john']

reverse(names)
print(names)  # => ['john', 'smith', 'karl']