def descending_order(num):
    l = list(str(num))
    l.sort(reverse=True)
    x = 0
    for i in range(len(l)):
        x += int(l[i]) * (10 ** (len(l) - (i+1)))
    return x

#Test:
print(descending_order(42145))