# 6. Циклы с индексами
def add_prefix(arr, prefix=''):
    return [f'{prefix} {elem}' for elem in arr]

names = ['john', 'smith', 'karl']

new_names = add_prefix(names, 'Mr')
print(new_names)
# => ['Mr john', 'Mr smith', 'Mr karl']

print(names) # Старый массив не меняется!
# => ['john', 'smith', 'karl']