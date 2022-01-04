def count_deaf_rats(town):
    if town.count("P") != 0:
        # Town splitting
        l = []
        i = 0
        while i < len(town):
            if town[i] != "P" and town[i] != " ":
                l.append(town[i:i + 2])
                i += 2
            elif town[i] == "P":
                l.append(town[i])
                i += 1
            elif town[i] == " ":
                i += 1
        # Checking
        r_pos = l.index("P")
        d_c = 0
        i = 0
        for i in range(0, len(l)):
            if l[i] != "P":
                if i > r_pos and l[i] == "~O":
                    d_c += 1
                elif i < r_pos and l[i] == "O~":
                    d_c += 1
        return d_c
    else:
        return 0

###Superb Kata! As newbie I brute-forced my way in, totes fun and gamedev like <3

#Test:
print(count_deaf_rats("~OO~ ~O P"))