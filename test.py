scores = {"Rick": 85, "Amy": 92, "Joe": 78, "Zelda": 99, "Bo": 88}

# Sort by value (the score), reversed for highest first
sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)

# Take the first three and print names
for i in range(3):
    print(f"{i+1}. {sorted_scores[i][0]}")