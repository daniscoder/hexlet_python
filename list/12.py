# 12. Теория множеств
def count_uniq_chars(text):
    return len(set(text))

text1 = 'yyab' # y, a, b
print(count_uniq_chars(text1)) # 3

text2 = 'You know nothing Jon Snow'
print(count_uniq_chars(text2)) # 13

# Если передана пустая строка, то функция должна вернуть `0`
text3 = ''
print(count_uniq_chars(text3)) # 0