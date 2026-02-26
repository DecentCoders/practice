# Import the required os module for file system operations
import os

# Traverse current directory (.) and all its subdirectories with os.walk()
# root = current folder path | dirs = list of subfolders in root | files = list of files in root
for root, dirs, files in os.walk('.'):
    # Loop through every file in the current folder (root)
    for file in files:
        # Check if the file has a .txt extension
        if file.endswith('.txt'):
            # Create the full file path (combines folder path + file name, OS-compatible)
            full_txt_path = os.path.join(root, file)
            # Print the full path of the .txt file
            print(f"Found .txt file: {full_txt_path}")