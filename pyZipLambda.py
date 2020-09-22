# euclidean distance between points a, b
d = lambda a, b: (sum((ai - bi) ** 2 for ai, bi in zip(a, b))) ** 0.5
john = (0, 1)
alice = (3, 1)

print(int(d(john, alice)))