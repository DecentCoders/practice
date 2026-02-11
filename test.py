matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat_list = []

for sublist in matrix:
    for item in sublist:
        flat_list.append(item)

print(flat_list)