import os
directory = input("Enter a directory you want to search in: ")
file_name = input("Enter the filename you want to search for: ")
if not file_name:
    print("The file doesn't exitst")
else:
    for root , dirs, files in os.walk('.'):
        for file in files:
            if file ==(file_name):
                full_path = os.path.join(root,file_name)
                print(f'Found the file,{full_path}')