list_a = [101, 102, 105, 108, 110]
list_b = [105, 108, 112, 115]

set_a = set(list_a)
set_b = set(list_b)

# IDs in both
both = set_a.intersection(set_b)

# IDs in only one (Symmetric Difference)
unique = set_a.symmetric_difference(set_b)

print(f"In both: {both}")
print(f"Unique to one list: {unique}")