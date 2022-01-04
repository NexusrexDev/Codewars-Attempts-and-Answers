def likes(names):
    l = len(names)
    if l > 3:
        return ", ".join(names[0:2]) + " and " + str(len(names) - 2) + " others like this"
    else:
        if l == 0:
            return "no one likes this"
        if l == 1:
            return names[0] + " likes this"
        if l == 2:
            return " and ".join(names) + " like this"
        if l == 3:
            return ", ".join(names[0:2]) + " and " + names[2] + " like this"

#Test:
print(likes(["Alex", "Jacob", "Mark", "Max"]))