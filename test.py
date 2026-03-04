import os

# Step 1: Create test folder and 100 empty .txt files
def create_test_files():
    test_dir = "batch_rename_test"
    os.makedirs(test_dir, exist_ok=True)  # Create folder (ignore if exists)
    
    # Create 100 empty files (file_001.txt to file_100.txt)
    for i in range(1, 101):
        # Use zfill(3) for 3-digit numbering (001 instead of 1)
        filename = f"file_{str(i).zfill(3)}.txt"
        file_path = os.path.join(test_dir, filename)
        # Create empty file
        with open(file_path, "w") as f:
            pass
    print(f"Created 100 test files in {test_dir}")

# Step 2: Rename .txt to .jpg (photo_001.jpg)
def batch_rename_files():
    test_dir = "batch_rename_test"
    if not os.path.isdir(test_dir):
        print(f"Error: {test_dir} does not exist!")
        return
    
    # Iterate over all files in the folder
    for filename in os.listdir(test_dir):
        # Only process .txt files
        if filename.endswith(".txt") and filename.startswith("file_"):
            # Extract number (e.g., "file_001.txt" → "001")
            file_number = filename.split("_")[1].split(".")[0]
            # New filename: photo_001.jpg
            new_filename = f"photo_{file_number}.jpg"
            # Full paths (cross-platform)
            old_path = os.path.join(test_dir, filename)
            new_path = os.path.join(test_dir, new_filename)
            
            # Rename file
            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} → {new_filename}")
            except Exception as e:
                print(f"Error renaming {filename}: {e}")

# Run the functions
create_test_files()
batch_rename_files()