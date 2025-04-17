def cart_prod(*sets):
    result = [()]
    for current_set in sets:
        temp = []
        for partial_tuple in result:
            for element in current_set:
                new_tuple = partial_tuple + (element,)
                temp.append(new_tuple)
        result = temp

    return set(result)

NULLSET = set()
A = {1}
B = {1, 2}
C = {1, 2, 3}
X = {'a'}
Y = {'a', 'b'}
Z = {'a', 'b', 'c'}

print(cart_prod(A, B, C))