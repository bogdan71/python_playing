xs = [3, 1, 4, 2, -1]


def q(xs):
    if len(xs) <= 1:
        return xs

    pivot_idx = int((len(xs)-1) / 2)
    pivot = xs[pivot_idx]
    ys = list(filter(lambda x: x > pivot, xs))
    zs = list(filter(lambda x: x < pivot, xs))

    return q(ys) + [pivot] + q(zs)

print(q(xs)[0])

Solution
4

Explanation
The function q(xs) in the puzzle implements the quicksort algorithm. For more details on the algorithm google quickly.
q(xs) returns the list sorted in descending order, so the biggest number comes first. Therefore q(xs)[0] returns 4.