def srange(x):
    return range(x-3, x)

s = 0
print(srange(2))
for i in srange(2):
    print('i' + str(i))
    s += i
    print('s' + str(s))

print(s)
