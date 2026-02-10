counts = {"INFO": 0, "ERROR": 0}
try:
    with open("server.log",'r') as file:
        for line in file:
            if line.startswith('INFO'):
                counts["INFO"] +=1
            elif line.startswith("ERROR"):
                counts["ERROR"] += 1
    print(f'Log Summary: {counts}')
except FileNotFoundError:
    print("File not found")