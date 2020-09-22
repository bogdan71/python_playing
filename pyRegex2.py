import re

matches = re.findall('finxter+?r', 'finxterrrr')
print(matches[0][:-1])