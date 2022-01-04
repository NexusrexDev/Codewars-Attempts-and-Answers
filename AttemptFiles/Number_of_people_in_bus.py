def number(bus_stops):
    ppl_in_bus = 0
    for i in bus_stops:
        ppl_in_bus += i[0]
        ppl_in_bus -= i[1]
    return ppl_in_bus

#Test:
print(number([[10,0],[3,5],[5,8]]))