fs = [
    lambda x: x + 1,
    lambda x: x + x,
    lambda x: x * x,
]

n = 0

for f in fs:
    n = f(n)

print(n)
