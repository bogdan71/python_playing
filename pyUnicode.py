def decrypt(s):
    l = [chr(ord(c)-2) for c in s]
    return ''.join(l)


print(decrypt("Ecguct"))


# Caesar