# 8. Методы объектов множеств
def apply_diff(target, diff):
    if 'add' in diff:
        target |= diff['add']
    if 'remove' in diff:
        target -= diff['remove']

target = {'a', 'b'}
diff = {'add': {'c'}, 'remove': {'a'}}
apply_diff(target, diff)
print(target)  # => {'c', 'b'}