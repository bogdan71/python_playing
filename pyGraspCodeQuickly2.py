def encrypt(s):
    return ''.join(reversed(s))

def decrypt(s):
    return s[::-1]

# print(decrypt("SomeTextBalony"))

cleartext = """Nothink travels \
faster than the speed of light \
with the exception of bad news"""

print(cleartext == decrypt(encrypt(cleartext)))
