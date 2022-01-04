def square_digits(num):
    l = list(str(num))
    x = ""
    for i in range(len(l)):
        l[i] = int(l[i]) ** 2
        x += str(l[i])
    return int(x)

#Test:
print(square_digits(9119))