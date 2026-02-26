import os
try:
    file_name = input("enter directory name:")
    os.rmdir(file_name)
except Exception as e:
    print(e)