def bsearch(l, value):
    lo, hi = 0, len(l)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if l[mid] < value:
            lo = mid + 1
        elif value < l[mid]:
            hi = mid -1
        else:
            return mid
    return -1

l = []
x = 6
print(bsearch(l, 6))
