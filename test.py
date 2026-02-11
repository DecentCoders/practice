store_a = {"apples": 20, "orange": 15}
store_b = {"apples": 10, "bananas": 5}

total_stock = store_a.copy()

for item, count in store_b.items():
    if item in total_stock:
        total_stock[item] += count
    else:
        total_stock[item] = count

print(total_stock)