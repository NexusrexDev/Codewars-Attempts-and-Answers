def expanded_form(num):
    str_n = str(num)
    s = []
    for i in range(len(str_n)):
        if int(str_n[i]) != 0:
            s.append(str(int(str_n[i]) * (10 ** (len(str_n) - (i+1)))))
    return ' + '.join(s)

#Test:
print(expanded_form(42))