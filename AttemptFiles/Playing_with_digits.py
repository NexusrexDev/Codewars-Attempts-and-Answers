def dig_pow(n, p):
    str_n = str(n)
    length = len(str_n)
    sum = 0
    for i in range(0,length,1):
        sum += int(str_n[i]) ** (p+i)
    k = sum/n
    if k.is_integer():
        return k
    else:
        return -1

#Test:
print(dig_pow(89, 1))