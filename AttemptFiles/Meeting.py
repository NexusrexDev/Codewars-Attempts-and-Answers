def meeting(s):
    l = []
    r_s = ""
    u_s = s.upper()
    u_s = u_s.split(";")
    for i in u_s:
        l.append(i.split(":"))
    for j in range(len(l)):
        l[j].reverse()
    l.sort()
    for k in range(len(l)):
        r_s += "("+", ".join(l[k])+")"
    return r_s

#Test:
s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
print(meeting(s))