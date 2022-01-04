def array_diff(a,b):
    for i in b:
        x = a.count(i)
        for j in range(x):
            a.remove(i)
    return a

#Test:
print(array_diff([1,2],[1]))