import re

fruits = [
    "apple",
    "banana",
    "orange",
    "bananas"
]

result = [x for x in fruits if re.fullmatch("b.+a", x)]

print(result[0])