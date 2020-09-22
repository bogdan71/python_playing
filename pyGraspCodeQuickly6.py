# mg per 100g

omega3_table = {
    "Salmon" : 2260,
    "Hering" : 1729,
    "Sardines" : 1480,
    "Flaxseeds" : 53400,
    "Eggs" : 400
    }

y = max(omega3_table, 
    key=lambda x : omega3_table[x])

print(y)
