def square_sum(numbers):
    s = 0
    for i in numbers:
        s += i ** 2
    return s

#Test:
print(square_sum([1,2,2]))