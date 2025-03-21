# 7. Срезы
def rotated_left(items):
    return items[1:] + items[:1]

def rotated_right(items):
    return items[-1:] + items[:-1]


print(rotated_left("ABCD"))
print(rotated_right([1, 2, 3, 4]))