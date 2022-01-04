def sum_two_smallest_numbers(numbers):
    s1 = min(numbers)
    numbers.remove(s1)
    s2 = min(numbers)
    return s1 + s2

#Test:
print(sum_two_smallest_numbers([1,2,4,3,2,0,2]))