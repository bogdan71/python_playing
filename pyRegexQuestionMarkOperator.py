import re

fruits = [
    "apple",
    "banana",
    "orange",
    "kiwi"
]
lx = lambda x: re.match(".?.?a", x) != None
result = list(map(lx, fruits))

print(sum(result))

Solution
3

Explanation
The lambda expression lx checks if the regex .?.?a matches the string x and returns True or False depending on the result of the match. When there is a match, the function re.match() returns a match object and if we compare it to None we get True or False for match or no match. The regular expression matches if the input string starts with "a" or has an "a" at the second or third position.
With the function map we map this lambda expression to the list of strings where .?.?a matches for "apple", "banana", "orange" and for "kiwi" it doesn't match. Therefore the result is a list of boolean values [True, True, True, False]. Finally we apply the function sum to the result list. Since True maps to 1 and False to 0 the sum is 3.