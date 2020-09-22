def RabinKarp(string, pattern):
    n, m = len(string), len(pattern)
    hpattern = hash(pattern);
    for i in range(n-m+1):
        hs = hash(string[i:i+m])
        if hs == hpattern:
            if string[i:i+m] == pattern:
                return i
    return -1

s1 = "Ronaldo is better than Messi"        

print(RabinKarp(s1, "Football"))