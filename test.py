with open("cities.txt","r+") as file:
    lines = file.readlines()
    line_count = len(lines)
    print(line_count)        