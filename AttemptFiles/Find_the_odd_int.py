def find_it(seq):
    seq.sort()
    if len(seq) > 1:
        s = 0
        l = []
        for i in range(0, len(seq)):
            if i > 0:
                if seq[i] != seq[i - 1]:
                    l.append(seq[i])
            else:
                l.append(seq[i])
        m = 999
        for i in l:
            if seq.count(i) % 2 != 0:
                if m > seq.count(i):
                    m = seq.count(i)
                    s = i
        return s
    else:
        return seq[0]

#Test:
print(find_it([0,1,0,1,0]))