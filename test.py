with open("icpc/test.txt","r") as file:
    file.truncate(5) 
    data = file.readline()
    print(data)