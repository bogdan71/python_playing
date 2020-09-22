def len_(x):
    length = len(x)
    # print everything in same row
    print(length, end='')
    return length

items = [3.14, 'mooon', {}]
i = 0

while i < len_(items):
    i += 1