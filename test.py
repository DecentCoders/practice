sentence = "Life is short, we need Python."
sentence = sentence.lower()  # Convert all characters to lowercase
counts = {}
for c in sentence:
    counts[c] = counts.get(c, 0) + 1
print(counts)