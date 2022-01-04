def get_count(sentence):
    vList = ["a","e","i","o","u"]
    x = 0
    for i in vList:
        x += sentence.count(i)
    return x

#Test:
print(get_count("Hi there"))