xs = [1,5,3,7,2,8,4,6]
y = 0

for x in xs:
    #print('x - ' + str(x))
    if x < y:
        y = x
    #print('y - ' + str(y))

print(min(xs) == y)