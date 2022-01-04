import math
def is_square(n):
    if n >= 0:
        if math.sqrt(n).is_integer():
            return True
        else:
            return False
    else:
        return False

#Test:
print(is_square(4))