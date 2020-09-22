def make_incrementor(n):
    print(n)
    return lambda x: x + n

f = make_incrementor(40)
print(f(0))
print(f(10))
