index = 5
string = 'g'

while index > 3:
    index -= 1
    if index == 3:
        continue
    string += 'o'

else:
    string += 'd'

print(string)
