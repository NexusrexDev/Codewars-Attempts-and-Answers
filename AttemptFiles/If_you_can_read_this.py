def to_nato(words):
    dictionary = {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf',
                  "H": "Hotel", 'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November',
                  'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform',
                  'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray', 'Y': 'Yankee', 'Z': 'Zulu'}

    words = words.upper()
    l = words.split(" ")
    s = []
    for i in l:
        for j in i:
            if j not in dictionary:
                s.append(j)
            else:
                s.append(dictionary.get(j))
    w = " ".join(s)
    return w

#Test:
print(to_nato("Hi there."))