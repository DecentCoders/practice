import os 

if(not os.path.exists("test")):
    os.mkdir("test")
for i in range(1,100):
    os.mkdir(f"test/day{i}")