s1 = "AAA"
s2 = "BBBBB"

s = list(s2)
for i,c in enumerate(s1):
    s.insert(i*2, c)
print("".join(s))