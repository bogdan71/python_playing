import re

regex = '^(https?:\/\/)?(www\.)?[a-zA-Z0-9]{1,256}\.[a-zA-Z]{1,6}$'

urls = [
    'https://de.wikipedia.org',
    'nytimes.com',
    'https://www.google.de/?client=safari',
    'www.mywebsite.info',
    'https://www.google.de/?client=safari',
    'https://www.wayfair.de/v/checkout/basket'
]

rejected = [url for url in urls if not re.match(regex, url)]
print(len(rejected))