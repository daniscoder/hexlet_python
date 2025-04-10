# 5. Множества
def all_unique(iterable):
    return len(set(iterable)) == len(iterable)

print(all_unique([]))
# True
print(all_unique([1, 2, 3]))
# True
print(all_unique([1, 2, 1]))
# False