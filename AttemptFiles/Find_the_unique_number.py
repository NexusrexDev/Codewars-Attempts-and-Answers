def find_uniq(arr):
    rev = True
    x = 0
    while x < len(arr):
        arr.sort(reverse=rev)
        if arr.count(arr[x]) == 1:
            return arr[x]
        else:
            arr.remove(arr[x])
            rev = not rev

#Test
print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))