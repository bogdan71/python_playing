item_prices = [
    ('apple', 0.45),
    ('banana', 0.75),
    ('kiwi', 0.5),
    ('orange', 0.8)
]

prices = [price for item, price in item_prices]

print(sum(prices))