import os
try:
    file_name = input("enter file name:")
    os.remove(f"test/{file_name}")
except Exception as e:
    print(e)