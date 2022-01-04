def count_smileys(arr):
    c = 0
    for i in arr:
        if i[0] == ":" or i[0] == ";":
            if len(i) == 3:
                if i[1] == "-" or i[1] == "~":
                    if i[-1] == "D" or i[-1] == ")":
                        c += 1
            else:
                if i[-1] == "D" or i[-1] == ")":
                    c += 1
    return c

#Test
print(count_smileys([':)', ';(', ';}', ':-D']))