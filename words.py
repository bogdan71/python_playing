words = ['cat','mouse','dog']
for w in words[:]:
    if len(w) > 3:
        words.insert(0, w)
print(words[0])