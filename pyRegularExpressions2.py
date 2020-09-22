import re

regex = r'[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,64}'

emails = [
    'ronald.mcdonalds@mcd.com',
    '12345%@000.com',
    'fast!cars4sale@gmail.com',
    'me.myhouse.mycity@co.uk',
    '__main__@py.com',
    'one+two@equals.four',
    'the_sky_is_blue@in-my-universe.com',
    'a@b.c'
]

accepted = [email for email in emails if re.match(regex, email)]

print(len(accepted))