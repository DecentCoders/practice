with open("cities.txt","r+") as file:
    lines = file.readlines()
    line_count = 0
    for line in lines:
        line_count+=1
    print(line_count)     