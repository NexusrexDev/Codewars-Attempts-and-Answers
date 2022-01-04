def data_reverse(data):
    length = int(len(data) / 8)
    t_l = []
    r_d = []
    for i in range(1,length+1):
        t_l.append(data[(i-1)*8:(i)*8])
    t_l.reverse()
    for byte in t_l:
        for bit in byte:
            r_d.append(bit)
    return r_d

#Test:
print(data_reverse([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]))