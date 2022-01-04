import string
def is_pangram(s):
    l_s = s.lower()
    for i in string.ascii_lowercase:
        if l_s.count(i) < 1:
            return False
    else:
        return True

#Test
print(is_pangram("abcdefghijklmnopqrstuvwxyz"))