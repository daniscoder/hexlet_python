# 6. Изменение множеств
def toggle(key, flags: set):
    if key in flags:
        flags.remove(key)
    else:
        flags.add(key)

def toggled(key, flags: set):
    res = flags.copy()
    toggle(key, res)
    return res

READ_ONLY = 'read_only'
flags = set()
toggle(READ_ONLY, flags)
print(READ_ONLY in flags)  # True
toggle(READ_ONLY, flags)
print(READ_ONLY in flags)  # False

flags = set()
new_flags = toggled(READ_ONLY, flags)
print(READ_ONLY in flags)  # False
print(READ_ONLY in new_flags)  # True