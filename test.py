import os 
def os_practice():
    print(os.getcwd())
    print(os.listdir("icpc/"))
    a= input("Enter a directory: ")
    if os.path.exists(a):
        print("path exists")
    else:
        print("path didn't exist")
    new_dir = input("Enter new directory name: ")
    try:
        os.mkdir(new_dir)
        print("New directory created successfully")
    except:
        if os.path.exists(new_dir):
            print("Directory already exists..")
        else:
            print("something went wrong")
    os.makedirs("abc/bc/c")
    os.path.abspath("kbc/index.py")
    print(os.path.split(dir))
    print(os.path.basename(dir))
    
    dir = input("Enter the path:")
    print(os.name)
    print(os.cpu_count())
    print(os.getpid())
# ---------------------------



