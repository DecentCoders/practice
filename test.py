with open("cities.txt", "r") as file:
    lines = file.readlines()
    for line in lines: 
        if line.startswith("N"):
            print(line)