def binary_array_to_number(arr):
    s = 0
    c = 1
    for i in arr:
        s += (i) * (2 ** (len(arr) - c))
        c += 1
    return s

print(binary_array_to_number([0, 0, 0, 1]))