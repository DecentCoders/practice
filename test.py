import os 
folders = os.listdir("test")
for folder in folders:
    print(folder)
    print(os.listdir(f"test/{folder}"))