# 17. Стек
def are_symbols_balanced(text):
    stack = []
    open_brackets = "({["
    close_brackets = ")}]"

    for char in text:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if not stack or open_brackets.index(stack.pop()) != close_brackets.index(char):
                return False

    return not stack

print(are_symbols_balanced('(>'))  # False
print(are_symbols_balanced('()'))  # True
print(are_symbols_balanced('[()]'))  # True
print(are_symbols_balanced('({}[])'))  # True
print(are_symbols_balanced('{<>}}')) # False
print(are_symbols_balanced('([)]')) # False
print(are_symbols_balanced('(<><<{[()]}>>)'))