matrix = [
    (0, 1, 1),
    (2, 1, -1),
    (-1, 0, 3),
]

d = [row[col] for col, row in enumerate(matrix)]

print(d)