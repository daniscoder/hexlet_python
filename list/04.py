# 4. Проверка существования значения
def get(arr, index, default=None):
    if (index >= 0 and index >= len(arr)) or (index < 0 and -index > len(arr)):
        return default
    return arr[index]

cities = ['moscow', 'london', 'berlin', 'porto', '', True]
print(get(cities, 1)) # 'london'
print(get(cities, 4)) # ''
print(get(cities, 10, 'paris')) # 'paris'
print(get(cities, 5, 'oops')) # True
print(get(cities, -1, 'oops')) # True
print(get(cities, 7)) # None