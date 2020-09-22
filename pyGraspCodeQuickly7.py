def levenshtein(a, b):
    if not a: return len(b)
    if not b: return len(a)
    return min(levenshtein(a[1:], b[1:])+(a[0] != b[0]),
        levenshtein(a[1:], b)+1, levenshtein(a, b[1:])+1)

print(levenshtein("chess", "chello"))