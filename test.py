def move_zeros(arr):
    return [x for x in arr if x != 0] + [0] * arr.count(0)

#test
print(move_zeros([1, 0, 1, 2, 0, 1, 3]))  # Output: [1, 1, 2, 1, 3, 0, 0]
print(move_zeros([0, 0, 1, 2, 3]))        # Output: [1, 2, 3, 0, 0, 0]
print(move_zeros([0, 0, 0, 1]))           # Output: [1, 0, 0, 0]
print(move_zeros([1, 2, 3]))              # Output: [1, 2, 3]