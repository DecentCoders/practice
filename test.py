# Goal: Calculate the average of a list and save a report
data = [80, 90, 100]

def get_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count  # Bug 1

result = get_average(data)

if result > 85:
    print("Great job!")  # Bug 2

with open("report.txt", "w") as f:
    f.write("The average was: " + result)  # Bug 3