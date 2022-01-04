def is_valid_walk(walk):
    if len(walk) == 10:
        y = abs(walk.count('n') - walk.count('s'))
        x = abs(walk.count('e') - walk.count('w'))
        if x + y == 0:
            return True
        else:
            return False
    else:
        return False

#Test:
print(is_valid_walk(['n','s','n','s','e','e','w','w','n','s']))