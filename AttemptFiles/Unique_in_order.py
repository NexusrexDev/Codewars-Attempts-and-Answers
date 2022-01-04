def unique_in_order(iterable):
    or_l = []
    for i in iterable:
        if len(or_l) > 0:
            if i == or_l[-1]:
                continue
            else:
                or_l.append(i)
        else:
            or_l.append(i)
    return or_l

#Test:
print(unique_in_order('AAAABBBCCDAABBB'))