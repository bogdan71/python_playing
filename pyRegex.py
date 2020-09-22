import re

pattern = '[a-z]+(?! world)'
string = 'hello world'
print(re.findall(pattern, string))
