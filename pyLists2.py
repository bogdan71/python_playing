# Create list of strings
customers = ["Alice", "Bob", "Ann", "Alice", "Charles"]

# Count each customer in list and store in dictionary
d = {k:customers.count(k) for k in customers}

# Print everything
print(d["Alice"])