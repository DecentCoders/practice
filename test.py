with open("icpc/test.txt","r") as file:
    file.seek(7)    
    data = file.read(6)
    print(file.tell())
    print(data)