def bubblesort(lst):
    for passesLeft in range(len(lst)-1, 0, -1):
        for index in range(passesLeft):
            if lst[index] > lst[index + 1]:
                lst[index], lst[index + 1] = lst[index + 1], lst[index]
    return lst

l = [66, 89, 62, 9, 53, 59]
print(bubblesort(l))
