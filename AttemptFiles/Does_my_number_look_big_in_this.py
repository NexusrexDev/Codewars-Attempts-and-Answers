def narcissistic( value ):
    s = 0
    l = len(str(value))
    for i in range(0,l):
        s += int(str(value)[i]) ** l
    if s == value:
        return True
    else:
        return False

#Test:
print(narcissistic(153))